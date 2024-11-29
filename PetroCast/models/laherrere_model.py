"""
This module contains the Laherrère bell curve model for modeling resource extraction dynamics.
"""

import numpy as np

def laherrere_bell_curve(
    t: np.ndarray, peak_production: float, tm: float, c: float, urr: float = None
) -> np.ndarray:
    """
    Laherrère bell curve model.

    This function models production rates based on the Laherrère bell curve, which is
    commonly used for modeling resource extraction dynamics.

    Parameters:
    - t (np.ndarray or float): Time (array or scalar).pylint
    - peak_production (float): Peak production rate (EJ/year).
    - tm (float): Time of peak production (year).
    - c (float): Width parameter controlling steepness.
    - urr (float, optional): Ultimate Recoverable Resources (not used in this function).

    Returns:
    - np.ndarray or float: Production rate at time t.
    """
    if not isinstance(t, (np.ndarray, float, int)):
        raise TypeError("Parameter 't' must be a scalar or numpy array.")
    if not isinstance(peak_production, (float, int)):
        raise TypeError("Parameter 'peak_production' must be a float or int.")
    if not isinstance(tm, (float, int)):
        raise TypeError("Parameter 'tm' must be a float or int.")
    if not isinstance(c, (float, int)):
        raise TypeError("Parameter 'c' must be a float or int.")
    if urr is not None and not isinstance(urr, (float, int)):
        raise TypeError("Parameter 'urr' must be a float or int if provided.")

    # Compute the hyperbolic cosine term
    cosh_term = np.cosh(-5 / c * (t - tm))

    # Compute production rate
    production_rate = 2 * peak_production / (1 + cosh_term)

    return production_rate
