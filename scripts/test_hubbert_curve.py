import unittest
import numpy as np
from PetroCast.models.hubbert_curve_model import hubbert_curve

class TestHubbertCurve(unittest.TestCase):
    def test_hubbert_curve_valid_input(self):
        """
        Test the hubbert_curve function with valid input.
        """
        time = np.array([2000, 2001, 2002, 2003, 2004])
        urr = 100.0
        steepness = 0.1
        peak_time = 2002.0

        # Expected results are approximate, depending on input parameters
        expected_output = np.array([1.664, 2.015, 2.5, 2.015, 1.664])
        result = hubbert_curve(time, urr, steepness, peak_time)

        # Assert that the result is close to the expected output
        np.testing.assert_almost_equal(result, expected_output, decimal=3)

    def test_hubbert_curve_invalid_time(self):
        """
        Test the hubbert_curve function with invalid time input (not a numpy array).
        """
        time = [2000, 2001, 2002, 2003, 2004]  # Invalid: list instead of np.ndarray
        urr = 100.0
        steepness = 0.1
        peak_time = 2002.0

        with self.assertRaises(TypeError):
            hubbert_curve(time, urr, steepness, peak_time)

    def test_hubbert_curve_invalid_parameters(self):
        """
        Test the hubbert_curve function with invalid parameter types.
        """
        time = np.array([2000, 2001, 2002, 2003, 2004])
        urr = "100"  # Invalid: string instead of float
        steepness = 0.1
        peak_time = 2002.0

        with self.assertRaises(TypeError):
            hubbert_curve(time, urr, steepness, peak_time)

    def test_hubbert_curve_empty_time_array(self):
        """
        Test the hubbert_curve function with an empty numpy array for time.
        """
        time = np.array([])  # Empty array
        urr = 100.0
        steepness = 0.1
        peak_time = 2002.0

        result = hubbert_curve(time, urr, steepness, peak_time)

        # Assert that the result is also an empty array
        self.assertTrue(result.size == 0)

if __name__ == "__main__":
    unittest.main()
