import pandas as pd
import numpy as np

class StreamKpiCalculations:

    @staticmethod
    def _validate_iterable(data):
        """Validate that the data is a valid iterable."""
        if not isinstance(data, (pd.DataFrame, pd.Series, list, tuple)):
            raise ValueError("Input data must be a DataFrame, Series, list, or tuple.")
        if isinstance(data, (list, tuple)):
            data = pd.DataFrame(data)
        return data

    @staticmethod
    def _validate_column(df, column):
        """Validate that the specified column exists in the DataFrame."""
        if column not in df.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
    
    @staticmethod
    def stream_revenue_growth(data, revenue_col, new_col_name="revenue_growth"):
        """
        Calculates the revenue growth between each row in a specified column.
        
        Args:
            data (Iterable): Input data (list, tuple, Series, or DataFrame).
            revenue_col (str): The column containing the revenue values.
            new_col_name (str): The new column to store the revenue growth.
        
        Returns:
            pd.DataFrame: DataFrame with the revenue growth column.
        """
        df = StreamKpiCalculations._validate_iterable(data)
        StreamKpiCalculations._validate_column(df, revenue_col)
        
        # Calculate revenue growth as percentage change
        df[new_col_name] = df[revenue_col].pct_change() * 100  # Percentage growth
        
        # Round off values to 2 decimals
        df[new_col_name] = df[new_col_name].round(2)
        
        return df

    @staticmethod
    def stream_churn_rate(data, start_col, end_col, new_col_name="churn_rate"):
        """
        Calculates the churn rate between two columns (e.g., start and end of customer lifecycle).
        
        Args:
            data (Iterable): Input data (list, tuple, Series, or DataFrame).
            start_col (str): Column containing the starting count (e.g., active customers at the start).
            end_col (str): Column containing the ending count (e.g., active customers at the end).
            new_col_name (str): The new column to store the churn rate.
        
        Returns:
            pd.DataFrame: DataFrame with the churn rate column.
        """
        df = StreamKpiCalculations._validate_iterable(data)
        StreamKpiCalculations._validate_column(df, start_col)
        StreamKpiCalculations._validate_column(df, end_col)
        
        # Calculate churn rate: (start - end) / start
        df[new_col_name] = ((df[start_col] - df[end_col]) / df[start_col]) * 100
        
        # Round off values to 2 decimals
        df[new_col_name] = df[new_col_name].round(2)
        
        return df

    @staticmethod
    def stream_growth_rate(data, start_col, end_col, new_col_name="growth_rate"):
        """
        Calculates the growth rate between two columns.
        
        Args:
            data (Iterable): Input data (list, tuple, Series, or DataFrame).
            start_col (str): Column containing the starting value.
            end_col (str): Column containing the ending value.
            new_col_name (str): The new column to store the growth rate.
        
        Returns:
            pd.DataFrame: DataFrame with the growth rate column.
        """
        df = StreamKpiCalculations._validate_iterable(data)
        StreamKpiCalculations._validate_column(df, start_col)
        StreamKpiCalculations._validate_column(df, end_col)
        
        # Calculate growth rate: (end - start) / start
        df[new_col_name] = ((df[end_col] - df[start_col]) / df[start_col]) * 100
        
        # Round off values to 2 decimals
        df[new_col_name] = df[new_col_name].round(2)
        
        return df

