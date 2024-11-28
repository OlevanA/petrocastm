import unittest
import numpy as np
from PetroCast.utils.curve_fitting import fit_hubbert_curve, fit_laherrere_model


class TestCurveFitting(unittest.TestCase):

    def setUp(self):
        # Historical production data (years and production values)
        self.years = np.array([2000, 2001, 2002, 2003, 2004, 2005])
        self.production = np.array([50, 55, 60, 65, 70, 75])

        # Setting the Ultimate Recoverable Resources (URR)
        self.ultimate_recoverable_resources = 1000.0

    def test_fit_hubbert_curve(self):
        # Fit the Hubbert curve using provided data
        params = fit_hubbert_curve(self.years, self.production, self.ultimate_recoverable_resources)

        # Check if the parameters returned are as expected
        self.assertIn('urr', params)
        self.assertIn('steepness', params)
        self.assertIn('peak_time', params)

        # Make generic assumptions about fitted parameters
        self.assertAlmostEqual(params['urr'], self.ultimate_recoverable_resources, places=2)
        self.assertTrue(0.01 <= params['steepness'] <= 0.05)
        self.assertTrue(2030 <= params['peak_time'] <= 2040)

    def test_fit_laherrere_model(self):
        # Fit the Laherrère bell curve using provided data
        params = fit_laherrere_model(self.years, self.production, self.ultimate_recoverable_resources)

        # Check if the parameters returned are as expected
        self.assertIn('peak_production', params)
        self.assertIn('tm', params)
        self.assertIn('c', params)

        # Make generic assumptions about fitted parameters
        self.assertAlmostEqual(params['peak_production'], max(self.production), delta=10)
        self.assertTrue(2030 <= params['tm'] <= 2040)
        self.assertTrue(10 <= params['c'] <= 300)


if __name__ == '__main__':
    unittest.main()
