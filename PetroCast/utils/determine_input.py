from pathlib import Path
import pandas as pd
import json

from data.output.Oil_estimate import saved_output

# Load the CSV file into a DataFrame
file_path = Path('data/raw/sorted_oil_endowments_with_estimations.csv')
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
            return f"Invalid unit. Please choose 'Gb' (gigabarrels) or 'EJ' (exajoules)."

        # Filter the DataFrame to find the row corresponding to the estimate
        row = df[df['Estimations'] == estimate_name]
        if not row.empty:
            return row[unit].values[0]  # Return the value in the specified unit
        else:
            return f"{estimate_name} not found in the data."
    except Exception as e:
        return f"An error occurred: {e}"


def determine_input():
    # Print the DataFrame
    print("Available estimates for Ultimate Recoverable Resources (URR):\n")
    print(df)

    saved_output = None  # Variable to store the selected estimate for future use
    saved_unit = None  # Variable to store the selected unit
    another_bool = True


    # User selects an estimate
    print("\nEnter the estimate name from the available list below or enter your own estimate in Gb or in EJ:")
    print(df['Estimations'].tolist())
    estimate_name = input("Enter the estimate name (e.g., 'Estimate 1'): ").strip()

    # User selects a unit
    unit = ('EJ')

    # Get the value for the selected estimate and unit
    if estimate_name[0:8] == "Estimate":
        value = get_estimate_value(estimate_name, unit)
    else:
        value = float(estimate_name)

    if isinstance(value, float):  # Valid estimate
        print(f"The value for {estimate_name} in {unit} is: {value}")
        saved_output = value  # Save the value for future use
        saved_unit = unit
        print(f"The value {value} has been saved as output for further processing.")
    else:  # Invalid estimate or unit
        print(value)

        # Ask if the user wants to check another estimate
        # another = input("\nDo you want to check another estimate? (yes/no): ").strip().lower()
        # if another != 'yes':
        #     another_bool = False
            # print("\nExiting the program.")
            # if saved_output is not None:
            #     print(f"Final saved output: {saved_output} ({saved_unit})")
            #
            #     # Save the output to a JSON file
            #     json_file_path = r'C:\Users\oleva\PycharmProjects\PetroCast\data\processed\Oil_estimate.json'
            #     with open(json_file_path, 'w') as json_file:
            #         json.dump({'estimate_name': estimate_name, 'unit': saved_unit, 'value': saved_output}, json_file)
            #     print(f"Output saved to {json_file_path}")
            #
            #     # Save the output to a CSV file
            #     csv_file_path = r'C:\Users\oleva\PycharmProjects\PetroCast\data\processed\Oil_estimate.csv'
            #     output_df = pd.DataFrame([{
            #         'estimate_name': estimate_name,
            #         'unit': saved_unit,
            #         'value': saved_output
            #     }])
            #     output_df.to_csv(csv_file_path, index=False)
            #     print(f"Output saved to {csv_file_path}")

    return saved_output, unit