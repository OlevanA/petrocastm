"""
Curve fitting utilities for Laherrère and Hubbert models.

This module provides functions for fitting historical production data
using the Laherrère and Hubbert models.
"""

import numpy as np
from scipy.optimize import curve_fit
from PetroCast.models.laherrere_model import laherrere_bell_curve
from PetroCast.models.hubbert_curve_model import hubbert_curve


def fit_hubbert_curve(years, production, ultimate_recoverable_resources):
    """
    Fit the Hubbert curve to historical production data.

    Parameters:
    - years (array-like): Array of years (time).
    - production (array-like): Array of historical production data.
    - ultimate_recoverable_resources (float): Ultimate Recoverable Resources (URR).

    Returns:
    - dict: Fitted parameters {'urr', 'steepness', 'peak_time'}.
    """
    # Validate inputs
    if not isinstance(years, (np.ndarray, list)):
        raise TypeError("Parameter 'years' must be an array or list.")
    if not isinstance(production, (np.ndarray, list)):
        raise TypeError("Parameter 'production' must be an array or list.")
    if not np.issubdtype(np.array(years).dtype, np.number):
        raise ValueError("Parameter 'years' must contain only numeric values.")
    if not np.issubdtype(np.array(production).dtype, np.number):
        raise ValueError("Parameter 'production' must contain only numeric values.")

    def hubbert_function(t, steepness, peak_time):
        return hubbert_curve(t, ultimate_recoverable_resources, steepness, peak_time)

    # Initial guess for parameters
    initial_guess = [0.02, 2040]  # Allow later peak (conservative assumption)
    bounds = ([0.01, 2030], [0.05, 2040])  # Constrain t_peak to 2030-2040

    # Perform curve fitting
    params, _ = curve_fit(hubbert_function, years, production, p0=initial_guess, bounds=bounds)

    return {"urr": ultimate_recoverable_resources, "steepness": params[0], "peak_time": params[1]}


def fit_laherrere_model(years, production, ultimate_recoverable_resources):
    """
    Fit the Laherrère bell curve model to historical production data.

    Parameters:
    - years (array-like): Array of years (time).
    - production (array-like): Array of historical production data.
    - ultimate_recoverable_resources (float): Ultimate Recoverable Resources (URR).

    Returns:
    - dict: Fitted parameters {'peak_production', 'tm', 'c'}.
    """
    # Validate inputs
    if not isinstance(years, (np.ndarray, list)):
        raise TypeError("Parameter 'years' must be an array or list.")
    if not isinstance(production, (np.ndarray, list)):
        raise TypeError("Parameter 'production' must be an array or list.")
    if not np.issubdtype(np.array(years).dtype, np.number):
        raise ValueError("Parameter 'years' must contain only numeric values.")
    if not np.issubdtype(np.array(production).dtype, np.number):
        raise ValueError("Parameter 'production' must contain only numeric values.")

    def laherrere_function(t, peak_production, peak_time, width):
        return laherrere_bell_curve(t, peak_production, peak_time, width, ultimate_recoverable_resources)

    # Initial guess for parameters
    initial_guess = [max(production), 2040, 200]  # Assume a peak in 2040 with a reasonable width
    bounds = ([0, 2030, 10], [np.inf, 2040, 300])  # Adjust bounds for a peak after 2030

    # Perform curve fitting
    params, _ = curve_fit(laherrere_function, years, production, p0=initial_guess, bounds=bounds)

    return {"peak_production": params[0], "tm": params[1], "c": params[2]}
