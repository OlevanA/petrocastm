"""
This module provides visualization functionality for plotting production data and model fits
using Laherrère and Hubbert curve models.
"""

import matplotlib.pyplot as plt
import numpy as np
from PetroCast.models.laherrere_model import laherrere_bell_curve
from PetroCast.models.hubbert_curve_model import hubbert_curve


def plot_results(data, laherrere_params, hubbert_params, urr):
    """
    Plots historical production data along with Laherrère and Hubbert model fits.

    Parameters:
        data (dict): Contains 'years', 'production', and 'future_years'.
        laherrere_params (dict): Parameters for the Laherrère model.
        hubbert_params (dict): Parameters for the Hubbert model.
        urr (float): Ultimate Recoverable Resource value.
    """
    years = data['years']
    production = data['production']
    future_years = data['future_years']

    plt.figure(figsize=(14, 7))
    full_years = np.arange(years[0], future_years[-1] + 1)

    # Extract the parameters expected by laherrere_bell_curve
    laherrere_fit_full = laherrere_bell_curve(
        full_years,
        peak_production=laherrere_params['peak_production'],
        tm=laherrere_params['tm'],
        c=laherrere_params['c'],
        urr=urr
    )
    plt.plot(full_years, laherrere_fit_full, color="orange", label="Laherrère Model Fit")

    # Call hubbert_curve with specific expected parameters
    hubbert_fit_full = hubbert_curve(
        full_years,
        urr=hubbert_params['urr'],
        steepness=hubbert_params['steepness'],
        peak_time=hubbert_params['peak_time']
    )
    plt.plot(full_years, hubbert_fit_full, color="red", label="Hubbert Model Fit")

    plt.scatter(years, production, color="blue", label="Historical Annual Production", s=10)

    plt.axvline(laherrere_params["tm"], color="green", linestyle="--", label="Laherrère Peak Year")
    plt.axvline(hubbert_params["peak_time"], color="purple", linestyle="--",
                label="Hubbert Peak Year")

    plt.xlabel("Year")
    plt.ylabel(f"Production (EJ/year or similar)")
    plt.title("Production and Model Fits (Full Curve)")
    plt.legend()
    plt.grid()
    plt.show(block=False)
