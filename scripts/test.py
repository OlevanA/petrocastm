import unittest
import numpy as np
import matplotlib.pyplot as plt
from PetroCast.models.hubbert_curve_model import hubbert_curve

class TestHubbertCurve(unittest.TestCase):
    def test_hubbert_curve_valid_input(self):
        """
        Test the hubbert_curve function with valid input and plot the results.
        """
        # Input data
        time = np.arange(1990, 2011)  # Years from 1990 to 2010
        urr = 100.0
        steepness = 0.1
        peak_time = 2000.0

        # Expected output
        result = hubbert_curve(time, urr, steepness, peak_time)

        # Plotting the result
        plt.figure(figsize=(10, 6))
        plt.plot(time, result, label="Hubbert Curve", color="blue", marker="o")
        plt.title("Hubbert Curve - Annual Production")
        plt.xlabel("Year")
        plt.ylabel("Production (EJ/year)")
        plt.legend()
        plt.grid(True)
        plt.savefig("hubbert_curve_test_output.png")  # Save graph to file
        plt.show()

        # Assert that the result is not empty
        self.assertTrue(len(result) > 0)

    def test_hubbert_curve_empty_time_array(self):
        """
        Test the hubbert_curve function with an empty numpy array for time.
        """
        time = np.array([])  # Empty array
        urr = 100.0
        steepness = 0.1
        peak_time = 2000.0

        result = hubbert_curve(time, urr, steepness, peak_time)

        # Assert that the result is also an empty array
        self.assertTrue(result.size == 0)


if __name__ == "__main__":
    unittest.main()
