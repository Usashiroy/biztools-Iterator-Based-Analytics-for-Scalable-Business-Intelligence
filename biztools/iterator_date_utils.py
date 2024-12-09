import pandas as pd
from pandas.tseries.offsets import BDay
from collections.abc import Iterable

class IteratorDateUtils:
    @staticmethod
    def _validate_iterable(data):
        """
        Validates that the input is an iterable and converts it to a pandas DataFrame if necessary.

        Args:
            data (Iterable): Input data (e.g., list, tuple, pandas Series, or DataFrame).

        Returns:
            pd.DataFrame: A DataFrame constructed from the input data.

        Raises:
            ValueError: If the input is not a valid iterable or doesn't contain dates.
        """
        if not isinstance(data, Iterable):
            raise ValueError("Input must be an iterable (e.g., list, tuple, pandas Series, or DataFrame).")
        
        # If it's a list, tuple, or Series, convert to DataFrame
        if isinstance(data, (list, tuple, pd.Series)):
            df = pd.DataFrame({ "date": data })
        elif isinstance(data, pd.DataFrame):
            df = data
        else:
            raise ValueError("Unsupported iterable type. Must be a list, tuple, pandas Series, or DataFrame.")

        return df

    @staticmethod
    def _validate_date_column(df, date_col):
        """
        Validates that the specified column exists in the dataframe and contains valid dates.

        Args:
            df (pd.DataFrame): Input dataframe.
            date_col (str): Column name to validate.

        Raises:
            ValueError: If the column does not exist or contains invalid dates.
        """
        if date_col not in df.columns:
            raise ValueError(f"Column '{date_col}' does not exist in the dataframe.")
        
        try:
            pd.to_datetime(df[date_col])
        except Exception:
            raise ValueError(f"Column '{date_col}' does not contain valid date values.")

    @staticmethod
    def business_days_between_rows(data, date_column='delivery_start_date', new_col_name="business_days_to_previous"):
        """
        Adds a column to the dataframe (or returns a new iterable) with the count of business days 
        to the previous row.

        Args:
            data (Iterable): Input data containing dates (list, tuple, Series, or DataFrame).
            date_column (str): The name of the date column in the data.
            new_col_name (str): Name for the new column to be added.

        Returns:
            pd.DataFrame: DataFrame with the business days to the previous row column.
        """
        # Validate the iterable and check if the date column exists
        df = IteratorDateUtils._validate_iterable(data)
        IteratorDateUtils._validate_date_column(df, date_column)
        
        # Shift dates upward to align with the previous row
        df['previous_date'] = df[date_column].shift(1)  

        # Apply business days calculation
        df[new_col_name] = df.apply(
            lambda row: pd.bdate_range(start=row['previous_date'], end=row[date_column]).size - 1
            if pd.notnull(row['previous_date']) else None,
            axis=1
        )
        df.drop(columns=['previous_date'], inplace=True)  # Remove the helper column
        return df

    @staticmethod
    def iter_next_working_day(data, date_column, new_col_name="next_working_day"):
        """
        Adds a column to the dataframe (or returns a new iterable) with the next working day for each date.

        Args:
            data (Iterable): Input data containing dates (list, tuple, Series, or DataFrame).
            date_column (str): The name of the date column to be processed.
            new_col_name (str): Name for the new column to be added.

        Returns:
            pd.DataFrame: DataFrame with the next working day column.
        """
        # Validate the iterable and check if the date column exists
        df = IteratorDateUtils._validate_iterable(data)
        IteratorDateUtils._validate_date_column(df, date_column)
        
        # Calculate next working day by adding one business day to the specified date column
        df[new_col_name] = pd.to_datetime(df[date_column]) + BDay(1)
        return df

    @staticmethod
    def iter_business_days(data, start_date_col, end_date_col, new_col_name="business_days_between"):
        """
        Adds a column to the dataframe with the count of business days between two date columns.

        Args:
            data (pd.DataFrame): Input dataframe (or iterable that can be converted to DataFrame).
            start_date_col (str): Name of the start date column.
            end_date_col (str): Name of the end date column.
            new_col_name (str): Name for the new column to be added.

        Returns:
            pd.DataFrame: DataFrame with the business days between the two dates.
        """
        df = IteratorDateUtils._validate_iterable(data)
        IteratorDateUtils._validate_date_column(df, start_date_col)
        IteratorDateUtils._validate_date_column(df, end_date_col)

        df[new_col_name] = df.apply(
            lambda row: len(pd.bdate_range(start=row[start_date_col], end=row[end_date_col])) - 1
            if pd.notnull(row[start_date_col]) and pd.notnull(row[end_date_col]) else None,
            axis=1
        )
        return df

    @staticmethod
    def add_business_days(data, date_col, num_days, new_col_name="date_plus_business_days"):
        """
        Adds a specified number of business days to each date in a column.

        Args:
            data (Iterable): Input data containing dates (list, tuple, Series, or DataFrame).
            date_col (str): Name of the column containing the base dates.
            num_days (int): Number of business days to add.
            new_col_name (str): Name for the new column to be added.

        Returns:
            pd.DataFrame: DataFrame with a new column of dates plus business days.
        """
        df = IteratorDateUtils._validate_iterable(data)
        IteratorDateUtils._validate_date_column(df, date_col)
        
        if num_days == 0:
            df[new_col_name] = df[date_col]  # If 0 business days, the date stays the same
        else:
            df[new_col_name] = pd.to_datetime(df[date_col]) + BDay(num_days)
        
        return df


    @staticmethod
    def subtract_business_days(data, date_col, num_days, new_col_name="date_minus_business_days"):
        """
        Subtracts a specified number of business days from each date in a column.

        Args:
            data (Iterable): Input data containing dates (list, tuple, Series, or DataFrame).
            date_col (str): Name of the column containing the base dates.
            num_days (int): Number of business days to subtract.
            new_col_name (str): Name for the new column to be added.

        Returns:
            pd.DataFrame: DataFrame with a new column of dates minus business days.
        """
        df = IteratorDateUtils._validate_iterable(data)
        IteratorDateUtils._validate_date_column(df, date_col)
        
        if num_days == 0:
            df[new_col_name] = df[date_col]  # If 0 business days, the date stays the same
        else:
            df[new_col_name] = pd.to_datetime(df[date_col]) - BDay(num_days)
        
        return df


    @staticmethod
    def is_business_day(data, date_col, new_col_name="is_business_day"):
        """
        Checks if each date in a column is a business day.

        Args:
            data (Iterable): Input data containing dates (list, tuple, Series, or DataFrame).
            date_col (str): Name of the column containing the dates to check.
            new_col_name (str): Name for the new column to be added.

        Returns:
            pd.DataFrame: DataFrame with a boolean column indicating if each date is a business day.
        """
        df = IteratorDateUtils._validate_iterable(data)
        IteratorDateUtils._validate_date_column(df, date_col)
        df[new_col_name] = pd.to_datetime(df[date_col]).apply(lambda x: x.weekday() < 5)
        return df

    @staticmethod
    def weekday_name(data, date_col, new_col_name="weekday_name"):
        """
        Adds a column with the name of the weekday for each date.

        Args:
            data (Iterable): Input data containing dates (list, tuple, Series, or DataFrame).
            date_col (str): Name of the column containing the dates.
            new_col_name (str): Name for the new column to be added.

        Returns:
            pd.DataFrame: DataFrame with the weekday name column.
        """
        df = IteratorDateUtils._validate_iterable(data)
        IteratorDateUtils._validate_date_column(df, date_col)
        df[new_col_name] = pd.to_datetime(df[date_col]).dt.day_name()
        return df

    @staticmethod
    def days_difference(data, start_date_col, end_date_col, new_col_name="days_difference"):
        """
        Calculates the total number of days between two date columns.

        Args:
            data (Iterable): Input data containing dates (list, tuple, Series, or DataFrame).
            start_date_col (str): Name of the start date column.
            end_date_col (str): Name of the end date column.
            new_col_name (str): Name for the new column to be added.

        Returns:
            pd.DataFrame: DataFrame with the total days difference column.
        """
        df = IteratorDateUtils._validate_iterable(data)
        IteratorDateUtils._validate_date_column(df, start_date_col)
        IteratorDateUtils._validate_date_column(df, end_date_col)
        df[new_col_name] = (pd.to_datetime(df[end_date_col]) - pd.to_datetime(df[start_date_col])).dt.days
        return df