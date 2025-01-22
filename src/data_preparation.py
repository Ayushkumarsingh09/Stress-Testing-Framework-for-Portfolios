import pandas as pd

class DataPreparation:
    @staticmethod
    def load_data(file_path):
        """
        Load data from a CSV file.
        """
        return pd.read_csv(file_path)

    @staticmethod
    def clean_data(data):
        """
        Perform basic data cleaning.
        """
        data = data.dropna()
        data = data[data.select_dtypes(include=['number']).ge(0).all(1)]
        return data

    @staticmethod
    def preprocess_data(data):
        """
        Additional preprocessing if needed.
        """
        data = data.reset_index(drop=True)
        return data
