"""
Unit tests for the calculate_cumulative_production function.

This script tests the correctness and robustness of the calculate_cumulative_production
function using a dummy model for predictions.
"""

import unittest
import numpy as np
from petrocast.utils.cumulative_production import calculate_cumulative_production


def dummy_model_func(future_years, param1, param2, param3):
    """
    A dummy model function replicating a simplified model for testing.

    Parameters:
    - future_years (array-like): Array of future years.
    - param1, param2, param3: Dummy parameters.

    Returns:
    - array-like: Predicted future production values.
    """
    return param1 * np.exp(-param2 * (future_years - param3))


class TestCumulativeProduction(unittest.TestCase):
    """
    Test suite for the calculate_cumulative_production function.
    """

    def setUp(self):
        """
        Set up test data and parameters for the tests.
        """
        # Historical data
        self.years = np.array([2000, 2001, 2002, 2003, 2004, 2005])
        self.production = np.array([50, 55, 60, 65, 70, 75])

        # Model parameters for the dummy model
        self.model_params = {'param1': 100, 'param2': 0.01, 'param3': 2050}
        self.model_func = dummy_model_func

    def test_calculate_cumulative_production(self):
        """
        Test the calculation of cumulative production.
        """
        # Calculate cumulative production using the dummy model
        total_cumulative = calculate_cumulative_production(
            self.years, self.production, self.model_params, self.model_func
        )

        # Verify types
        self.assertIsInstance(total_cumulative, float)

        # Calculate expected cumulative production manually
        future_years = np.arange(self.years[-1] + 1, 2101)
        projected_production = self.model_func(future_years, *self.model_params.values())
        expected_cumulative = self.production.sum() + projected_production.sum()

        # Verify the calculated cumulative production
        self.assertAlmostEqual(total_cumulative, expected_cumulative, places=2)

    def test_invalid_years_type(self):
        """
        Test invalid input for the years parameter.
        """
        with self.assertRaises(TypeError):
            calculate_cumulative_production('invalid_type', self.production,
                                            self.model_params, self.model_func)

    def test_invalid_production_type(self):
        """
        Test invalid input for the production parameter.
        """
        with self.assertRaises(TypeError):
            calculate_cumulative_production(self.years, 'invalid_type',
                                            self.model_params, self.model_func)

    def test_invalid_model_params_type(self):
        """
        Test invalid input for the model_params parameter.
        """
        with self.assertRaises(TypeError):
            calculate_cumulative_production(self.years, self.production,
                                            'invalid_type', self.model_func)

    def test_invalid_model_func_type(self):
        """
        Test invalid input for the model_func parameter.
        """
        with self.assertRaises(TypeError):
            calculate_cumulative_production(self.years, self.production,
                                            self.model_params, 'invalid_type')


if __name__ == '__main__':
    unittest.main()
