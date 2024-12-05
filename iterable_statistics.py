from collections import Counter

class IterableStatistics:
    # 1. Count
    @staticmethod
    def stream_count(iterables):
        """
        Counts the number of valid (non-None) elements in the iterable.
        """
        if not isinstance(iterables, (list, tuple, set, str)):
            raise TypeError("Input must be a list, tuple, set, or string.")
        return len([x for x in iterables if x is not None])

    # 2. Mode
    @staticmethod
    def stream_mode(iterables):
        """
        Finds the most frequent element(s) in the iterable.
        """
        if not isinstance(iterables, (list, tuple, set, str)):
            raise TypeError("Mode operation is allowed only for strings or iterables.")
        if not iterables:
            raise ValueError("Input iterable is empty. Mode cannot be calculated.")
        counts = Counter(iterables)
        max_count = max(counts.values())
        return [k for k, v in counts.items() if v == max_count]

    # 3. Mean and Median
    @staticmethod
    def stream_mean_median(iterables):
        """
        Calculates the mean and median of numeric values in the iterable.
        """
        if not isinstance(iterables, (list, tuple)):
            raise TypeError("Mean and median operations are allowed only for list or tuple of numeric values.")
        if not all(isinstance(i, (int, float)) for i in iterables):
            raise TypeError("All elements in the iterable must be numeric.")
        if not iterables:
            raise ValueError("Input iterable is empty. Mean and median cannot be calculated.")
        
        numeric_values = sorted(iterables)
        n = len(numeric_values)
        mean = sum(numeric_values) / n
        median = numeric_values[n // 2] if n % 2 != 0 else (numeric_values[n // 2 - 1] + numeric_values[n // 2]) / 2
        return mean, median

    # 4. Minimum and Maximum
    @staticmethod
    def stream_min_max(iterables):
        """
        Finds the minimum and maximum values in the iterable.
        """
        if not isinstance(iterables, (list, tuple)):
            raise TypeError("Min and max operations are allowed only for list or tuple of numeric values.")
        if not all(isinstance(i, (int, float)) for i in iterables):
            raise TypeError("All elements in the iterable must be numeric.")
        if not iterables:
            raise ValueError("Input iterable is empty. Min and max cannot be calculated.")
        
        return min(iterables), max(iterables)

    # 5. Standard Deviation and Variance
    @staticmethod
    def stream_std_var(iterables):
        """
        Calculates the standard deviation and variance of numeric values in the iterable.
        """
        if not isinstance(iterables, (list, tuple)):
            raise TypeError("Standard deviation and variance operations are allowed only for list or tuple of numeric values.")
        if not all(isinstance(i, (int, float)) for i in iterables):
            raise TypeError("All elements in the iterable must be numeric.")
        if not iterables:
            raise ValueError("Input iterable is empty. Standard deviation and variance cannot be calculated.")
        
        n = len(iterables)
        mean = sum(iterables) / n
        var = sum((x - mean) ** 2 for x in iterables) / n
        std = var ** 0.5
        return std, var

    # 6. Mean Absolute Deviation
    @staticmethod
    def stream_mad(iterables):
        """
        Calculates the mean absolute deviation of numeric values in the iterable.
        """
        if not isinstance(iterables, (list, tuple)):
            raise TypeError("Mean absolute deviation is allowed only for list or tuple of numeric values.")
        if not all(isinstance(i, (int, float)) for i in iterables):
            raise TypeError("All elements in the iterable must be numeric.")
        if not iterables:
            raise ValueError("Input iterable is empty. Mean absolute deviation cannot be calculated.")
        
        n = len(iterables)
        mean = sum(iterables) / n
        mad = sum(abs(x - mean) for x in iterables) / n
        return mad

    # 7. Product
    @staticmethod
    def stream_prod(iterables):
        """
        Calculates the product of all numeric values in the iterable.
        """
        if not isinstance(iterables, (list, tuple)):
            raise TypeError("Product operation is allowed only for list or tuple of numeric values.")
        if not all(isinstance(i, (int, float)) for i in iterables):
            raise TypeError("All elements in the iterable must be numeric.")
        if not iterables:
            raise ValueError("Input iterable is empty. Product cannot be calculated.")
        
        prod = 1
        for val in iterables:
            prod *= val
        return prod

    # 8. Sum
    @staticmethod
    def stream_sum(iterables):
        """
        Calculates the sum of all numeric values in the iterable.
        """
        if not isinstance(iterables, (list, tuple)):
            raise TypeError("Sum operation is allowed only for list or tuple of numeric values.")
        if not all(isinstance(i, (int, float)) for i in iterables):
            raise TypeError("All elements in the iterable must be numeric.")
        if not iterables:
            raise ValueError("Input iterable is empty. Sum cannot be calculated.")
        
        return sum(iterables)

    # 9. First and Last
    @staticmethod
    def stream_first_last(iterables):
        """
        Retrieves the first and last elements of the iterable.
        """
        if not isinstance(iterables, (list, tuple, set, str)):
            raise TypeError("Input must be a list, tuple, set, or string.")
        if not iterables:
            raise ValueError("Input iterable is empty. First and last elements cannot be retrieved.")
        return iterables[0], iterables[-1]
