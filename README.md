#PetroCast: A Scientific Tool for Oil Resource Modeling and Forecasting

PetroCast is a Python-based scientific modeling package designed to compare the accuracy 
and forecasting power of different resource extraction models used by the scientific community, 
with an initial focus on oil production. This tool helps researchers analyze historical trends, 
predict future extraction rates, and evaluate model performance under shared assumptions, 
such as a common Ultimate Recoverable Resource (URR) value.

In future versions, additional models and resource types (e.g., natural gas, coal, copper etc...) 
will be added, making PetroCast a versatile tool for resource modeling and forecasting.
------------------------------------------------------------------------------------------------------------------
Key Features: 

    Current Models Included 
        Hubbert Model: Symmetric production curve for peak oil analysis.
        Laherrère Model: Flexible asymmetric production curve, tailored for resource extraction modeling.
    Comparative Analysis: 
        Compare model accuracy for historical data.
        Evaluate model predictions for future production under identical URR assumptions.
    Cumulative Production Analysis:
        Calculate cumulative production based on historical data and model forecasts.
        Convert production units (e.g., from Exajoules to Giga barrels).
    Visualization:
        Generate clear, annotated plots showing historical data, model fits, and future projections.
    Extensibility:
        Easily integrate additional models or resources in future iterations.
--------------------------------------------------------------------------------------------------------------------
Installation:
---------------------------------------------------------------------------------------------------------------------
Prerequisites: 

    Python >= 3.8
    Required Python packages: 
    numpy
    matplotlib 
    scipy
    pylint

Installation Instructions 

Clone the repository and install the dependencies: 

git clone https://github.com/OlevanA/PetroCast.git
cd PetroCast
pip install -r requirements.txt

Run the code as a module
python -m PetroCast
---------------------------------------------------------------------------------------------------------------------
