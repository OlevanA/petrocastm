import unittest
from unittest.mock import patch
import numpy as np

# Mock imports for laherrere_bell_curve and hubbert_curve
from PetroCast.models.laherrere_model import laherrere_bell_curve
from PetroCast.models.hubbert_curve_model import hubbert_curve


class TestPlotResults(unittest.TestCase):

    @patch('matplotlib.pyplot.show')
    @patch('PetroCast.models.hubbert_curve_model.hubbert_curve')
    @patch('PetroCast.models.laherrere_model.laherrere_bell_curve')
    def test_plot_results(self, mock_laherrere_bell_curve, mock_hubbert_curve, mock_show):
        # Setup test data
        data = {
            'years': np.array([2000, 2001, 2002]),
            'production': np.array([10, 15, 20]),
            'future_years': np.array([2003, 2004, 2005])
        }

        laherrere_params = {
            'peak_production': 25,
            'tm': 2002,
            'c': 1.5
        }

        hubbert_params = {
            'urr': 100,
            'steepness': 0.2,
            'peak_time': 2001
        }

        urr = 1000

        # Setup mock return values
        full_years = np.arange(data['years'][0], data['future_years'][-1] + 1)
        mock_laherrere_bell_curve.return_value = np.zeros_like(full_years)
        mock_hubbert_curve.return_value = np.zeros_like(full_years)

        # Call the function
        plot_results(data, laherrere_params, hubbert_params, urr)

        # Assertions to check function calls and parameters
        mock_laherrere_bell_curve.assert_called_once_with(full_years, peak_production=25, tm=2002, c=1.5, URR=urr)
        mock_hubbert_curve.assert_called_once_with(full_years, urr=100, steepness=0.2, peak_time=2001)
        mock_show.assert_called_once()


if __name__ == '__main__':
    unittest.main()
