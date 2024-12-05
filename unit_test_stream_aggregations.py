import unittest
import pandas as pd
import numpy as np
from stream_aggregations import StreamAggregationsScratch  # Import the class from stream_aggregations.py

class TestStreamAggregationsScratch(unittest.TestCase):
    
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
    
    def test_stream_group_count(self):
        result = StreamAggregationsScratch.stream_group_count(self.df, ['store'], 'sales')
        print("Result for stream_group_count:\n", result)  # Print result for debugging
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)

    def test_stream_group_first_last(self):
        result = StreamAggregationsScratch.stream_group_first_last(self.df, ['store'], 'sales')
        print("Result for stream_group_first_last:\n", result)  # Print result for debugging
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)

    def test_stream_group_mean_median(self):
        result = StreamAggregationsScratch.stream_group_mean_median(self.df, ['store'], 'sales')
        print("Result for stream_group_mean_median:\n", result)  # Print result for debugging
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_min_max(self):
        result = StreamAggregationsScratch.stream_group_min_max(self.df, ['store'], 'sales')
        print("Result for stream_group_min_max:\n", result)  # Print result for debugging
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_std_var(self):
        result = StreamAggregationsScratch.stream_group_std_var(self.df, ['store'], 'sales')
        print("Result for stream_group_std_var:\n", result)  # Print result for debugging
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_mad(self):
        result = StreamAggregationsScratch.stream_group_mad(self.df, ['store'], 'sales')
        print("Result for stream_group_mad:\n", result)  # Print result for debugging
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_prod(self):
        result = StreamAggregationsScratch.stream_group_prod(self.df, ['store'], 'sales')
        print("Result for stream_group_prod:\n", result)  # Print result for debugging
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)
    
    def test_stream_group_sum(self):
        result = StreamAggregationsScratch.stream_group_sum(self.df, ['store'], 'sales')
        print("Result for stream_group_sum:\n", result)  # Print result for debugging
        self.assertEqual(result.shape[0], 3)  # Should return 3 groups (for 3 stores)

    
    # --- Invalid Inputs ---
    
    def test_invalid_group_by_column(self):
        # Invalid column name that doesn't exist in the dataframe
        with self.assertRaises(KeyError):
            StreamAggregationsScratch.stream_group_count(self.df, ['invalid_column'], 'sales')
    
    def test_invalid_value_column(self):
        # Invalid column for aggregation
        with self.assertRaises(KeyError):
            StreamAggregationsScratch.stream_group_count(self.df, ['store'], 'invalid_column')
    
    def test_invalid_data_type_for_aggregation(self):
        # Providing a non-numeric column for an aggregation that requires numeric data
        self.df['store'] = self.df['store'].astype(str)  # Changing 'store' to non-numeric type
        with self.assertRaises(TypeError):
            StreamAggregationsScratch.stream_group_sum(self.df, ['store'], 'store')  # 'store' is non-numeric now

    def test_empty_dataframe(self):
        # Test with an empty dataframe
        empty_df = pd.DataFrame(columns=['store', 'region', 'sales', 'date'])
        result = StreamAggregationsScratch.stream_group_count(empty_df, ['store'], 'sales')
        self.assertEqual(result.shape[0], 0)  # Should return an empty DataFrame since there's no data
    
    def test_nan_in_group_by_column(self):
        # NaN values in the 'store' column
        self.df.loc[0, 'store'] = np.nan
        result = StreamAggregationsScratch.stream_group_count(self.df, ['store'], 'sales')
        # Ensure the result doesn't contain NaN values in the 'store' column after grouping
        self.assertTrue(result['store'].isnull().sum() == 0)  # No NaN values in the result after grouping

    def test_nan_in_value_column(self):
        # NaN values in the 'sales' column
        self.df.loc[0, 'sales'] = np.nan
        result = StreamAggregationsScratch.stream_group_sum(self.df, ['store'], 'sales')
        # Ensure NaN values in the 'sales' column are handled (sum should ignore NaNs)
        self.assertTrue(result.isnull().sum().sum() == 0)  # No NaN values in the sum after grouping
    
    def test_invalid_column_type_for_grouping(self):
        # Attempting to group by a non-numeric or string column in a function that requires it (if applicable)
        self.df['region'] = self.df['region'].astype(float)  # Alter the 'region' column to float type
        with self.assertRaises(TypeError):
            StreamAggregationsScratch.stream_group_sum(self.df, ['region'], 'sales')  # Trying to group by a non-numeric column

def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)

if __name__ == "__main__":
    main()
