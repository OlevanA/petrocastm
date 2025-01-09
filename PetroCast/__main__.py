"""
Main module for the PetroCast application.

This script loads data, fits models, calculates cumulative production,
and visualizes results for resource analysis.
"""
from pathlib import Path
import numpy as np
from PetroCast.visualization import plot_results
from PetroCast.utils.data_processing import load_data
from PetroCast.utils.curve_fitting import fit_hubbert_curve, fit_laherrere_model
from PetroCast.utils.cumulative_production import calculate_cumulative_production
from PetroCast.models.hubbert_curve_model import hubbert_curve
from PetroCast.models.laherrere_model import laherrere_bell_curve
from data.output.Oil_estimate import saved_output
from PetroCast.utils.determine_input import determine_input


def main():
    """
    Main function for running the PetroCast application.

    Loads data, fits Laherrère and Hubbert models, calculates cumulative production,
    and visualizes the results.
    """
    filepath = Path("data/raw/data1_oil_his_havard.csv")
    years, production_ej = load_data(filepath)
    production_gb = production_ej / 6.9

    run_estimate = True

    while run_estimate == True:
        urr, unit = determine_input()
        # Define Ultimate Recoverable Resources (URR)
        #urr = saved_output  # Adjust URR based on updated estimates

        # Convert data if necessary in the inpout unit
        if unit == "Gb":
            production = production_gb
        elif unit == "EJ":
            production = production_ej


        # Fit Laherrère and Hubbert models
        laherrere_params = fit_laherrere_model(years, production, urr)
        print(laherrere_params)
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
        print(f"Hubbert Model Cumulative Extraction: {hubbert_cumulative:.2f} {unit}")
        print(f"Laherrère Model Cumulative Extraction: {laherrere_cumulative:.2f} {unit}")

        # Visualize results
        future_years = np.arange(years[0], 2101)
        data = {
            "years": years,
            "production": production,
            "future_years": future_years
        }
        plot_results(data, laherrere_params, hubbert_params, urr)

        another = input("\nDo you want to check another estimate? (yes/no): ").strip().lower()
        if another != 'yes':
            run_estimate = False



if __name__ == "__main__":
    main()
