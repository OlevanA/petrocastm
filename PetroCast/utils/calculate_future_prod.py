"""
This module provides calculation functionality for calculating future production data and model fits
using Laherrère and Hubbert curve models.
"""
import numpy as np
from PetroCast.models.laherrere_model import laherrere_bell_curve
from PetroCast.models.hubbert_curve_model import hubbert_curve

def calculate_future_production(data: dict, laherrere_params: dict, hubbert_params: dict, urr: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Calculates future production based on Laherrère and Hubbert models.

    Parameters:
        data (dict): Contains 'years', 'production', and 'future_years'.
        laherrere_params (dict): Parameters for the Laherrère model.
        hubbert_params (dict): Parameters for the Hubbert model.
        urr (float): Ultimate Recoverable Resource value.
    """
    years = data['years']
    production = data['production']
    future_years = data['future_years']

    full_years = np.arange(years[0], future_years[-1] + 1)

    # Extract the parameters expected by laherrere_bell_curve
    laherrere_fit_full = laherrere_bell_curve(
        full_years,
        peak_production=laherrere_params['peak_production'],
        tm=laherrere_params['tm'],
        c=laherrere_params['c'],
        urr=urr
    )

    # Call hubbert_curve with specific expected parameters
    hubbert_fit_full = hubbert_curve(
        full_years,
        urr=hubbert_params['urr'],
        steepness=hubbert_params['steepness'],
        peak_time=hubbert_params['peak_time']
    )
    
    return laherrere_fit_full, hubbert_fit_full
