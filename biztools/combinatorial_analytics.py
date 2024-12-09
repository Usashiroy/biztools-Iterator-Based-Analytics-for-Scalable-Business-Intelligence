import numpy as np
from scipy.stats import pearsonr

class CombinatorialAnalytics:
    def __init__(self, data):
        """
        Initialize with the data to perform analytics on.
        
        Args:
            data (iterable): Any iterable (list, tuple, set, etc.) containing the data.
        """
        if not hasattr(data, '__iter__'):
            raise TypeError("Data must be an iterable.")
        self.data = data

    def pairwise_correlation(self, numeric_iterable1, numeric_iterable2):
        """
        Calculates the correlation between two numeric iterables.
        
        Args:
            numeric_iterable1 (iterable): First numeric iterable (e.g., list, tuple).
            numeric_iterable2 (iterable): Second numeric iterable (e.g., list, tuple).
            
        Returns:
            float: Pearson correlation coefficient between the two iterables.
        """
        if not numeric_iterable1 or not numeric_iterable2:
            raise ValueError("Iterables cannot be empty.")
        
        # Ensure the iterables are numeric
        if not isinstance(numeric_iterable1, (list, tuple, set)) or not all(isinstance(x, (int, float)) for x in numeric_iterable1):
            raise TypeError("Expected 'numeric_iterable1' to be a list, tuple, or set containing numeric values.")
        
        if not isinstance(numeric_iterable2, (list, tuple, set)) or not all(isinstance(x, (int, float)) for x in numeric_iterable2):
            raise TypeError("Expected 'numeric_iterable2' to be a list, tuple, or set containing numeric values.")
        
        # Ensure both iterables have the same length
        if len(numeric_iterable1) != len(numeric_iterable2):
            raise ValueError("The numeric iterables must have the same length.")
        
        # Calculate the Pearson correlation
        corr, _ = pearsonr(np.array(numeric_iterable1), np.array(numeric_iterable2))
        
        return corr

    def subset_sum(self, numeric_iterable, target_sum):
        """
        Finds subsets of data that add up to a specific target.
        
        Args:
            numeric_iterable (iterable): Iterable of numerical data.
            target_sum (float): The target sum for the subset.
        
        Returns:
            list: List of subsets that add up to target_sum.
        """
        if not numeric_iterable:
            raise ValueError("numeric_iterable cannot be empty.")
        
        if not isinstance(numeric_iterable, (list, tuple, set)) or not all(isinstance(x, (int, float)) for x in numeric_iterable):
            raise TypeError("numeric_iterable must be an iterable of numerical values.")
        if not isinstance(target_sum, (int, float)):
            raise TypeError("Target sum must be a numeric value.")
        
        result = []
        n = len(numeric_iterable)
        
        def find_subsets(idx, current_subset, current_sum):
            if current_sum == target_sum:
                result.append(current_subset)
                return
            if idx >= n or current_sum > target_sum:
                return
            find_subsets(idx + 1, current_subset + [numeric_iterable[idx]], current_sum + numeric_iterable[idx])
            find_subsets(idx + 1, current_subset, current_sum)
        
        find_subsets(0, [], 0)
        return result

    def generate_combinatorial_groups(self, numeric_iterable, r, unique=True):
        """
        Generates all possible r-sized combinations for specified data.
        
        Args:
            numeric_iterable (iterable): Iterable of data elements.
            r (int): Size of each combination.
            unique (bool): Whether to ensure unique combinations when input data has duplicates.
        
        Returns:
            list: A list of all possible r-sized combinations.
        """
        if not numeric_iterable:
            raise ValueError("numeric_iterable cannot be empty.")
        
        if not isinstance(numeric_iterable, (list, tuple, set)):
            raise TypeError("numeric_iterable must be an iterable (list, tuple, or set).")
        if not isinstance(r, int) or r < 0:
            raise ValueError("r must be a non-negative integer.")
        if r > len(numeric_iterable):
            raise ValueError("r cannot be greater than the length of numeric_iterable.")
        if not isinstance(unique, bool):
            raise TypeError("Unique must be a boolean value.")
        
        if unique:
            numeric_iterable = list(set(numeric_iterable))
        
        result = []
        n = len(numeric_iterable)
        stack = [(0, [])]
        
        while stack:
            start, current_combination = stack.pop()
            if len(current_combination) == r:
                result.append(current_combination)
                continue
            for i in range(start, n):
                stack.append((i + 1, current_combination + [numeric_iterable[i]]))
        
        return result

    def permutational_growth_paths(self, numeric_iterable):
        """
        Generates all potential growth paths by rearranging data values.
        
        Args:
            numeric_iterable (iterable): Iterable of numerical values.
        
        Returns:
            list: List of all permutations of growth paths.
        """
        if not numeric_iterable:
            raise ValueError("numeric_iterable cannot be empty.")
        
        if not isinstance(numeric_iterable, (list, tuple, set)) or not all(isinstance(x, (int, float)) for x in numeric_iterable):
            raise TypeError("numeric_iterable must be an iterable of numerical values.")
        
        result = []
        n = len(numeric_iterable)
        
        def generate_permutations(start):
            if start == n:
                result.append(list(numeric_iterable))
                return
            for i in range(start, n):
                numeric_iterable[start], numeric_iterable[i] = numeric_iterable[i], numeric_iterable[start]
                generate_permutations(start + 1)
                numeric_iterable[start], numeric_iterable[i] = numeric_iterable[i], numeric_iterable[start]
        
        generate_permutations(0)
        return result

    def pareto_analysis(self, numeric_iterable, metric_iterable, top_percentage=20):
        """
        Applies Pareto analysis to identify the top contributing factors based on numeric and metric iterables.
        
        Args:
            numeric_iterable (iterable): Iterable containing numeric data for sorting (e.g., list, tuple).
            metric_iterable (iterable): Iterable containing metric values for analysis (e.g., list, tuple, or any type).
            top_percentage (float): The percentage threshold for Pareto analysis (default is 20%).
        
        Returns:
            list: List of top contributing factors based on the Pareto principle.
        """
        if not numeric_iterable or not metric_iterable:
            raise ValueError("Iterables cannot be empty.")
        
        # Ensure numeric_iterable is an iterable containing numeric values
        if not isinstance(numeric_iterable, (list, tuple, set)) or not all(isinstance(x, (int, float)) for x in numeric_iterable):
            raise TypeError("numeric_iterable must be an iterable containing numeric values.")
        
        # Ensure metric_iterable is an iterable (no numeric value check required for metric_iterable)
        if not isinstance(metric_iterable, (list, tuple, set)):
            raise TypeError("metric_iterable must be an iterable.")
        
        # Ensure top_percentage is a valid number between 0 and 100
        if not isinstance(top_percentage, (int, float)) or not (0 < top_percentage <= 100):
            raise ValueError("Top percentage must be a value between 0 and 100.")
        
        # Ensure the iterables have the same length
        if len(numeric_iterable) != len(metric_iterable):
            raise ValueError("numeric_iterable and metric_iterable must have the same length.")
        
        # Sort the data based on the numeric_iterable (numeric data column)
        sorted_data = sorted(zip(numeric_iterable, metric_iterable), key=lambda x: x[0], reverse=True)
        
        # Calculate the total of the numeric data for Pareto calculation
        total_metric = sum(x[0] for x in sorted_data)
        cumulative_sum = 0
        pareto_threshold = total_metric * (top_percentage / 100)
        
        top_contributors = []
        
        # Now, we collect the top contributors based on the Pareto threshold
        for item in sorted_data:
            cumulative_sum += item[0]
            top_contributors.append(item)
            
            # Stop once the cumulative sum exceeds the Pareto threshold
            if cumulative_sum >= pareto_threshold:
                break
        
        return top_contributors
