"""
This module provides visualization functionality for plotting production data and model fits
using Laherrère and Hubbert curve models.
"""
import uuid
from pathlib import Path  # Standard library import first
import matplotlib.pyplot as plt
import numpy as np



def plot_results(data: dict, laherre_full: np.ndarray, hubbert_full: np.ndarray,
                 output_path: Path | str):
    """
    Plots historical production data along with Laherrère and Hubbert model fits.

    Parameters:
        data (dict): Dictionary containing 'years', 'production', and 'future_years'.
        laherre_full (np.ndarray): Laherrère model output.
        hubbert_full (np.ndarray): Hubbert model output.
        output_path (Path or str): Path where the plot will be saved.
    """
    output_path = Path(output_path)  # Ensure it's a Path object
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Create directory if needed

    years = data["years"]
    production = data["production"]
    future_years = data["future_years"]

    fig, _ = plt.subplots(figsize=(14, 7))
    full_years = np.arange(years[0], future_years[-1] + 1)

    plt.plot(full_years, laherre_full, color="orange", label="Laherrère Model Fit")
    plt.plot(full_years, hubbert_full, color="red", label="Hubbert Model Fit")
    plt.scatter(years, production, color="blue", label="Historical Annual Production", s=10)

    plt.axvline(data["tm"], color="green", linestyle="--", label="Laherrère Peak Year")
    plt.axvline(data["peak_time"], color="purple", linestyle="--", label="Hubbert Peak Year")

    plt.xlabel("Year")
    unit = data.get("unit", "EJ")  # either unit or EJ as default
    plt.ylabel(f"Production ({unit}/year)")  # Unit defined by TOML
    plt.title("Production and Model Fits (Full Curve)")
    plt.legend()
    plt.grid()

    # Save the figure and close it to avoid file lock issues
    output_filename = f"results_{data['urr_key']}_{str(uuid.uuid4())[-4:]}.png"
    fig.savefig(output_path / output_filename)
    plt.close(fig)
    plt.close("all")  # Extra safety to close any lingering figures

    print(f"Plot saved to: {output_path}")
