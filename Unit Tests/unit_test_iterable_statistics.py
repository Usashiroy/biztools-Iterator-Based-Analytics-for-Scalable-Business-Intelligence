import sys
import os
current_directory = os.getcwd()
main_directory_path = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, main_directory_path)

import unittest
from iterable_statistics import IterableStatistics

class TestIterableStatistics(unittest.TestCase):

    # ==========================
    # Valid input tests
    # ==========================
    
    # Test for stream_count method
    def test_stream_count_valid_input(self):
        self.assertEqual(IterableStatistics.stream_count([1, 2, 3, 4]), 4)  # Valid case with 4 elements
        self.assertEqual(IterableStatistics.stream_count([1, None, 3]), 2)  # Ignore None values
    
    # Test for stream_mode method
    def test_stream_mode_valid_input(self):
        self.assertEqual(IterableStatistics.stream_mode([1, 2, 2, 3, 3, 3]), [3])  # Most frequent value
        self.assertEqual(IterableStatistics.stream_mode([1, 1, 1, 2, 2]), [1])  # Mode is 1
        self.assertEqual(IterableStatistics.stream_mode([1, 1, 2, 2]), [1, 2])  # Multiple modes

    # Test for stream_mean_median method
    def test_stream_mean_median_valid_input(self):
        self.assertEqual(IterableStatistics.stream_mean_median([1, 2, 3, 4, 5]), (3.0, 3))  # Mean and median
    
    # Test for stream_min_max method
    def test_stream_min_max_valid_input(self):
        self.assertEqual(IterableStatistics.stream_min_max([1, 2, 3, 4, 5]), (1, 5))  # Min and Max values
    
    # Test for stream_std_var method
    def test_stream_std_var_valid_input(self):
        self.assertAlmostEqual(IterableStatistics.stream_std_var([1, 2, 3, 4, 5]), 1.58, places=2)  # Standard deviation and variance
    
    # Test for stream_mad method
    def test_stream_mad_valid_input(self):
        self.assertEqual(IterableStatistics.stream_mad([1, 2, 3, 4, 5]), 1.2)  # Mean Absolute Deviation
    
    # Test for stream_prod method
    def test_stream_prod_valid_input(self):
        self.assertEqual(IterableStatistics.stream_prod([1, 2, 3, 4]), 24)  # Product of values
    
    # Test for stream_sum method
    def test_stream_sum_valid_input(self):
        self.assertEqual(IterableStatistics.stream_sum([1, 2, 3, 4, 5]), 15)  # Sum of values
    
    # Test for stream_first_last method
    def test_stream_first_last_valid_input(self):
        self.assertEqual(IterableStatistics.stream_first_last([1, 2, 3]), (1, 3))  # First and last element

    # ==========================
    # Invalid input tests
    # ==========================
    
    # Test for stream_count method
    def test_stream_count_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.stream_count(123)  # Invalid input, should be an iterable
        with self.assertRaises(TypeError):
            IterableStatistics.stream_count({})  # Invalid input, should be a list, tuple, set, or string

    # Test for stream_mode method
    def test_stream_mode_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.stream_mode(123)  # Invalid input, should be an iterable like list, tuple, or string
        with self.assertRaises(ValueError):
            IterableStatistics.stream_mode([])  # Empty iterable should raise an error

    # Test for stream_mean_median method
    def test_stream_mean_median_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.stream_mean_median("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.stream_mean_median([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.stream_mean_median([])  # Empty iterable should raise an error
    
    # Test for stream_min_max method
    def test_stream_min_max_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.stream_min_max("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.stream_min_max([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.stream_min_max([])  # Empty iterable should raise an error
    
    # Test for stream_std_var method
    def test_stream_std_var_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.stream_std_var("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.stream_std_var([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.stream_std_var([])  # Empty iterable should raise an error
    
    # Test for stream_mad method
    def test_stream_mad_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.stream_mad("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.stream_mad([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.stream_mad([])  # Empty iterable should raise an error
    
    # Test for stream_prod method
    def test_stream_prod_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.stream_prod("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.stream_prod([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.stream_prod([])  # Empty iterable should raise an error
    
    # Test for stream_sum method
    def test_stream_sum_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.stream_sum("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.stream_sum([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.stream_sum([])  # Empty iterable should raise an error
    
    # Test for stream_first_last method
    def test_stream_first_last_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.stream_first_last(123)  # Invalid input, should be a list, tuple, set, or string
        with self.assertRaises(ValueError):
            IterableStatistics.stream_first_last([])  # Empty iterable should raise an error

def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)

if __name__ == "__main__":
    main()
