import unittest
import numpy as np
from pathlib import Path
from petrocast.models.laherrere_model import laherrere_bell_curve
from petrocast.models.hubbert_curve_model import hubbert_curve
from petrocast.visualization import plot_results


class TestPlotResults(unittest.TestCase):
    def setUp(self):
        self.data = {
            'years': np.array([2000, 2001, 2002]),
            'production': np.array([100, 110, 120]),
            'future_years': np.array([2003, 2004, 2005])
        }
        self.laherrere_params = {
            'peak_production': 150,
            'tm': 2003,
            'c': 0.5
        }
        self.hubbert_params = {
            'urr': 1000,
            'steepness': 0.15,
            'peak_time': 2003
        }
        self.urr = 1000
        self.output_path = Path("test_output")
        if not self.output_path.exists():
            self.output_path.mkdir()

    def test_plot_creation(self):
        plot_results(self.data, self.laherrere_params, self.hubbert_params,
                     self.urr, self.output_path)

        # Check if file was created
        self.assertTrue((self.output_path / "results.png").exists())

        # Check file size is non-zero
        self.assertGreater((self.output_path / "results.png").stat().st_size, 0)

    def tearDown(self):
        # Clean up test files
        if (self.output_path / "results.png").exists():
            (self.output_path / "results.png").unlink()
    #    if self.output_path.exists():
    #        self.output_path.rmdir()


if __name__ == '__main__':
    unittest.main()