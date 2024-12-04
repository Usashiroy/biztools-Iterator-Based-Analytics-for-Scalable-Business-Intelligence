import pandas as pd
import numpy as np
import math

class StreamAggregations:
    @staticmethod
    def stream_group_sum(df, group_column, value_column):
        """
        Computes group sums for a specified column using Pandas.
        Handles ValueError and TypeError gracefully.
        """
        try:
            if group_column not in df.columns or value_column not in df.columns:
                raise ValueError(f"Columns '{group_column}' or '{value_column}' not found in DataFrame.")
            
            return df.groupby(group_column, as_index=False)[value_column].sum()
        except (ValueError, TypeError) as e:
            print(f"Error in stream_group_sum: {e}")
            return pd.DataFrame()

    @staticmethod
    def stream_group_average(df, group_column, value_column):
        """
        Computes group averages for a specified column using Pandas.
        Handles ValueError and TypeError gracefully.
        """
        try:
            if group_column not in df.columns or value_column not in df.columns:
                raise ValueError(f"Columns '{group_column}' or '{value_column}' not found in DataFrame.")
            
            return df.groupby(group_column, as_index=False)[value_column].mean()
        except (ValueError, TypeError) as e:
            print(f"Error in stream_group_average: {e}")
            return pd.DataFrame()

    @staticmethod
    def stream_group_min_max(df, group_column, value_column):
        """
        Tracks minimum and maximum values in groups using Pandas.
        Handles ValueError and TypeError gracefully.
        """
        try:
            if group_column not in df.columns or value_column not in df.columns:
                raise ValueError(f"Columns '{group_column}' or '{value_column}' not found in DataFrame.")
            
            grouped = df.groupby(group_column, as_index=False)[value_column].agg(['min', 'max']).reset_index()
            grouped.columns = [group_column, 'min', 'max']
            return grouped
        except (ValueError, TypeError) as e:
            print(f"Error in stream_group_min_max: {e}")
            return pd.DataFrame()

    @staticmethod
    def stream_group_multi_aggregate(df, group_column, value_column):
        """
        Performs multiple aggregations (sum, count, avg) in a single operation using Pandas.
        Handles ValueError and TypeError gracefully.
        """
        try:
            if group_column not in df.columns or value_column not in df.columns:
                raise ValueError(f"Columns '{group_column}' or '{value_column}' not found in DataFrame.")
            
            grouped = df.groupby(group_column, as_index=False)[value_column].agg(
                sum="sum",
                count="count",
                avg="mean"
            )
            return grouped
        except (ValueError, TypeError) as e:
            print(f"Error in stream_group_multi_aggregate: {e}")
            return pd.DataFrame()
