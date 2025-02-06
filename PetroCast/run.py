"""
Core module for the PetroCast application.

This script loads data, fits models, calculates cumulative production,
and visualizes results for resource analysis.
"""

from pathlib import Path
import tomli
import pandas as pd
from PetroCast.utils.data_processing import load_data
from PetroCast.utils.curve_fitting import fit_hubbert_curve, fit_laherrere_model
from PetroCast.utils.cumulative_production import calculate_cumulative_production
from PetroCast.utils.calculate_future_prod import calculate_future_production
from PetroCast.models.hubbert_curve_model import hubbert_curve
from PetroCast.models.laherrere_model import laherrere_bell_curve
from PetroCast.visualization import plot_results
import numpy as np

def run_petrocast(config_path, urr_key):
    # Load TOML config
    with open(config_path, "rb") as file:
        config = tomli.load(file)

    dataset_path = Path(config["dataset"])
    urr_file = Path(config["urr_file"])
    output_pth = Path(config["output_pth"])
    unit = config.get("unit", "EJ")

    # Load dataset
    years, production_ej = load_data(dataset_path)
    production_gb = production_ej / 6.9

    # Load URR estimate
    df = pd.read_csv(urr_file)
    df["estimate"] = df["estimate"].str.strip()
    if urr_key not in df["estimate"].tolist():
        raise ValueError(f"URR key '{urr_key}' not found. Available: {df['estimate'].tolist()}")
    urr = df.loc[df["estimate"] == urr_key, "value"].values[0]

    # Convert data based on unit
    production = production_gb if unit == "Gb" else production_ej

    # Fit models
    laherrere_params = fit_laherrere_model(years, production, urr)
    hubbert_params = fit_hubbert_curve(years, production, urr)

    # Print results
    print(f"\nUsing dataset: {dataset_path}")
    print(f"URR: {urr:,.1f} {unit} (Key: {urr_key})\n")
    print(f"Laherrère Model Peak Year: {int(laherrere_params['tm'])}")
    print(f"Hubbert Model Peak Year: {int(hubbert_params['peak_time'])}\n")

    # Calculate cumulative extraction
    hubbert_cumulative = calculate_cumulative_production(years, production, hubbert_params, hubbert_curve)
    laherrere_cumulative = calculate_cumulative_production(years, production, laherrere_params, laherrere_bell_curve)

    print(f"Hubbert Cumulative: {hubbert_cumulative:.2f} {unit}")
    print(f"Laherrère Cumulative: {laherrere_cumulative:.2f} {unit}")
    
    # Generate full fit
    future_years = np.arange(years[0], 2101)
    data = {
        "years": years, 
        "production": production, 
        "future_years": future_years, 
        "tm":int(laherrere_params['tm']), 
        "peak_time":int(hubbert_params['peak_time'])
        }
    laherre_fit_full, hubbert_fit_full = calculate_future_production(
        data = data, 
        laherrere_params=laherrere_params, 
        hubbert_params=hubbert_params, 
        urr=urr
        )

    # Generate plots
    plot_results(data = data, laherre_full = laherre_fit_full, hubbert_full = hubbert_fit_full, output_pth=output_pth)
