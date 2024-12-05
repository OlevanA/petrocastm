import pandas as pd


def load_historical_data(filepath):
    """
    Load historical production data from a CSV file and calculate the reference year (t0),
    initial cumulative production (Q0), and set initial guesses for parameters.
    :param filepath: Path to the CSV file.
    :return: A tuple containing the DataFrame, reference year (t0), Q0, and initial parameter guesses.
    """
    # Load the data
    data = pd.read_csv(filepath)

    # Ensure the data contains the required columns
    if 'Year' not in data.columns or 'Production' not in data.columns:
        raise ValueError("The CSV file must contain 'Year' and 'Production' columns.")

    # Sort the data by year to ensure chronological order
    data = data.sort_values(by='Year')

    # Extract the last year as the reference year (t0)
    t0 = data['Year'].iloc[-1]

    # Calculate cumulative production (Q0) up to the last year
    data['cumulative_production'] = data['Production'].cumsum()
    Q0 = data['cumulative_production'].iloc[-1]

    # Set initial guesses for K and τ
    K_guess = Q0 * 1.5  # Assume URR (K) is 1.5 times the cumulative production as an initial guess
    tau_guess = 20  # Characteristic time in years (can be adjusted)

    # Return the data, t0, Q0, and initial parameters
    initial_params = {
        "K": K_guess,
        "Q0": Q0,
        "t0": t0,
        "tau": tau_guess
    }

    return data, t0, Q0, initial_params


# Example usage
if __name__ == "__main__":
    # Path to your CSV file
    filepath = r"C:\Users\oleva\PycharmProjects\PetroCast\data\raw\data1_oil_his_havard.csv"

    # Load the data and calculate parameters
    try:
        historical_data, reference_year, cumulative_production, initial_parameters = load_historical_data(filepath)

        print("Historical Data:")
        print(historical_data.head())  # Display the first few rows of the data
        print(f"Reference Year (t0): {reference_year}")
        print(f"Initial Cumulative Production (Q0): {cumulative_production} metric tons")
        print("Initial Parameter Guesses:")
        for key, value in initial_parameters.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")
