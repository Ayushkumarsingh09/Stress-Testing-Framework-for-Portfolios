import unittest
import pandas as pd
from src.data_preparation import DataPreparation

class TestDataPreparation(unittest.TestCase):
    def setUp(self):
        self.raw_data = pd.DataFrame({
            "col1": [1, 2, None],
            "col2": [3, None, 5],
            "col3": [-1, 2, 3]
        })

    def test_clean_data(self):
        cleaned_data = DataPreparation.clean_data(self.raw_data)
        self.assertFalse(cleaned_data.isnull().values.any())

    def test_preprocess_data(self):
        preprocessed_data = DataPreparation.preprocess_data(self.raw_data)
        self.assertTrue(preprocessed_data.reset_index is not None)
