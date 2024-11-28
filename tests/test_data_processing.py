import unittest
import pandas as pd
import numpy as np
import os
from PetroCast.utils.data_processing import load_data


class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        # Create a temporary CSV file with sample data for testing
        self.test_csv = 'temp_test_data.csv'
        data = {
            'Year': [2000, 2001, 2002, 2003, 2004, 2005],
            'Production': [50, 55, 60, 65, 70, 75]
        }
        df = pd.DataFrame(data)
        df.to_csv(self.test_csv, index=False)

    def tearDown(self):
        # Remove the temporary CSV file after tests
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_load_data(self):
        # Test loading data from the CSV file
        years, production = load_data(self.test_csv)

        expected_years = np.array([2000, 2001, 2002, 2003, 2004, 2005])
        expected_production = np.array([50, 55, 60, 65, 70, 75])

        # Check if the loaded data matches the expected data
        np.testing.assert_array_equal(years, expected_years)
        np.testing.assert_array_equal(production, expected_production)


if __name__ == '__main__':
    unittest.main()
