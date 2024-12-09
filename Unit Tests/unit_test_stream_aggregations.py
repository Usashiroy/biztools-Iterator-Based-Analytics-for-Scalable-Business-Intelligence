import sys
import os
current_directory = os.getcwd()
main_directory_path = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, main_directory_path)

import unittest
import pandas as pd
import numpy as np
from biztools.stream_aggregations import StreamAggregations  # Import the class from stream_aggregations.py

class TestStreamAggregations(unittest.TestCase):
    
    def setUp(self):
        # Sample data setup (from the realistic dataset)
        np.random.seed(42)
        data = {
            'store': np.random.choice(['Store A', 'Store B', 'Store C'], size=100),
            'region': np.random.choice(['North', 'South', 'East', 'West'], size=100),
            'sales': np.random.uniform(1000, 5000, size=100),
            'date': pd.date_range('2023-01-01', periods=100, freq='D')
        }
        self.df = pd.DataFrame(data)
        
        # Introducing NaN values in the 'sales' column (10 random NaN values)
        nan_indices = np.random.choice(self.df.index, size=10, replace=False)
        self.df.loc[nan_indices, 'sales'] = np.nan  

    # ==========================
    # Valid input tests
    # ==========================
 
    def test_stream_group_count(self):
        result = StreamAggregations.stream_group_count(self.df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)

    def test_stream_group_first_last(self):
        result = StreamAggregations.stream_group_first_last(self.df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)

    def test_stream_group_mean_median(self):
        result = StreamAggregations.stream_group_mean_median(self.df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_min_max(self):
        result = StreamAggregations.stream_group_min_max(self.df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_std_var(self):
        result = StreamAggregations.stream_group_std_var(self.df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_mad(self):
        result = StreamAggregations.stream_group_mad(self.df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_prod(self):
        result = StreamAggregations.stream_group_prod(self.df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_sum(self):
        result = StreamAggregations.stream_group_sum(self.df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    # ==========================
    # Invalid input tests
    # ==========================
    
    def test_invalid_group_by_column(self):
        # Invalid column name that doesn't exist in the dataframe
        with self.assertRaises(KeyError):
            StreamAggregations.stream_group_count(self.df, ['invalid_column'], 'sales')
    
    def test_invalid_value_column(self):
        with self.assertRaises(ValueError) as context:
            StreamAggregations.stream_group_count(self.df, ['store'], 'invalid_column')

        self.assertEqual(str(context.exception), "Column 'invalid_column' not found in Data.")
    
    def test_invalid_data_type_for_aggregation(self):
        self.df['store'] = self.df['store']

        with self.assertRaises(ValueError) as context:
            StreamAggregations.stream_group_sum(self.df, ['store'], 'store')  # 'store' is non-numeric now

        self.assertEqual(str(context.exception), "The value column 'store' must contain numeric data.")

    def test_empty_dataframe(self):
        # Test with an empty dataframe
        empty_df = pd.DataFrame(columns=['store', 'region', 'sales', 'date'])
        result = StreamAggregations.stream_group_count(empty_df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 0)  # Should return an empty DataFrame since there's no data
    
    def test_nan_in_group_by_column(self):
        # NaN values in the 'store' column
        self.df.loc[0, 'store'] = np.nan
        result = StreamAggregations.stream_group_count(self.df, ['store'], 'sales')
        # Ensure the result doesn't contain NaN values in the 'store' column after grouping
        self.assertTrue(result['store'].isnull().sum() == 0)  # No NaN values in the result after grouping

    def test_nan_in_value_column(self):
        # NaN values in the 'sales' column
        self.df.loc[0, 'sales'] = np.nan
        result = StreamAggregations.stream_group_sum(self.df, ['store'], 'sales')
        # Ensure NaN values in the 'sales' column are handled (sum should ignore NaNs)
        self.assertTrue(result.isnull().sum().sum() == 0)  # No NaN values in the sum after grouping
    

def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)

if __name__ == "__main__":
    main()
