import pandas as pd

class StreamAggregations:
    @staticmethod
    def _validate_inputs(df, group_columns, value_column):
        """
        Validates the input data and columns.
        """
        # Convert dictionary to DataFrame
        if isinstance(df, dict):
            df = pd.DataFrame(df)
        # Convert Series to DataFrame
        elif isinstance(df, pd.Series):
            df = df.reset_index()

        # Check if the input is now a DataFrame
        if not isinstance(df, pd.DataFrame):
            raise TypeError("The input data must be a Pandas DataFrame, Series, or dictionary.")
        
        # Check if DataFrame is empty
        if df.empty:
            return df.empty  # DataFrame is empty
        
        # Convert grouping columns to string type if needed
        for col in group_columns:
            if not pd.api.types.is_string_dtype(df[col]) and not pd.api.types.is_object_dtype(df[col]):
                df[col] = df[col].astype(str)

        # Ensure group_columns is a list
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        
        # Check if all group_columns and value_column exist in DataFrame
        missing_cols = [col for col in group_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Columns '{missing_cols}' not found in Data.")
        if value_column not in df.columns:
            raise ValueError(f"Column '{value_column}' not found in Data.")
        if not pd.api.types.is_numeric_dtype(df[value_column]):
            raise ValueError(f"The value column '{value_column}' must contain numeric data.")
        


    @staticmethod
    def _format_output(result, output_type):
        """
        Formats the output based on the specified output type.
        """
        if output_type == 'int':
            result = result.round(0).astype('Int64')  # Int64 allows for missing values
        elif output_type == 'float':
            result = result.round(2)
        else:
            raise ValueError("Invalid 'output_type' value. It must be either 'int' or 'float'.")
        return result

    @staticmethod
    def stream_group_count(df, group_columns, value_column, output_type='float'):
        """
        Computes the total number of items in each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        result_df = df.groupby(group_columns).size().reset_index(name="count")
        result_df["count"] = StreamAggregations._format_output(result_df["count"], output_type)
        return result_df

    @staticmethod
    def stream_group_first_last(df, group_columns, value_column, output_type='float'):
        """
        Computes the first and last item for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        result_df = df.groupby(group_columns).agg(
            first=(value_column, 'first'),
            last=(value_column, 'last')
        ).reset_index()
        result_df["first"] = StreamAggregations._format_output(result_df["first"], output_type)
        result_df["last"] = StreamAggregations._format_output(result_df["last"], output_type)
        return result_df

    @staticmethod
    def stream_group_mean_median(df, group_columns, value_column, output_type='float'):
        """
        Computes the mean and median for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        result_df = df.groupby(group_columns).agg(
            mean=(value_column, 'mean'),
            median=(value_column, 'median')
        ).reset_index()
        result_df["mean"] = StreamAggregations._format_output(result_df["mean"], output_type)
        result_df["median"] = StreamAggregations._format_output(result_df["median"], output_type)
        return result_df

    @staticmethod
    def stream_group_min_max(df, group_columns, value_column, output_type='float'):
        """
        Computes the minimum and maximum for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        result_df = df.groupby(group_columns).agg(
            min=(value_column, 'min'),
            max=(value_column, 'max')
        ).reset_index()
        result_df["min"] = StreamAggregations._format_output(result_df["min"], output_type)
        result_df["max"] = StreamAggregations._format_output(result_df["max"], output_type)
        return result_df

    @staticmethod
    def stream_group_std_var(df, group_columns, value_column, output_type='float'):
        """
        Computes the standard deviation and variance for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        result_df = df.groupby(group_columns).agg(
            std=(value_column, 'std'),
            var=(value_column, 'var')
        ).reset_index()
        result_df["std"] = StreamAggregations._format_output(result_df["std"], output_type)
        result_df["var"] = StreamAggregations._format_output(result_df["var"], output_type)
        return result_df

    @staticmethod
    def stream_group_mad(df, group_columns, value_column, output_type='float'):
        """
        Computes the mean absolute deviation for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        result_df = df.groupby(group_columns).agg(
            mad=(value_column, lambda x: (abs(x - x.mean())).mean())
        ).reset_index()
        result_df["mad"] = StreamAggregations._format_output(result_df["mad"], output_type)
        return result_df

    @staticmethod
    def stream_group_prod(df, group_columns, value_column, output_type='float'):
        """
        Computes the product of all items in each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        result_df = df.groupby(group_columns).agg(
            prod=(value_column, 'prod')
        ).reset_index()
        result_df["prod"] = StreamAggregations._format_output(result_df["prod"], output_type)
        return result_df

    @staticmethod
    def stream_group_sum(df, group_columns, value_column, output_type='float'):
        """
        Computes the sum of all items in each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        result_df = df.groupby(group_columns).agg(
            sum=(value_column, 'sum')
        ).reset_index()
        result_df["sum"] = StreamAggregations._format_output(result_df["sum"], output_type)
        return result_df
