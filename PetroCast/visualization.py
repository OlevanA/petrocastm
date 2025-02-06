"""
This module provides visualization functionality for plotting production data and model fits
using Laherrère and Hubbert curve models.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_results(data, laherre_full, hubbert_full, output_pth):
    """
    Plots historical production data along with Laherrère and Hubbert model fits.

    Parameters:
        laherre_data (np.ndarray)
        hubbert_data (np.ndarray)
        output_pth (Path): Path to the directory where the plot will be saved.
    """
    if not output_pth.exists():
        output_pth.mkdir()

    years = data['years']
    production = data['production']
    future_years = data['future_years']

    fig,ax = plt.subplots(figsize=(14, 7))
    full_years = np.arange(years[0], future_years[-1] + 1)

    plt.plot(full_years, laherre_full, color="orange", label="Laherrère Model Fit")
    #
    plt.plot(full_years, hubbert_full, color="red", label="Hubbert Model Fit")

    plt.scatter(years, production, color="blue", label="Historical Annual Production", s=10)

    plt.axvline(data["tm"], color="green", linestyle="--", label="Laherrère Peak Year")
    plt.axvline(data["peak_time"], color="purple", linestyle="--",
                label="Hubbert Peak Year")

    plt.xlabel("Year")
    plt.ylabel(f"Production (EJ/year or similar)")
    plt.title("Production and Model Fits (Full Curve)")
    plt.legend()
    plt.grid()
    plt.show(block=False)

    fig.savefig(output_pth / "results.png")
