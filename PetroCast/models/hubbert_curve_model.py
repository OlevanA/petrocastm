"""
This module provides an implementation of the Hubbert curve model for resource extraction.

The Hubbert curve is commonly used to model production rates over time based on
parameters such as ultimate recoverable resources (URR), steepness, and peak production time.
"""

import numpy as np


def hubbert_curve(time: np.ndarray, urr: float, steepness: float, peak_time: float) -> np.ndarray:
    """
    Compute the Hubbert curve for annual production.

    The Hubbert curve models the annual production rate of a resource as a function of time,
    based on parameters such as the ultimate recoverable resources (URR), the steepness
    of the curve, and the year of peak production.

    Parameters:
        time (np.ndarray): Array of years for which production is calculated.
        urr (float): Ultimate recoverable resources (URR),representing the total extractable amount
        steepness (float): Controls the steepness of the curve.
        peak_time (float): Year of peak production.

    Returns:
        np.ndarray: Annual production rates for each year in the `time` array.
    """
    if not isinstance(time, np.ndarray):
        raise TypeError("Parameter 'time' must be a numpy array.")

    if not all(isinstance(param, (float, int)) for param in [urr, steepness, peak_time]):
        raise TypeError("Parameters 'urr', 'steepness', and "
                        "'peak_time' must be floats or integers.")

    # Calculate the exponential term
    exponential_term = np.exp(-steepness * (time - peak_time))

    # Compute the production rate
    production_rate = (urr * steepness * exponential_term) / ((1 + exponential_term) ** 2)

    return production_rate
