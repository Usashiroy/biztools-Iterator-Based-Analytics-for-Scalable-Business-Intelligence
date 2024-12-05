import math
import numpy as np
from collections.abc import Iterable

class LazyRollingWindow:
    def __init__(self, data, window_size):
        # Check if data is iterable
        if not isinstance(data, Iterable):
            raise TypeError("Data should be an iterable.")
        
        # Check if data is empty
        if len(data) == 0:
            raise ValueError("Data cannot be empty.")
        
        # Check if all elements can be converted to numeric types (int/float)
        self.data = []
        for item in data:
            try:
                self.data.append(float(item))  # Try to convert to float
            except (ValueError, TypeError):
                raise ValueError(f"Non-numeric value found: {item}. Data should contain only numeric values.")
        
        # Check window_size validity
        if not isinstance(window_size, int) or window_size <= 0:
            raise ValueError("Window size must be a positive integer.")

        self.window_size = window_size
        self.window_start = 0
        self.window_end = window_size

    def _get_window_data(self):
        """Returns the data in the current window."""
        return self.data[self.window_start:self.window_end]
    
    def _update_window(self):
        """Moves the window by one step."""
        if self.window_end < len(self.data):
            self.window_start += 1
            self.window_end += 1

    def get_window_sum(self):
        """Returns the sum of the values in the current window."""
        return sum(self._get_window_data())

    def get_window_avg(self):
        """Returns the average of the values in the current window."""
        window_data = self._get_window_data()
        return sum(window_data) / len(window_data) if len(window_data) > 0 else 0

    def get_window_std_dev(self):
        """Returns the standard deviation of the values in the current window."""
        window_data = self._get_window_data()
        if len(window_data) < 2:
            return 0.0
        return np.std(window_data)

    def get_max_of_window(self):
        """Returns the maximum value in the current window."""
        return max(self._get_window_data())

    def get_min_of_window(self):
        """Returns the minimum value in the current window."""
        return min(self._get_window_data())

    def filter_window(self, condition):
        """Applies a filter on the window (e.g., a condition such as values greater than a threshold)."""
        window_data = self._get_window_data()
        return [x for x in window_data if condition(x)]

    def detect_outliers(self):
        """Detects outliers in the current window using the IQR method."""
        window_data = self._get_window_data()
        if len(window_data) < 4:
            return []
        q1, q3 = np.percentile(window_data, [25, 75])
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        return [x for x in window_data if x < lower_bound or x > upper_bound]

    def detect_seasonality(self):
        """Detects simple seasonality patterns using rolling mean over a window."""
        window_data = self._get_window_data()
        if len(window_data) < 3:
            return None
        rolling_mean = np.mean(window_data)
        deviations = [abs(x - rolling_mean) for x in window_data]
        seasonality_score = np.mean(deviations) / rolling_mean
        return seasonality_score

    def next_window(self):
        """Moves the window to the next step."""
        if self.window_end < len(self.data):
            self._update_window()
        else:
            return None
