"""
Unit tests for the visualization module in PetroCast.

This script tests the functionality of the `plot_results` function, ensuring that it correctly
creates a plot and saves it as an image file.
"""

import unittest
from pathlib import Path
import numpy as np
from petrocast.visualization import plot_results


class TestPlotResults(unittest.TestCase):
    """Unit tests for verifying that the `plot_results`
    function generates and saves plots correctly."""

    def setUp(self):
        """Set up synthetic test data and output directory."""
        self.data = {
            "years": np.array([2000, 2001, 2002]),
            "production": np.array([100, 110, 120]),
            "future_years": np.array([2003, 2004, 2005]),
            "tm": 2050,
            "peak_time": 2030,
            "urr_key": "example_key"  #
        }
        self.laherrere_full = np.array([2000, 2001, 2002, 2003, 2004, 2005])
        self.hubbert_full = np.array([2000, 2001, 2002, 2003, 2004, 2005])

        self.output_path = Path("test_output")
        self.output_path.mkdir(exist_ok=True)

        #  Initialize `generated_file` to `None`
        self.generated_file = None

    def test_plot_creation(self):
        """Test that the `plot_results` function successfully generates a plot file."""
        plot_results(
            data=self.data,
            laherre_full=self.laherrere_full,
            hubbert_full=self.hubbert_full,
            output_path=self.output_path,
        )

        # Dynamically find the generated file using glob pattern
        matching_files = list(self.output_path.glob(f"results_{self.data['urr_key']}_*.png"))

        # Ensure a file was created
        self.assertTrue(matching_files, "No plot file was created.")

        # Get the first matching file
        output_file = matching_files[0]

        # Check if the file size is non-zero
        self.assertGreater(
            output_file.stat().st_size, 0, "Plot file is empty."
        )

        # Store the filename for cleanup in tearDown
        self.generated_file = output_file

    def tearDown(self):
        """Clean up generated test files after execution."""
        if hasattr(self, "generated_file") and self.generated_file.exists():
            self.generated_file.unlink()

        # Remove directory only if empty
        if not any(self.output_path.iterdir()):
            self.output_path.rmdir()


if __name__ == "__main__":
    unittest.main()
