import sys
import os
current_directory = os.getcwd()
main_directory_path = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, main_directory_path)

import unittest
from biztools.iterable_statistics import IterableStatistics

class TestIterableStatistics(unittest.TestCase):

    # ==========================
    # Valid input tests
    # ==========================
    
    # Test for iterable_count method
    def test_iterable_count_valid_input(self):
        self.assertEqual(IterableStatistics.iterable_count([1, 2, 3, 4]), 4)  # Valid case with 4 elements
        self.assertEqual(IterableStatistics.iterable_count([1, None, 3]), 2)  # Ignore None values
    
    # Test for iterable_mode method
    def test_iterable_mode_valid_input(self):
        self.assertEqual(IterableStatistics.iterable_mode([1, 2, 2, 3, 3, 3]), [3])  # Most frequent value
        self.assertEqual(IterableStatistics.iterable_mode([1, 1, 1, 2, 2]), [1])  # Mode is 1
        self.assertEqual(IterableStatistics.iterable_mode([1, 1, 2, 2]), [1, 2])  # Multiple modes

    # Test for iterable_mean_median method
    def test_iterable_mean_median_valid_input(self):
        self.assertEqual(IterableStatistics.iterable_mean_median([1, 2, 3, 4, 5]), (3.0, 3))  # Mean and median
    
    # Test for iterable_min_max method
    def test_iterable_min_max_valid_input(self):
        self.assertEqual(IterableStatistics.iterable_min_max([1, 2, 3, 4, 5]), (1, 5))  # Min and Max values
    
    # Test for iterable_std_var method
    def test_iterable_std_var_valid_input(self):
        std, var = IterableStatistics.iterable_std_var([1, 2, 3, 4, 5])
        self.assertAlmostEqual(std, 1.414, places=3)  # Standard deviation (approximately 1.414)
        self.assertEqual(var, 2)  # Variance (exact value 2)
        
    # Test for iterable_mad method
    def test_iterable_mad_valid_input(self):
        self.assertEqual(IterableStatistics.iterable_mad([1, 2, 3, 4, 5]), 1.2)  # Mean Absolute Deviation
    
    # Test for iterable_prod method
    def test_iterable_prod_valid_input(self):
        self.assertEqual(IterableStatistics.iterable_prod([1, 2, 3, 4]), 24)  # Product of values
    
    # Test for iterable_sum method
    def test_iterable_sum_valid_input(self):
        self.assertEqual(IterableStatistics.iterable_sum([1, 2, 3, 4, 5]), 15)  # Sum of values
    
    # Test for iterable_first_last method
    def test_iterable_first_last_valid_input(self):
        self.assertEqual(IterableStatistics.iterable_first_last([1, 2, 3]), (1, 3))  # First and last element

    # ==========================
    # Invalid input tests
    # ==========================
    
    # Test for iterable_count method
    def test_iterable_count_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_count(123)  # Invalid input, should be an iterable
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_count({})  # Invalid input, should be a list, tuple, set, or string

    # Test for iterable_mode method
    def test_iterable_mode_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_mode(123)  # Invalid input, should be an iterable like list, tuple, or string
        with self.assertRaises(ValueError):
            IterableStatistics.iterable_mode([])  # Empty iterable should raise an error

    # Test for iterable_mean_median method
    def test_iterable_mean_median_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_mean_median("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_mean_median([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.iterable_mean_median([])  # Empty iterable should raise an error
    
    # Test for iterable_min_max method
    def test_iterable_min_max_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_min_max("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_min_max([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.iterable_min_max([])  # Empty iterable should raise an error
    
    # Test for iterable_std_var method
    def test_iterable_std_var_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_std_var("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_std_var([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.iterable_std_var([])  # Empty iterable should raise an error
    
    # Test for iterable_mad method
    def test_iterable_mad_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_mad("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_mad([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.iterable_mad([])  # Empty iterable should raise an error
    
    # Test for iterable_prod method
    def test_iterable_prod_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_prod("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_prod([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.iterable_prod([])  # Empty iterable should raise an error
    
    # Test for iterable_sum method
    def test_iterable_sum_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_sum("string")  # Invalid input, should be list or tuple of numbers
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_sum([1, 2, 'a'])  # Non-numeric value should raise an error
        with self.assertRaises(ValueError):
            IterableStatistics.iterable_sum([])  # Empty iterable should raise an error
    
    # Test for iterable_first_last method
    def test_iterable_first_last_invalid_input(self):
        with self.assertRaises(TypeError):
            IterableStatistics.iterable_first_last(123)  # Invalid input, should be a list, tuple, set, or string
        with self.assertRaises(ValueError):
            IterableStatistics.iterable_first_last([])  # Empty iterable should raise an error

def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)

if __name__ == "__main__":
    main()
