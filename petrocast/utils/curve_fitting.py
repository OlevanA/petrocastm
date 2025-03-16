"""
Curve fitting utilities for Laherrère and Hubbert models.

This module provides functions for fitting historical production data
using the Laherrère and Hubbert models.
"""

import numpy as np
from scipy.optimize import curve_fit
from petrocast.models.laherrere_model import laherrere_bell_curve
from petrocast.models.hubbert_curve_model import hubbert_curve


def fit_hubbert_curve(years, production, ultimate_recoverable_resources):
    """
    Fit the Hubbert curve to historical production data.

    Parameters:
        years (array-like): Array of years (time).
        production (array-like): Array of historical production data.
        ultimate_recoverable_resources (float): Ultimate Recoverable Resources (URR).

    Returns:
        dict: Fitted parameters {'urr', 'steepness', 'peak_time'}.
    """
    # Validate inputs
    if not isinstance(years, (np.ndarray, list)) or not all(
        isinstance(val, (int, float)) for val in years
    ):
        raise TypeError("Parameter 'years' must be a list or NumPy array of numeric values.")

    if not isinstance(production, (np.ndarray, list)) or not all(
        isinstance(val, (int, float)) for val in production
    ):
        raise TypeError("Parameter 'production' must be a list or NumPy array of numeric values.")

    def hubbert_function(t, steepness, peak_time):
        return hubbert_curve(t, ultimate_recoverable_resources, steepness, peak_time)

    # Initial guess and bounds
    initial_guess = [0.02, 2040]  # Conservative peak assumption
    bounds = ([0.01, 2030], [0.05, 2040])  # Restrict peak time between 2030-2040

    # Perform curve fitting

    result = curve_fit(
        hubbert_function, years, production, p0=initial_guess, bounds=bounds
    )

    # Unpack correctly, handling unexpected extra values
    if len(result) >= 2:
        params, _ = result[:2]  # Only take first two values
        steepness, peak_time = params
    else:
        raise ValueError(f"Unexpected number of parameters returned: {len(result)}")


    return {"urr": ultimate_recoverable_resources, "steepness": steepness, "peak_time": peak_time}


def fit_laherrere_model(years, production, ultimate_recoverable_resources):
    """
    Fit the Laherrère bell curve model to historical production data.

    Parameters:
        years (array-like): Array of years (time).
        production (array-like): Array of historical production data.
        ultimate_recoverable_resources (float): Ultimate Recoverable Resources (URR).

    Returns:
        dict: Fitted parameters {'peak_production', 'tm', 'c'}.
    """
    # Validate inputs
    if not isinstance(years, (np.ndarray, list)) or not all(
        isinstance(val, (int, float)) for val in years
    ):
        raise TypeError("Parameter 'years' must be a list or NumPy array of numeric values.")

    if not isinstance(production, (np.ndarray, list)) or not all(
        isinstance(val, (int, float)) for val in production
    ):
        raise TypeError("Parameter 'production' must be a list or NumPy array of numeric values.")

    def laherrere_function(t, peak_production, peak_time, width):
        return laherrere_bell_curve(
            t, peak_production, peak_time, width, ultimate_recoverable_resources
        )

    # Initial guess and bounds
    initial_guess = [max(production), 2040, 200]  # Peak at 2040 with reasonable width
    bounds = ([0, 2030, 10], [np.inf, 2040, 300])  # Adjusted for peak time limits

    # Perform curve fitting

    result = curve_fit(
        laherrere_function, years, production, p0=initial_guess, bounds=bounds
    )

    # Unpack correctly, handling unexpected extra values
    if len(result) >= 2:
        params, _ = result[:2]  # Only take first two values
        peak_production, peak_time, c = params
    else:
        raise ValueError(f"Unexpected number of parameters returned: {len(result)}")



    return {"peak_production": peak_production, "tm": peak_time, "c": c}
