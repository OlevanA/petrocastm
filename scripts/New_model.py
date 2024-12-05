import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# --- MODEL FUNCTIONS ---
def cumulative_production(t, K, Q0, t0, tau):
    """Logistic growth equation for cumulative production Q(t)."""
    t_norm = (t - t0) / tau
    exp_term = np.exp(-t_norm)
    return K / (1 + ((K / Q0) - 1) * exp_term)


def annual_production(t, K, Q0, t0, tau):
    """Calculate annual production P(t) as the derivative of Q(t)."""
    Q_t = cumulative_production(t, K, Q0, t0, tau)
    dQ_dt = np.gradient(Q_t, t)
    return dQ_dt


def remaining_resources(t, K, Q0, t0, tau):
    """Calculate remaining resources R(t) as K - Q(t)."""
    Q_t = cumulative_production(t, K, Q0, t0, tau)
    return K - Q_t


def peak_production(K, Q0, t0, tau):
    """Calculate the peak production value and its timing."""
    if K <= 2 * Q0:
        print("Warning: K must be greater than 2 * Q0 for valid peak production.")
        return t0, 0
    t_peak = t0 + tau * np.log((K - 2 * Q0) / (2 * Q0))
    P_peak = K / (4 * tau)
    return t_peak, P_peak


def goodness_of_fit(actual, modeled):
    """Calculate the R² goodness-of-fit metric."""
    residual_sum_of_squares = np.sum((actual - modeled) ** 2)
    total_sum_of_squares = np.sum((actual - np.mean(actual)) ** 2)
    return 1 - (residual_sum_of_squares / total_sum_of_squares)


# --- CURVE FITTING ---
def fit_model(time_data, production_data, initial_params):
    """Fit the logistic growth model to historical production data."""

    def fitting_function(t, K, Q0, t0, tau):
        return cumulative_production(t, K, Q0, t0, tau)

    # Bounds for parameters
    bounds_lower = [initial_params["Q0"], initial_params["Q0"] * 0.8, min(time_data), 5]
    bounds_upper = [initial_params["Q0"] * 1.5, initial_params["Q0"] * 1.2, max(time_data), 30]

    params, _ = curve_fit(
        fitting_function,
        time_data,
        production_data,
        p0=[initial_params["K"], initial_params["Q0"], initial_params["t0"], initial_params["tau"]],
        bounds=(bounds_lower, bounds_upper)
    )
    return params


# --- VISUALIZATION ---
def plot_results(time_data, production_data, params):
    """Plot historical data, modeled production, cumulative production, and remaining resources."""
    K, Q0, t0, tau = params
    t = np.linspace(min(time_data), max(time_data) + 50, 500)

    Q_t = cumulative_production(t, K, Q0, t0, tau)
    P_t = annual_production(t, K, Q0, t0, tau)
    R_t = remaining_resources(t, K, Q0, t0, tau)

    t_peak, _ = peak_production(K, Q0, t0, tau)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Primary y-axis: Annual production
    ax1.plot(time_data, production_data, 'o', label="Historical Data (P(t))", color="blue")
    ax1.plot(t, P_t, label="Modeled Annual Production (P(t))", color="orange")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Annual Production (P(t))", color="orange")
    ax1.tick_params(axis='y', labelcolor="orange")
    ax1.axvline(x=t_peak, linestyle='--', color='gray', label=f"Peak Year (t_peak)")
    ax1.legend(loc="upper left")

    # Secondary y-axis: Cumulative production and remaining resources
    ax2 = ax1.twinx()
    ax2.plot(t, Q_t, label="Cumulative Production (Q(t))", color="green")
    ax2.plot(t, R_t, label="Remaining Resources (R(t))", color="red")
    ax2.set_ylabel("Cumulative / Remaining Resources (EJ)", color="green")
    ax2.tick_params(axis='y', labelcolor="green")
    ax2.set_ylim(0, 50)  # Scaled data: adjust as necessary
    ax2.legend(loc="upper right")

    # Title and grid
    fig.suptitle("Hubbert Model Production and Resource Dynamics")
    fig.tight_layout()
    plt.grid()
    plt.show()


# --- DATA LOADING ---
def load_historical_data(filepath, custom_K=None):
    """Load historical production data from a CSV file and calculate reference year (t0) and Q0."""
    # Load the data
    data = pd.read_csv(filepath)

    # Ensure the data contains the required columns
    if 'Year' not in data.columns or 'Production' not in data.columns:
        raise ValueError("The CSV file must contain 'Year' and 'Production' columns.")

    # Sort the data by year
    data = data.sort_values(by='Year')

    # Calculate cumulative production
    data['cumulative_production'] = data['Production'].cumsum()

    # Extract the last year as t0 and total cumulative production as Q0
    t0 = data['Year'].iloc[-1]  # Last year in the dataset
    Q0 = data['Production'].sum()  # Total cumulative production (sum of all data points)

    # Normalize production data for numerical stability
    data['Production'] /= 1000
    data['cumulative_production'] /= 1000
    Q0 /= 1000

    # Set initial guesses for K and tau
    K_guess = custom_K if custom_K else Q0 * 1.2  # Allow user-defined K or default to 1.2 * Q0
    tau_guess = 15  # Example characteristic time in years

    initial_params = {"K": K_guess, "Q0": Q0, "t0": t0, "tau": tau_guess}
    return data, initial_params


# --- MAIN SCRIPT ---
if __name__ == "__main__":
    filepath = r"C:\Users\oleva\PycharmProjects\PetroCast\data\raw\data1_oil_his_havard.csv"
    custom_K = None  # Let the script calculate K dynamically

    try:
        # Load data and initial parameters
        historical_data, initial_params = load_historical_data(filepath, custom_K=custom_K)

        print(f"Initial Parameters: {initial_params}")
        print(f"Loaded Data:\n{historical_data.head()}")

        time_data = historical_data['Year'].values
        production_data = historical_data['Production'].values

        # Fit the model
        fitted_params = fit_model(time_data, production_data, initial_params)
        K, Q0, t0, tau = fitted_params
        print(f"Fitted Parameters: K={K:.2f}, Q0={Q0:.2f}, t0={t0:.2f}, tau={tau:.2f}")

        # Calculate peak production
        t_peak, P_peak = peak_production(K, Q0, t0, tau)
        print(f"Peak Production: P_peak={P_peak:.2f}, Year={t_peak:.2f}")

        # Evaluate goodness-of-fit
        modeled_production = annual_production(time_data, K, Q0, t0, tau)
        r_squared = goodness_of_fit(production_data, modeled_production)
        print(f"Goodness of Fit (R²): {r_squared:.4f}")

        # Plot the residuals
        residuals = production_data - modeled_production
        plt.plot(time_data, residuals, 'o')
        plt.axhline(y=0, color='r', linestyle='--')
        plt.title("Residuals")
        plt.xlabel("Year")
        plt.ylabel("Residual (Actual - Modeled)")
        plt.show()

        # Plot the results
        plot_results(time_data, production_data, fitted_params)

    except Exception as e:
        print(f"An error occurred: {e}")
