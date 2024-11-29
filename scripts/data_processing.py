"""
This module provides utilities for loading and processing historical production data.

Functions:
    load_data(filepath): Loads production data from a CSV file.
"""
import pandas as pd

def load_data(filepath):
    """
    Load historical production data from CSV file.

    Parameters:
        filepath (str): Path to CSV file.

    Returns:
        tuple: (years, production) as numpy arrays.
    """
    data = pd.read_csv(filepath)
    years = data["Year"].to_numpy()
    production = data["Production"].to_numpy()
    return years, production
