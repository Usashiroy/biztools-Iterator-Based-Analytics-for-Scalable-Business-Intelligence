import itertools
import pandas as pd

class FinancialSimulation:
    def __init__(self, initial_investment, years):
        self.initial_investment = initial_investment
        self.years = years

    @staticmethod
    def simulate_investment_growth(principal, rate_of_return, years):
        """
        Simulates the growth of an investment over time.

        Args:
            principal (float): The initial investment amount.
            rate_of_return (float): The annual return rate (in decimal form).
            years (int): The number of years for the investment to grow.

        Returns:
            float: The final investment value.
        """
        return principal * (1 + rate_of_return) ** years

    @staticmethod
    def simulate_profit_margin(revenue, profit_margin_percentage):
        """
        Simulates the profit based on revenue and profit margin.

        Args:
            revenue (float): The revenue value.
            profit_margin_percentage (float): The profit margin as a percentage (in decimal form).

        Returns:
            float: The profit value.
        """
        return revenue * profit_margin_percentage

    @staticmethod
    def run_simulation(parameters, simulation_type="growth"):
        """
        Run simulations for different parameter combinations.
        
        Args:
            parameters (dict): Dictionary of parameters for the simulation.
            simulation_type (str): Type of simulation, e.g., "growth" or "profit_margin".
        
        Returns:
            pd.DataFrame: DataFrame of the simulation results.
        """
        # Generate all combinations of the input parameters using itertools.product
        combinations = list(itertools.product(*parameters.values()))

        # Prepare list to hold the results
        results = []

        for combination in combinations:
            param_dict = dict(zip(parameters.keys(), combination))

            if simulation_type == "growth":
                # Simulate investment growth
                result = FinancialSimulation.simulate_investment_growth(
                    param_dict["initial_investment"], param_dict["rate_of_return"], param_dict["years"]
                )
            elif simulation_type == "profit_margin":
                # Simulate profit margin
                result = FinancialSimulation.simulate_profit_margin(
                    param_dict["revenue"], param_dict["profit_margin_percentage"]
                )
            else:
                raise ValueError("Unsupported simulation type")

            # Add the result to the results list
            param_dict["result"] = result
            results.append(param_dict)

        # Return the results as a DataFrame
        return pd.DataFrame(results)

    @staticmethod
    def run_multiple_simulations(simulations):
        """
        Run multiple simulation scenarios using itertools.chain to combine results.
        
        Args:
            simulations (list): List of simulation results (DataFrames).
        
        Returns:
            pd.DataFrame: Combined DataFrame from all simulations.
        """
        # Use itertools.chain to combine results from multiple simulations
        combined_results = list(itertools.chain(*[sim.to_dict(orient="records") for sim in simulations]))

        # Return as DataFrame
        return pd.DataFrame(combined_results)

# # Example Usage

# # Define simulation parameters for investment growth
# investment_params = {
#     "initial_investment": [1000, 5000],  # Different initial investments
#     "rate_of_return": [0.05, 0.1],  # Different rates of return (5% and 10%)
#     "years": [5, 10]  # Different time periods (5 and 10 years)
# }

# # Run investment growth simulations
# growth_simulations = FinancialSimulation.run_simulation(investment_params, simulation_type="growth")
# print("Investment Growth Simulations:")
# print(growth_simulations)

# # Define simulation parameters for profit margin
# profit_params = {
#     "revenue": [10000, 20000],  # Different revenue values
#     "profit_margin_percentage": [0.1, 0.2, 0.5, 1]  # Different profit margins (10% and 20%)
# }

# # Run profit margin simulations
# profit_simulations = FinancialSimulation.run_simulation(profit_params, simulation_type="profit_margin")
# print("\nProfit Margin Simulations:")
# print(profit_simulations)

# # Combine both simulations
# combined_simulations = FinancialSimulation.run_multiple_simulations([growth_simulations, profit_simulations])
# print("\nCombined Simulations:")
# print(combined_simulations)
