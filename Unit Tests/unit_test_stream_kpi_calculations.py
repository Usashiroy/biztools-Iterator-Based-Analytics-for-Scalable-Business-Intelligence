import sys
import os
current_directory = os.getcwd()
main_directory_path = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, main_directory_path)


import unittest
import pandas as pd
from stream_kpi_calculations import StreamKpiCalculations  # Replace with the correct import for your module

class TestStreamKpiCalculations(unittest.TestCase):

    def setUp(self):
        # Sample data setup
        self.data = {
            'revenue': [1000, 1500, 2000, 1200, 1700],
            'start_customers': [200, 250, 300, 220, 270],
            'end_customers': [180, 230, 280, 210, 260]
        }
        self.df = pd.DataFrame(self.data)

    # ==========================
    # Valid input tests
    # ==========================
    
    def test_revenue_growth(self):
        result = StreamKpiCalculations.stream_revenue_growth(self.df, 'revenue', 'revenue_growth')
        
        # Check if the growth rate is calculated and rounded to 2 decimal places
        for value in result['revenue_growth']:
            # Skip NaN values and check for rounding
            if pd.notna(value):
                self.assertEqual(round(value, 2), value)

    def test_churn_rate(self):
        result = StreamKpiCalculations.stream_churn_rate(self.df, 'start_customers', 'end_customers', 'churn_rate')
        
        # Check if the churn rate is calculated and rounded to 2 decimal places
        for value in result['churn_rate']:
            self.assertEqual(round(value, 2), value)

    def test_growth_rate(self):
        result = StreamKpiCalculations.stream_growth_rate(self.df, 'start_customers', 'end_customers', 'growth_rate')
        
        # Check if the growth rate is calculated and rounded to 2 decimal places
        for value in result['growth_rate']:
            self.assertEqual(round(value, 2), value)

    # ==========================
    # Edge cases and invalid input tests
    # ==========================
    
    def test_invalid_column(self):
        with self.assertRaises(ValueError):
            StreamKpiCalculations.stream_revenue_growth(self.df, 'non_existent_column', 'revenue_growth')

def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)

if __name__ == "__main__":
    main()
