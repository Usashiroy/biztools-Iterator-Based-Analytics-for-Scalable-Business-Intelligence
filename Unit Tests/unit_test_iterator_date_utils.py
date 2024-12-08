import sys
import os
current_directory = os.getcwd()
main_directory_path = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, main_directory_path)


import unittest
import pandas as pd
import numpy as np
from iterator_date_utils import IteratorDateUtils  # Import the IteratorDateUtils class

class TestIteratorDateUtils(unittest.TestCase):
    
    def setUp(self):
        # Sample data setup
        np.random.seed(42)
        date_range = pd.date_range('2024-12-01', periods=100, freq='D')
        data = {
            'store': np.random.choice(['Store A', 'Store B', 'Store C'], size=100),
            'delivery_start_date': date_range,
            'delivery_end_date': date_range + pd.to_timedelta(np.random.randint(1, 6, size=len(date_range)), unit='D')
        }
        self.df = pd.DataFrame(data)
        
    # ==========================
    # Valid input tests
    # ==========================
    
    def test_business_days_between_rows_true(self):
        # Test the case where business days between rows are calculated correctly
        result = IteratorDateUtils.business_days_between_rows(self.df, 'delivery_start_date', 'business_days_to_previous')
        
        # Check that the first row's value is NaN (since there is no previous row)
        self.assertTrue(pd.isna(result['business_days_to_previous'].iloc[0]))
        
        # Check if business days between other rows are calculated correctly
        for i in range(1, len(result)):
            self.assertIsInstance(result['business_days_to_previous'].iloc[i], (int, float))  # Should be integer
    
    def test_business_days_between_rows_first_row(self):
        # Test the case where the first row should return NaN, not None
        result = IteratorDateUtils.business_days_between_rows(self.df, 'delivery_start_date', 'business_days_to_previous')
        
        # The first row should have NaN since there is no previous row to calculate
        self.assertTrue(pd.isna(result['business_days_to_previous'].iloc[0]))

    def test_iter_next_working_day_true(self):
        # Test the case where next working day is calculated correctly
        result = IteratorDateUtils.iter_next_working_day(self.df, 'delivery_start_date', 'next_working_day')

        # Check if next working day is calculated correctly for each row
        for i in range(1, len(result)):
            next_working_day = result['next_working_day'].iloc[i]
            current_date = result['delivery_start_date'].iloc[i]
            
            # The next working day should be strictly greater than the current date
            self.assertTrue(next_working_day > current_date, f"Failed for row {i}: {next_working_day} <= {current_date}")

    def test_iter_business_days(self):
        # Test case where business days between two date columns are calculated correctly
        result = IteratorDateUtils.iter_business_days(self.df, 'delivery_start_date', 'delivery_end_date', 'business_days_between')

        # Check if business days between columns are calculated correctly
        for i in range(len(result)):
            start_date = result['delivery_start_date'].iloc[i]
            end_date = result['delivery_end_date'].iloc[i]
            business_days = result['business_days_between'].iloc[i]
            
            # Calculate the expected number of business days using pandas bdate_range
            expected_business_days = len(pd.bdate_range(start=start_date, end=end_date)) - 1

            # Assert the calculated business days matches the expected
            self.assertEqual(business_days, expected_business_days, f"Failed for row {i}: Expected {expected_business_days} but got {business_days}")

    def test_add_business_days(self):
        # Test case where business days are added correctly to the 'delivery_start_date'
        result = IteratorDateUtils.add_business_days(self.df, 'delivery_start_date', 3, 'new_delivery_date')

        # Check if the new column has the expected date values (adding 3 business days)
        for i in range(len(result)):
            original_date = result['delivery_start_date'].iloc[i]
            new_date = result['new_delivery_date'].iloc[i]
            
            # Ensure the new date is a business day and 3 days ahead
            expected_new_date = original_date + pd.tseries.offsets.BDay(3)
            self.assertEqual(new_date, expected_new_date, f"Failed for row {i}: Expected {expected_new_date} but got {new_date}")
    def test_subtract_business_days(self):
        # Test case where business days are subtracted correctly from the 'delivery_start_date'
        result = IteratorDateUtils.subtract_business_days(self.df, 'delivery_start_date', 3, 'new_delivery_date')

        # Check if the new column has the expected date values (subtracting 3 business days)
        for i in range(len(result)):
            original_date = result['delivery_start_date'].iloc[i]
            new_date = result['new_delivery_date'].iloc[i]
            
            # Ensure the new date is a business day and 3 days before
            expected_new_date = original_date - pd.tseries.offsets.BDay(3)
            self.assertEqual(new_date, expected_new_date, f"Failed for row {i}: Expected {expected_new_date} but got {new_date}")

    def test_is_business_day(self):
        # Test case where the business day flag is added correctly
        result = IteratorDateUtils.is_business_day(self.df, 'delivery_start_date', 'is_business_day')

        # Check if each date in 'delivery_start_date' column has the correct business day flag
        for i in range(len(result)):
            date = result['delivery_start_date'].iloc[i]
            is_business_day = result['is_business_day'].iloc[i]
            expected_value = date.weekday() < 5  # Business day if weekday is less than 5 (Monday to Friday)
            self.assertEqual(is_business_day, expected_value, f"Failed for row {i}: Expected {expected_value} but got {is_business_day}")

    def test_weekday_name(self):
        # Test the case where weekday name is added correctly
        result = IteratorDateUtils.weekday_name(self.df, 'delivery_start_date', 'weekday_name')

        # Check if the weekday name is correctly assigned for each date in 'delivery_start_date' column
        for i in range(len(result)):
            date = result['delivery_start_date'].iloc[i]
            weekday_name = result['weekday_name'].iloc[i]
            expected_weekday = date.day_name()  # Get the expected weekday name from the date
            self.assertEqual(weekday_name, expected_weekday, f"Failed for row {i}: Expected {expected_weekday} but got {weekday_name}")

    def test_days_difference(self):
        # Test the case where the days difference is calculated correctly
        result = IteratorDateUtils.days_difference(self.df, 'delivery_start_date', 'delivery_end_date', 'days_difference')

        # Check if the days difference is calculated correctly for each row
        for i in range(len(result)):
            start_date = result['delivery_start_date'].iloc[i]
            end_date = result['delivery_end_date'].iloc[i]
            expected_difference = (end_date - start_date).days  # Calculate expected difference
            self.assertEqual(result['days_difference'].iloc[i], expected_difference, 
                             f"Failed for row {i}: Expected {expected_difference} but got {result['days_difference'].iloc[i]}")
    # ==========================
    # Invalid input tests
    # ==========================
    
    def test_invalid_date_column(self):
        # Test case when invalid column name is passed (e.g., non-date column)
        invalid_data = {
            'store': ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
        }
        df_invalid = pd.DataFrame(invalid_data)
        with self.assertRaises(ValueError):
            IteratorDateUtils.business_days_between_rows(df_invalid, 'store', 'business_days_to_previous')

    def test_invalid_column_type(self):
        # Passing a non-date column to date-related functions
        with self.assertRaises(ValueError):
            IteratorDateUtils.business_days_between_rows(self.df, 'store', 'business_days_to_previous')  # 'store' is a non-date column

    def test_invalid_date_column(self):
        # Test case when invalid column name is passed (e.g., non-existent column)
        with self.assertRaises(ValueError):  # Expecting KeyError when the column doesn't exist
            IteratorDateUtils.iter_next_working_day(self.df, 'non_existent_column', 'next_working_day')

    def test_invalid_end_date_column(self):
        # Test case when the end date column doesn't exist
        with self.assertRaises(ValueError):
            IteratorDateUtils.iter_business_days(self.df, 'start_date', 'non_existent_end_date', 'business_days_between')

    def test_add_zero_business_days(self):
        # Test case where zero business days are added (the date should remain the same)
        result = IteratorDateUtils.add_business_days(self.df, 'delivery_start_date', 0, 'same_delivery_date')

        # Check if the new column has the same dates (no change after adding 0 business days)
        for i in range(len(result)):
            original_date = result['delivery_start_date'].iloc[i]
            same_date = result['same_delivery_date'].iloc[i]
            self.assertEqual(original_date, same_date, f"Failed for row {i}: Expected {original_date} but got {same_date}")

    def test_subtract_zero_business_days(self):
        # Test case where zero business days are subtracted (the date should remain the same)
        result = IteratorDateUtils.subtract_business_days(self.df, 'delivery_start_date', 0, 'same_delivery_date')

        # Check if the new column has the same dates (no change after subtracting 0 business days)
        for i in range(len(result)):
            original_date = result['delivery_start_date'].iloc[i]
            same_date = result['same_delivery_date'].iloc[i]
            self.assertEqual(original_date, same_date, f"Failed for row {i}: Expected {original_date} but got {same_date}")

    def test_handle_missing_dates(self):
        # Test case where one of the dates is NaN
        self.df.loc[0, 'delivery_start_date'] = np.nan  # Set a NaN value in the first row
        result = IteratorDateUtils.subtract_business_days(self.df, 'delivery_start_date', 2, 'new_delivery_date')

        # The first row should have NaN in the 'new_delivery_date' column
        self.assertTrue(pd.isna(result['new_delivery_date'].iloc[0]), "Expected NaN for row 0, but got a value")

    def test_handle_missing_dates(self):
        # Test case where one of the dates is NaN
        self.df.loc[0, 'delivery_start_date'] = np.nan  # Set a NaN value in the first row
        result = IteratorDateUtils.weekday_name(self.df, 'delivery_start_date', 'weekday_name')

        # The first row should have NaN in the 'weekday_name' column
        self.assertTrue(pd.isna(result['weekday_name'].iloc[0]), "Expected NaN for row 0, but got a value")

def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)

if __name__ == "__main__":
    main()
