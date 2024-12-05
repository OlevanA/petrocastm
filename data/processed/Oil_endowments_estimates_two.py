import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\oleva\PycharmProjects\PetroCast\data\raw\sorted_oil_endowments_with_estimations.csv'  # Replace with the correct path if needed
df = pd.read_csv(file_path)


# Function to get the value for a specific estimate and unit
def get_estimate_value(estimate_name, unit):
    """
    Get the value for a given estimate and unit (Gb or EJ).

    Parameters:
    estimate_name (str): The name of the estimate (e.g., 'Estimate 1').
    unit (str): The unit to retrieve ('Gb' or 'EJ').

    Returns:
    float: The corresponding value in the specified unit.
    """
    try:
        # Validate the unit
        if unit not in ['Gb', 'EJ']:
            return f"Invalid unit. Please choose 'Gb' or 'EJ'."

        # Filter the DataFrame to find the row corresponding to the estimate
        row = df[df['Estimations'] == estimate_name]
        if not row.empty:
            return row[unit].values[0]  # Return the value in the specified unit
        else:
            return f"{estimate_name} not found in the data."
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    # Print the entire DataFrame
    print("Oil Endowments Data:\n")
    print(df)

    # User interaction to select an estimate and unit
    while True:
        print("\nAvailable estimates:", df['Estimations'].tolist())
        estimate_name = input("Enter the estimate name (e.g., 'Estimate 1'): ").strip()
        unit = input("Enter the unit you want ('Gb' or 'EJ'): ").strip()

        # Get the value based on user input
        value = get_estimate_value(estimate_name, unit)
        print(f"The value for {estimate_name} in {unit} is: {value}")

        # Ask if the user wants to check another estimate
        another = input("Do you want to check another estimate? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting the program.")
            break
