"""
Unit tests for the Laherrère bell curve model.
"""

import unittest
import numpy as np
from petrocast.models.laherrere_model import laherrere_bell_curve


class TestLaherrereBellCurve(unittest.TestCase):
    """
    Unit tests for validating the Laherrère bell curve model.
    """

    def test_bell_curve_scalar(self):
        """
        Test the Laherrère bell curve for a scalar input.
        """
        t = 10
        peak_production = 100
        tm = 8
        c = 1.5
        expected_output = 2 * peak_production / (1 + np.cosh(-5 / c * (t - tm)))
        result = laherrere_bell_curve(t, peak_production, tm, c)
        self.assertAlmostEqual(result, expected_output)

    def test_bell_curve_array(self):
        """
        Test the Laherrère bell curve for an array input.
        """
        t = np.array([5, 10, 15])
        peak_production = 100
        tm = 8
        c = 1.5
        expected_output = 2 * peak_production / (1 + np.cosh(-5 / c * (t - tm)))
        result = laherrere_bell_curve(t, peak_production, tm, c)
        np.testing.assert_almost_equal(result, expected_output)

    def test_invalid_type_t(self):
        """
        Test that invalid input type for 't' raises a TypeError.
        """
        with self.assertRaises(TypeError):
            laherrere_bell_curve('invalid', 100, 8, 1.5)

    def test_invalid_type_peak_production(self):
        """
        Test that invalid input type for 'peak_production' raises a TypeError.
        """
        with self.assertRaises(TypeError):
            laherrere_bell_curve(10, 'invalid', 8, 1.5)

    def test_invalid_type_tm(self):
        """
        Test that invalid input type for 'tm' raises a TypeError.
        """
        with self.assertRaises(TypeError):
            laherrere_bell_curve(10, 100, 'invalid', 1.5)

    def test_invalid_type_c(self):
        """
        Test that invalid input type for 'c' raises a TypeError.
        """
        with self.assertRaises(TypeError):
            laherrere_bell_curve(10, 100, 8, 'invalid')

    def test_invalid_type_urr(self):
        """
        Test that invalid input type for 'URR' raises a TypeError.
        """
        with self.assertRaises(TypeError):
            laherrere_bell_curve(10, 100, 8, 1.5, 'invalid')


if __name__ == '__main__':
    unittest.main()
