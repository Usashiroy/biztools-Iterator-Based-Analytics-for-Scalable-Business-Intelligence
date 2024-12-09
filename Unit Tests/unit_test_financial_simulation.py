import sys
import os
current_directory = os.getcwd()
main_directory_path = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, main_directory_path)

import unittest
import pandas as pd
from biztools.financial_simulation import FinancialSimulation  # Replace with the correct import path

class TestFinancialSimulation(unittest.TestCase):

    def test_simulate_investment_growth(self):
        # Test basic growth simulation
        result = FinancialSimulation.simulate_investment_growth(1000, 0.05, 10)
        expected = 1000 * (1 + 0.05) ** 10
        self.assertAlmostEqual(result, expected, places=2)

        # Test zero growth rate
        result = FinancialSimulation.simulate_investment_growth(1000, 0, 10)
        self.assertEqual(result, 1000)

        # Test zero years
        result = FinancialSimulation.simulate_investment_growth(1000, 0.05, 0)
        self.assertEqual(result, 1000)

    def test_simulate_profit_margin(self):
        # Test profit margin calculation
        result = FinancialSimulation.simulate_profit_margin(10000, 0.2)
        expected = 10000 * 0.2
        self.assertAlmostEqual(result, expected, places=2)

        # Test zero revenue
        result = FinancialSimulation.simulate_profit_margin(0, 0.2)
        self.assertEqual(result, 0)

        # Test zero profit margin
        result = FinancialSimulation.simulate_profit_margin(10000, 0)
        self.assertEqual(result, 0)

    def test_run_simulation_growth(self):
        # Define simulation parameters for growth
        params = {
            "initial_investment": [1000, 5000],
            "rate_of_return": [0.05, 0.1],
            "years": [5, 10]
        }
        df = FinancialSimulation.run_simulation(params, simulation_type="growth")
        self.assertEqual(len(df), 8)  # 2 * 2 * 2 = 8 combinations
        self.assertIn("result", df.columns)

        # Check if a sample result is correct
        sample = df[
            (df["initial_investment"] == 1000) &
            (df["rate_of_return"] == 0.05) &
            (df["years"] == 5)
        ]
        expected = 1000 * (1 + 0.05) ** 5
        self.assertAlmostEqual(sample.iloc[0]["result"], expected, places=2)

    def test_run_simulation_profit_margin(self):
        # Define simulation parameters for profit margin
        params = {
            "revenue": [10000, 20000],
            "profit_margin_percentage": [0.1, 0.2]
        }
        df = FinancialSimulation.run_simulation(params, simulation_type="profit_margin")
        self.assertEqual(len(df), 4)  # 2 * 2 = 4 combinations
        self.assertIn("result", df.columns)

        # Check if a sample result is correct
        sample = df[
            (df["revenue"] == 10000) &
            (df["profit_margin_percentage"] == 0.1)
        ]
        expected = 10000 * 0.1
        self.assertAlmostEqual(sample.iloc[0]["result"], expected, places=2)

    def test_run_multiple_simulations(self):
        # Define parameters for two different simulations
        growth_params = {
            "initial_investment": [1000],
            "rate_of_return": [0.05],
            "years": [5]
        }
        profit_params = {
            "revenue": [10000],
            "profit_margin_percentage": [0.1]
        }

        growth_sim = FinancialSimulation.run_simulation(growth_params, simulation_type="growth")
        profit_sim = FinancialSimulation.run_simulation(profit_params, simulation_type="profit_margin")

        # Combine simulations
        combined = FinancialSimulation.run_multiple_simulations([growth_sim, profit_sim])
        self.assertEqual(len(combined), 2)
        self.assertIn("result", combined.columns)

    def test_run_simulation_invalid_type(self):
        # Define invalid simulation type
        params = {
            "initial_investment": [1000],
            "rate_of_return": [0.05],
            "years": [5]
        }
        with self.assertRaises(ValueError):
            FinancialSimulation.run_simulation(params, simulation_type="invalid_type")

    def test_run_simulation_empty_params(self):
        # Define empty parameters
        params = {}
        with self.assertRaises(KeyError):
            FinancialSimulation.run_simulation(params, simulation_type="growth")

if __name__ == "__main__":
    unittest.main()
