"""
Unit tests for the curve_fitting_function.

This script tests the correctness and robustness of the curve_fitting
function using a dummy data for predictions.
"""



import unittest
import numpy as np
from petrocast.utils.curve_fitting import fit_hubbert_curve, fit_laherrere_model
from petrocast.models.hubbert_curve_model import hubbert_curve
from petrocast.models.laherrere_model import laherrere_bell_curve


class TestCurveFitting(unittest.TestCase):
    """Unit tests for curve fitting utilities."""

    def setUp(self):
        """
        Set up synthetic test data for curve fitting.
        """
        # Synthetic years and production data
        self.years = np.arange(2000, 2050, dtype=float)

        # Ensure the years array contains only numeric values
        assert np.issubdtype(self.years.dtype, np.number), "Years array contains non-numeric values"

        self.urr = 1000  # Ultimate recoverable resources
        self.steepness = 0.03
        self.peak_time = 2030

        # Generate synthetic Hubbert curve data
        self.hubbert_production = hubbert_curve(self.years, self.urr,
                                                self.steepness, self.peak_time)

        # Parameters for Laherrère model
        self.peak_production = 50
        self.tm = 2035
        self.c = 150

        # Generate synthetic Laherrère data
        self.laherrere_production = laherrere_bell_curve(self.years,
                                                         self.peak_production, self.tm, self.c)

    def test_fit_hubbert_curve(self):
        """Test Hubbert curve fitting using synthetic data."""
        fitted_params = fit_hubbert_curve(self.years, self.hubbert_production, self.urr)

        # Assert URR is correctly passed through
        self.assertAlmostEqual(fitted_params['urr'], self.urr, places=5)

        # Assert steepness is within 5% of the true value
        self.assertAlmostEqual(fitted_params['steepness'], self.steepness,
                               delta=0.05 * self.steepness)

        # Assert peak_time is within 1 year of the true value
        self.assertAlmostEqual(fitted_params['peak_time'], self.peak_time, delta=1)

    def test_fit_laherrere_model(self):
        """Test Laherrère model fitting using synthetic data."""
        fitted_params = fit_laherrere_model(self.years, self.laherrere_production, self.urr)

        # Assert peak_production is within 5% of the true value
        self.assertAlmostEqual(
            fitted_params['peak_production'], self.peak_production,
            delta=0.05 * self.peak_production
        )

        # Assert tm (peak year) is within 1 year of the true value
        self.assertAlmostEqual(fitted_params['tm'], self.tm, delta=1)

        # Assert c (width parameter) is within 10% of the true value
        self.assertAlmostEqual(fitted_params['c'], self.c, delta=0.1 * self.c)

    def test_invalid_inputs(self):
        """Test that invalid inputs raise appropriate exceptions."""
        # Test invalid type for 'years'
        with self.assertRaises(TypeError):
            fit_laherrere_model("invalid_years", self.laherrere_production, self.urr)

        # Test invalid type for 'production'
        with self.assertRaises(TypeError):
            fit_laherrere_model(self.years, "invalid_production", self.urr)

        # Test non-numeric values in 'production'
        with self.assertRaises(TypeError):
            fit_laherrere_model(self.years, ["invalid", 100], self.urr)

        # Test mismatched input lengths
        with self.assertRaises(ValueError):
            fit_laherrere_model(self.years, self.laherrere_production[:-1], self.urr)


if __name__ == '__main__':
    unittest.main()
