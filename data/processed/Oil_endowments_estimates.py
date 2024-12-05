import pandas as pd

# Load the CSV file into a DataFrame
file_path_endow = r'C:\Users\oleva\PycharmProjects\PetroCast\data\raw\sorted_oil_endowments_with_estimations.csv'  # Replace with the correct path if needed
df = pd.read_csv(file_path_endow)


# Function to get the EJ value for a specific estimate
def get_ej_value(estimate_name):
    """
    Get the EJ value for a given estimate.

    Parameters:
    estimate_name (str): The name of the estimate (e.g., 'Estimate 1').

    Returns:
    float: The corresponding EJ value.
    """
    try:
        # Filter the DataFrame to find the row corresponding to the estimate
        row = df[df['Estimations'] == estimate_name]
        if not row.empty:
            return row['EJ'].values[0]  # Return the EJ value
        else:
            return f"{estimate_name} not found in the data."
    except Exception as e:
        return f"An error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Load the DataFrame
    print("Available estimates:", df['Estimations'].tolist())

    # Example: Get the EJ value for 'Estimate 1'
    estimate_name = 'Estimate 1'
    ej_value = get_ej_value(estimate_name)
    print(f"The EJ value for {estimate_name} is: {ej_value}")
