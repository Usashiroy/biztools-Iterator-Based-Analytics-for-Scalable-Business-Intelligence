import unittest
import numpy as np
from lazy_rolling_window import LazyRollingWindow
import random

# Assuming LazyRollingWindow is already imported or defined in the same file.

class TestLazyRollingWindow(unittest.TestCase):

    def setUp(self):
        """Setup test data with random values."""
        self.data_valid = [random.randint(1, 100) for _ in range(50)]  # List of 50 random integers
        self.window_size = 5
        self.window = LazyRollingWindow(self.data_valid, self.window_size)

    # ==========================
    # Valid input tests
    # ==========================

    def test_window_sum(self):
        """Test get_window_sum method."""
        window_data = self.data_valid[:self.window_size]  # First window
        expected_sum = sum(window_data)
        self.assertEqual(self.window.get_window_sum(), expected_sum)

    def test_window_avg(self):
        """Test get_window_avg method."""
        window_data = self.data_valid[:self.window_size]  # First window
        expected_avg = sum(window_data) / len(window_data)
        self.assertEqual(self.window.get_window_avg(), expected_avg)

    def test_window_std_dev(self):
        """Test get_window_std_dev method."""
        window_data = self.data_valid[:self.window_size]  # First window
        expected_std_dev = np.std(window_data)
        self.assertAlmostEqual(self.window.get_window_std_dev(), expected_std_dev, places=2)

    def test_window_max(self):
        """Test get_max_of_window method."""
        window_data = self.data_valid[:self.window_size]  # First window
        expected_max = max(window_data)
        self.assertEqual(self.window.get_max_of_window(), expected_max)

    def test_window_min(self):
        """Test get_min_of_window method."""
        window_data = self.data_valid[:self.window_size]  # First window
        expected_min = min(window_data)
        self.assertEqual(self.window.get_min_of_window(), expected_min)

    def test_filter_window(self):
        """Test filter_window method with a simple filter."""
        result = self.window.filter_window(lambda x: x > 50)
        expected_result = [x for x in self.data_valid[:self.window_size] if x > 50]
        self.assertEqual(result, expected_result)

    def test_outliers_detection(self):
        """Test detect_outliers method."""
        result = self.window.detect_outliers()
        # Assuming no outliers in this test (this depends on the random data)
        self.assertEqual(result, [])

    def test_seasonality_detection(self):
        """Test detect_seasonality method."""
        result = self.window.detect_seasonality()
        self.assertIsNotNone(result)

    # ==========================
    # Invalid input tests
    # ==========================

    def test_non_iterable_data(self):
        """Test non-iterable input."""
        with self.assertRaises(TypeError):
            LazyRollingWindow(123, 5)

    def test_empty_data(self):
        """Test empty input data."""
        with self.assertRaises(ValueError):
            LazyRollingWindow([], 5)

    def test_non_numeric_data(self):
        """Test data with non-numeric values."""
        with self.assertRaises(ValueError):
            LazyRollingWindow([1, 2, "a", 4], 5)

    def test_invalid_window_size(self):
        """Test invalid window size."""
        with self.assertRaises(ValueError):
            LazyRollingWindow([1, 2, 3, 4], -1)  # Invalid window size
        with self.assertRaises(ValueError):
            LazyRollingWindow([1, 2, 3, 4], 0)  # Invalid window size
        with self.assertRaises(ValueError):
            LazyRollingWindow([1, 2, 3, 4], "three")  # Invalid window size type

    def test_next_window(self):
        """Test moving to the next window."""
        self.window.next_window()  # Move the window
        window_data = self.data_valid[1:self.window_size+1]  # Next window
        expected_sum = sum(window_data)
        self.assertEqual(self.window.get_window_sum(), expected_sum)

    def test_next_window_at_end(self):
        """Test moving window past the end."""
        window = LazyRollingWindow([1, 2, 3, 4, 5, 6], 3)
        window.next_window()  # First move
        window.next_window()  # Second move
        window.next_window()  # Third move (last valid window)
        self.assertIsNone(window.next_window())  # No further windows available

if __name__ == "__main__":
    unittest.main()
