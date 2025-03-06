"""
Unit tests for the Hubbert curve model.
This script verifies the correctness of the Hubbert curve implementation
by testing various scenarios with both valid and invalid inputs.
"""

import unittest
import numpy as np
from petrocast.models.hubbert_curve_model import hubbert_curve


class TestHubbertCurve(unittest.TestCase):
    """
    Test cases for the Hubbert curve model.
    """

    def test_hubbert_curve_array(self):
        """
        Test the Hubbert curve calculation with an array of time values.
        """
        time = np.array([2000, 2010, 2020])
        urr = 1000
        steepness = 0.1
        peak_time = 2010
        exponential_term = np.exp(-steepness * (time - peak_time))
        expected_output = (urr * steepness * exponential_term) / ((1 + exponential_term) ** 2)
        result = hubbert_curve(time, urr, steepness, peak_time)
        np.testing.assert_almost_equal(result, expected_output)

    def test_hubbert_curve_single_year(self):
        """
        Test the Hubbert curve calculation for a single year.
        """
        time = np.array([2010])
        urr = 1000
        steepness = 0.1
        peak_time = 2010
        exponential_term = np.exp(-steepness * (time - peak_time))
        expected_output = (urr * steepness * exponential_term) / ((1 + exponential_term) ** 2)
        result = hubbert_curve(time, urr, steepness, peak_time)
        np.testing.assert_almost_equal(result, expected_output)

    def test_invalid_type_time(self):
        """
        Test the Hubbert curve with an invalid time input (string instead of numeric).
        """
        with self.assertRaises(TypeError):
            hubbert_curve('invalid', 1000, 0.1, 2010)

    def test_invalid_type_urr(self):
        """
        Test the Hubbert curve with an invalid URR input (string instead of numeric).
        """
        time = np.array([2000, 2010, 2020])
        with self.assertRaises(TypeError):
            hubbert_curve(time, 'invalid', 0.1, 2010)

    def test_invalid_type_steepness(self):
        """
        Test the Hubbert curve with an invalid steepness input (string instead of numeric).
        """
        time = np.array([2000, 2010, 2020])
        with self.assertRaises(TypeError):
            hubbert_curve(time, 1000, 'invalid', 2010)

    def test_invalid_type_peak_time(self):
        """
        Test the Hubbert curve with an invalid peak time input (string instead of numeric).
        """
        time = np.array([2000, 2010, 2020])
        with self.assertRaises(TypeError):
            hubbert_curve(time, 1000, 0.1, 'invalid')


if __name__ == '__main__':
    unittest.main()
