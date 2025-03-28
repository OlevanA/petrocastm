"""
Core module for the PetroCast application.

This script loads data, fits models, calculates cumulative production,
and visualizes results for resource analysis.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import tomli

from petrocast.utils.data_processing import load_data
from petrocast.utils.curve_fitting import fit_hubbert_curve, fit_laherrere_model
from petrocast.utils.cumulative_production import calculate_cumulative_production
from petrocast.utils.calculate_future_prod import calculate_future_production
from petrocast.models.hubbert_curve_model import hubbert_curve
from petrocast.models.laherrere_model import laherrere_bell_curve
from petrocast.visualization import plot_results

print("Might take some time...")

def run_petrocast(config_path, urr_key,root_path):
    """Executes the PetroCast pipeline with given configuration."""
    print("Wait, processing request...")
    # Load TOML config
    with open(config_path, "rb") as file:
        config = tomli.load(file)

    dataset_file = Path.joinpath(root_path,config["dataset"])
    urr_file = Path.joinpath(root_path,config["urr_file"])
    output_path = Path.joinpath(root_path,config["output_path"])
    unit = config.get("unit", "EJ")

    # Load dataset
    years, production_ej = load_data(dataset_file)
    production_gb = production_ej / 6.9

    # Load URR estimate
    df = pd.read_csv(urr_file)
    df["estimate"] = df["estimate"].str.strip()

    if urr_key not in df["estimate"].tolist():
        raise ValueError(
            f"URR key '{urr_key}' not found. Available keys: {df['estimate'].tolist()}"
        )

    urr = float(df.loc[df["estimate"] == urr_key, "value"].values[0])

    # Convert data based on unit
    production = production_gb if unit == "Gb" else production_ej

    # Fit models
    laherrere_params = fit_laherrere_model(years, production, urr)
    hubbert_params = fit_hubbert_curve(years, production, urr)

    # Print results
    print(f"\nUsing dataset: {dataset_file.stem}")
    print(f"URR: {urr:,.1f} {unit} (Key: {urr_key})\n")
    print(f"Laherrère Model Peak Year: {int(laherrere_params['tm'])}")
    print(f"Hubbert Model Peak Year: {int(hubbert_params['peak_time'])}\n")

    # Calculate cumulative extraction
    hubbert_cumulative = calculate_cumulative_production(
        years, production, hubbert_params, hubbert_curve
    )
    laherrere_cumulative = calculate_cumulative_production(
        years, production, laherrere_params, laherrere_bell_curve
    )

    print(f"Hubbert Cumulative: {hubbert_cumulative:.2f} {unit}")
    print(f"Laherrère Cumulative: {laherrere_cumulative:.2f} {unit}")

    # Generate full fit
    future_years = np.arange(years[0], 2101)
    data = {
        "years": years,
        "production": production,
        "future_years": future_years,
        "tm": int(laherrere_params["tm"]),
        "peak_time": int(hubbert_params["peak_time"]),
        "urr_key": urr_key,
        "unit": unit,
    }

    laherre_fit_full, hubbert_fit_full = calculate_future_production(
        data=data,
        laherrere_params=laherrere_params,
        hubbert_params=hubbert_params,
        urr=urr,
    )

    # Generate plots
    plot_results(
        data=data,
        laherre_full=laherre_fit_full,
        hubbert_full=hubbert_fit_full,
        output_path=output_path,
    )
