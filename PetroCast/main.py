"""
Main module for the PetroCast application.

This script loads data, fits models, calculates cumulative production,
and visualizes results for resource analysis.
"""

import numpy as np
from PetroCast.visualization import plot_results
from PetroCast.utils.data_processing import load_data
from PetroCast.utils.curve_fitting import fit_hubbert_curve, fit_laherrere_model
from PetroCast.utils.cumulative_production import calculate_cumulative_production
from PetroCast.models.hubbert_curve_model import hubbert_curve
from PetroCast.models.laherrere_model import laherrere_bell_curve
from data.output.Oil_estimate import saved_output


def main():
    """
    Main function for running the PetroCast application.

    Loads data, fits Laherrère and Hubbert models, calculates cumulative production,
    and visualizes the results.
    """
    filepath = (
        r"C:\Users\oleva\PycharmProjects\PetroCast\data\raw\data1_oil_his_havard.csv"
    )
    years, production = load_data(filepath)

    # Define Ultimate Recoverable Resources (URR)
    urr = saved_output  # Adjust URR based on updated estimates

    # Fit Laherrère and Hubbert models
    laherrere_params = fit_laherrere_model(years, production, urr)
    hubbert_params = fit_hubbert_curve(years, production, urr)

    print(f"Laherrère Model Parameters: {laherrere_params}")
    print(f"Hubbert Model Parameters: {hubbert_params}")

    # Calculate cumulative extraction
    hubbert_cumulative = calculate_cumulative_production(
        years, production, hubbert_params, hubbert_curve
    )
    laherrere_cumulative = calculate_cumulative_production(
        years, production, laherrere_params, laherrere_bell_curve
    )

    # Print cumulative extraction results in Exajoules (EJ)
    print(f"Hubbert Model Cumulative Extraction: {hubbert_cumulative:.2f} EJ")
    print(f"Laherrère Model Cumulative Extraction: {laherrere_cumulative:.2f} EJ")

    # Visualize results
    future_years = np.arange(years[0], 2101)
    data = {
        "years": years,
        "production": production,
        "future_years": future_years
    }
    plot_results(data, laherrere_params, hubbert_params, urr)


if __name__ == "__main__":
    main()
