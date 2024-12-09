import sys
import os
current_directory = os.getcwd()
main_directory_path = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, main_directory_path)

import unittest
from biztools.combinatorial_analytics import CombinatorialAnalytics

class TestCombinatorialAnalytics(unittest.TestCase):
    def setUp(self):
        # Business dataset: sales data with price, sales volume, and region
        self.sales_data = [
            {"product_id": 1, "price": 100, "sales_volume": 200, "region": "North"},
            {"product_id": 2, "price": 150, "sales_volume": 150, "region": "South"},
            {"product_id": 3, "price": 200, "sales_volume": 180, "region": "East"},
            {"product_id": 4, "price": 250, "sales_volume": 220, "region": "West"},
            {"product_id": 5, "price": 180, "sales_volume": 170, "region": "North"},
            {"product_id": 6, "price": 120, "sales_volume": 130, "region": "South"},
        ]
        # Initialize CombinatorialAnalytics class with the data
        self.analytics = CombinatorialAnalytics(self.sales_data)

    # ==========================
    # Valid input tests
    # ==========================

    def test_pairwise_correlation_valid(self):
        price = [row["price"] for row in self.sales_data]
        sales_volume = [row["sales_volume"] for row in self.sales_data]
        
        correlation = self.analytics.pairwise_correlation(price, sales_volume)
        self.assertIsInstance(correlation, float)
        self.assertGreaterEqual(correlation, -1)
        self.assertLessEqual(correlation, 1)

    def test_subset_sum_valid(self):
        sales_volume = [row["sales_volume"] for row in self.sales_data]
        subsets = self.analytics.subset_sum(sales_volume, 500)
        
        self.assertIsInstance(subsets, list)
        self.assertGreater(len(subsets), 0)

    def test_generate_combinatorial_groups_valid(self):
        price = [row["price"] for row in self.sales_data]
        combinations = self.analytics.generate_combinatorial_groups(price, 2)
        
        self.assertIsInstance(combinations, list)
        self.assertGreater(len(combinations), 0)
        self.assertTrue(all(len(comb) == 2 for comb in combinations))

    def test_permutational_growth_paths_valid(self):
        sales_volume = [row["sales_volume"] for row in self.sales_data]
        permutations = self.analytics.permutational_growth_paths(sales_volume)
        
        self.assertIsInstance(permutations, list)
        self.assertGreater(len(permutations), 0)

    def test_pareto_analysis_valid(self):
        sales_volume = [row["sales_volume"] for row in self.sales_data]
        price = [row["price"] for row in self.sales_data]
        
        top_contributors = self.analytics.pareto_analysis(sales_volume, price, top_percentage=50)
        
        self.assertIsInstance(top_contributors, list)
        self.assertGreater(len(top_contributors), 0)

    # ==========================
    # Invalid input tests
    # ==========================

    def test_pairwise_correlation_invalid(self):
        price = []
        sales_volume = []
        
        with self.assertRaises(ValueError):  # Raise ValueError for invalid input
            self.analytics.pairwise_correlation(price, sales_volume)

    def test_subset_sum_invalid(self):
        sales_volume = [row["sales_volume"] for row in self.sales_data]
        subsets = self.analytics.subset_sum(sales_volume, -100)
        
        self.assertEqual(subsets, [])
 
    def test_generate_combinatorial_groups_invalid(self):
        price = [row["price"] for row in self.sales_data]
        
        # Use assertRaises to check that ValueError is raised when r > length of price list
        with self.assertRaises(ValueError):
            self.analytics.generate_combinatorial_groups(price, len(price) + 1)

    def test_permutational_growth_paths_invalid(self):
        sales_volume = []  # Empty list
        with self.assertRaises(ValueError):  # Expecting a ValueError to be raised
            self.analytics.permutational_growth_paths(sales_volume)

    def test_pareto_analysis_invalid(self):
        sales_volume = [row["sales_volume"] for row in self.sales_data]
        price = [row["price"] for row in self.sales_data]

        # Test for invalid top_percentage greater than 100
        with self.assertRaises(ValueError):  # Expecting a ValueError to be raised
            self.analytics.pareto_analysis(sales_volume, price, top_percentage=120)


if __name__ == '__main__':
    unittest.main()
