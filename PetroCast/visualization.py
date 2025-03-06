"""
This module provides visualization functionality for plotting production data and model fits
using Laherrère and Hubbert curve models.
"""

from pathlib import Path  # Standard library import first
import matplotlib.pyplot as plt
import numpy as np


def plot_results(data, laherre_full, hubbert_full, output_pth):
    """
    Plots historical production data along with Laherrère and Hubbert model fits.

    Parameters:
        data (dict): Dictionary containing 'years', 'production', and 'future_years'.
        laherre_full (np.ndarray): Laherrère model output.
        hubbert_full (np.ndarray): Hubbert model output.
        output_pth (Path or str): Path where the plot will be saved.
    """
    output_pth = Path(output_pth)  # Ensure it's a Path object
    output_pth.parent.mkdir(parents=True, exist_ok=True)  # Create directory if needed

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
    plt.ylabel("Production (EJ/year or similar)")
    plt.title("Production and Model Fits (Full Curve)")
    plt.legend()
    plt.grid()

    # Save the figure and close it to avoid file lock issues
    fig.savefig(output_pth / "results.png")
    plt.close(fig)
    plt.close("all")  # Extra safety to close any lingering figures

    print(f"Plot saved to: {output_pth}")
