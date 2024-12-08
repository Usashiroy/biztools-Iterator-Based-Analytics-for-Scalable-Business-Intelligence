import math
from collections import Counter

class IterableStatistics:
    @staticmethod
    def _filter_valid(iterables):
        """
        Filters out None and NaN values from the iterable.
        """
        return [x for x in iterables if x is not None and not (isinstance(x, float) and math.isnan(x))]
    
    # 1. Count
    @staticmethod
    def iterable_count(iterables):
        valid_items = IterableStatistics._filter_valid(iterables)
        return len(valid_items)

    # 2. Mode
    @staticmethod
    def iterable_mode(iterables):
        valid_items = IterableStatistics._filter_valid(iterables)
        if not valid_items:
            raise ValueError("Input iterable is empty or contains only invalid values. Mode cannot be calculated.")
        counts = Counter(valid_items)
        max_count = max(counts.values())
        return [k for k, v in counts.items() if v == max_count]

    # 3. Mean and Median
    @staticmethod
    def iterable_mean_median(iterables):
        valid_items = IterableStatistics._filter_valid(iterables)
        if not valid_items:
            raise ValueError("Input iterable is empty or contains only invalid values. Mean and median cannot be calculated.")
        if not all(isinstance(i, (int, float)) for i in valid_items):
            raise TypeError("All elements in the iterable must be numeric.")
        
        valid_items.sort()
        n = len(valid_items)
        mean = sum(valid_items) / n
        median = valid_items[n // 2] if n % 2 != 0 else (valid_items[n // 2 - 1] + valid_items[n // 2]) / 2
        return mean, median

    # 4. Minimum and Maximum
    @staticmethod
    def iterable_min_max(iterables):
        valid_items = IterableStatistics._filter_valid(iterables)
        if not valid_items:
            raise ValueError("Input iterable is empty or contains only invalid values. Min and max cannot be calculated.")
        return min(valid_items), max(valid_items)

    # 5. Standard Deviation and Variance
    @staticmethod
    def iterable_std_var(iterables):
        valid_items = IterableStatistics._filter_valid(iterables)
        if not valid_items:
            raise ValueError("Input iterable is empty or contains only invalid values. Standard deviation and variance cannot be calculated.")
        n = len(valid_items)
        mean = sum(valid_items) / n
        var = sum((x - mean) ** 2 for x in valid_items) / n
        std = var ** 0.5
        return std, var

    # 6. Mean Absolute Deviation
    @staticmethod
    def iterable_mad(iterables):
        valid_items = IterableStatistics._filter_valid(iterables)
        if not valid_items:
            raise ValueError("Input iterable is empty or contains only invalid values. Mean absolute deviation cannot be calculated.")
        n = len(valid_items)
        mean = sum(valid_items) / n
        mad = sum(abs(x - mean) for x in valid_items) / n
        return mad

    # 7. Product
    @staticmethod
    def iterable_prod(iterables):
        valid_items = IterableStatistics._filter_valid(iterables)
        if not valid_items:
            raise ValueError("Input iterable is empty or contains only invalid values. Product cannot be calculated.")
        prod = 1
        for val in valid_items:
            prod *= val
        return prod

    # 8. Sum
    @staticmethod
    def iterable_sum(iterables):
        valid_items = IterableStatistics._filter_valid(iterables)
        if not valid_items:
            raise ValueError("Input iterable is empty or contains only invalid values. Sum cannot be calculated.")
        return sum(valid_items)

    # 9. First and Last
    @staticmethod
    def iterable_first_last(iterables):
        valid_items = IterableStatistics._filter_valid(iterables)
        if not valid_items:
            raise ValueError("Input iterable is empty or contains only invalid values. First and last elements cannot be retrieved.")
        return valid_items[0], valid_items[-1]
