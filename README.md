# PetroCast: A Scientific Tool for Oil and Resource Modeling and Forecasting

PetroCast is a Python-based scientific modeling package designed to compare the accuracy 
and forecasting power of different resource extraction models used by the scientific community, 
with an initial focus on oil production. This tool helps researchers analyze historical trends, 
project future extraction rates, and evaluate model performance under shared assumptions, 
such as a common Ultimate Recoverable Resource (URR) value. The model can be applied to other resources
by the user when the instruction for the set up are followed. 

In future versions, additional models and resource types as examples (e.g., natural gas, coal, copper etc...) 
will be added, making PetroCast a versatile tool for resource modeling and forecasting.
---------------------------------------------------------------------------------------------------------------------
## **Overview**:
---------------------------------------------------------------------------------------------------------------------
    Current Models Included 
        Hubbert Model: Symmetric production curve for peak oil analysis.
        Laherrère Model: Flexible asymmetric production curve, tailored for resource extraction modeling.
    Comparative Analysis: 
        Compare model accuracy for historical data.
        Evaluate model projections for future production under identical URR assumptions.
    Cumulative Production Analysis:
        Calculate cumulative production based on historical data and model forecasts.
        Convert production units (e.g., from Exajoules to Giga barrels).
    Visualization:
        Generate clear, annotated plots showing historical data, model fits, and future projections.
    Extensibility:
        Easily integrate additional models or resources in future iterations.
---------------------------------------------------------------------------------------------------------------------
## **Installation**:
---------------------------------------------------------------------------------------------------------------------
### **Prerequisites**
---------------------------------------------------------------------------------------------------------------------
- Python 3.8+
- Required dependencies: `numpy`, `pandas`, `matplotlib`, `scipy`, `tomli` , `pylint` , `pytest`
---------------------------------------------------------------------------------------------------------------------
### **Install PetroCast Locally**
---------------------------------------------------------------------------------------------------------------------
Clone the repository git clone https://github.com/OlevanA/petrocastm.git

Run the following command inside the project directory:
```sh
pip install -e .
```
To verify installation:
```sh
pip list | grep petrocast  # macOS/Linux
pip list | findstr petrocast  # Windows
```
---------------------------------------------------------------------------------------------------------------------
## **Usage**
---------------------------------------------------------------------------------------------------------------------
### **1️⃣ Prepare the Configuration File (`config.toml`)**
Create a `config.toml` file with the following structure:
```toml
dataset = "data/raw/data1_oil_his_havard.csv"
urr_file = "data/processed/Oil_estimate.csv"
unit = "EJ"
```
### ** Prepare the Configuration File**
If you want to use your one data, take a look at structure of the CSV. files stuff

---------------------------------------------------------------------------------------------------------------------
### **2️⃣ Running the Application**
---------------------------------------------------------------------------------------------------------------------
Example Execute the program using with default example:
```sh
petrocast
```

Example Execute the program using:
```sh
petrocast --config config.toml --urr-key "Estimate1" #Or Estimate2...Estimate11
```
Or manually via Python:
```sh
python -m petrocast --config config.toml --urr-key "Estimate1" #Or Estimate2...Estimate11
```

---
---------------------------------------------------------------------------------------------------------------------
## **Configuration Options**
---------------------------------------------------------------------------------------------------------------------
The user has the option to configure petrocast to run with the example data which is for historical oil production
in EJ or Gb and a data set for e Ultimate Recoverable Resources (URR) estimates 


- `dataset`: Path to the historical production dataset.
- `urr_file`: Path to the CSV file containing URR estimates.
- `output_path` Path to the visualisation of the model results 
- `unit`: Choose between **EJ (Exajoules)** or **Gb (Gigabarrels)**.

---------------------------------------------------------------------------------------------------------------------
## **Example Output**
```
---------------------------------------------------------------------------------------------------------------------

Using dataset: data/raw/data1_oil_his_havard.csv
The estimated Ultimate Recoverable Resources (URR) is 13,423.2 EJ (Key: Estimate 1)

Laherrère Model Parameters:
   - Peak Production Rate: 207.05 EJ/year
   - Peak Year: 2030
   - Curve Width (Steepness): 135.19

Hubbert Model Parameters:
   - Ultimate Recoverable Resources (URR): 13,423.2 EJ
   - Steepness: 0.0436
   - Peak Year: 2030
   
   Example figure is saved under examples output showing the curves from both models, 
   indicating the peak production year and the decline of production in the future.
```

---
---------------------------------------------------------------------------------------------------------------------
## **Development**
### **Run Tests**
```sh
pytest tests/
```
### **Build & Install Package**
```sh
pip install build
python -m build
```

---
---------------------------------------------------------------------------------------------------------------------
## **License**
This project is licensed under the MIT License. See `LICENSE` for details.
