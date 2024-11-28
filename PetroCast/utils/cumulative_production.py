"""
Module for calculating cumulative production.
"""

import numpy as np


def calculate_cumulative_production(years, production, model_params, model_func):
    """
    Calculate cumulative production by combining historical production and future projections.

    Parameters:
    - years (array-like): Historical years.
    - production (array-like): Historical production data in Exajoules.
    - model_params (dict): Parameters for the model (Hubbert or Laherrère).
    - model_func (callable): Model function to use for predictions.

    Returns:
    - float: Total cumulative production in Exajoules.
    """
    # Validate inputs
    if not isinstance(years, (np.ndarray, list)):
        raise TypeError("years must be a list or numpy array.")
    if not isinstance(production, (np.ndarray, list)):
        raise TypeError("production must be a list or numpy array.")
    if not isinstance(model_params, dict):
        raise TypeError("model_params must be a dictionary.")
    if not callable(model_func):
        raise TypeError("model_func must be callable.")

    # Generate future years starting from the last historical year
    future_years = np.arange(years[-1] + 1, 2101)

    # We need to unpack the model parameters before passing them to the model function.
    projected_production = model_func(future_years, *model_params.values())

    # Calculate cumulative production
    historical_cumulative = np.sum(production)
    future_cumulative = np.sum(projected_production)
    total_cumulative = historical_cumulative + future_cumulative

    return total_cumulative
