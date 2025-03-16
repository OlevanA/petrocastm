"""
Utility functions for data processing.

This module provides functions to load and preprocess historical production
data from CSV files.
"""

import pandas as pd
import numpy as np


def load_data(filepath):
    """
    Load historical production data from a CSV file.

    Parameters:
        filepath (Path): Path to the CSV file.

    Returns:
        tuple: (years, production) as numpy arrays.

    Raises:
        ValueError: If an error occurs while reading or processing the file.
    """

        data = pd.read_csv(filepath)

        # Convert "Year" to numeric, forcing non-numeric values to NaN
        data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

        # Drop rows where 'Year' or 'Production' have NaN values
        data.dropna(subset=['Year', 'Production'], inplace=True)

        years = data["Year"].to_numpy(dtype=np.float64)
        production = data["Production"].to_numpy(dtype=np.float64)

        return years, production


