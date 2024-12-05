import pandas as pd

class StreamAggregationsScratch:
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
        
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        # Validate group columns
        if not all(col in df.columns for col in group_columns):
            raise ValueError(f"One or more columns in '{group_columns}' not found in Data.")
        
        # Validate value column
        if value_column not in df.columns:
            raise ValueError(f"Column '{value_column}' not found in Data.")
        
        # Validate numeric dtype for value column
        if not pd.api.types.is_numeric_dtype(df[value_column]):
            raise TypeError(f"The value column '{value_column}' must contain numeric data.")

    @staticmethod
    def _format_output(result, output_type):
        if output_type == 'int':
            result = result.round(0).astype('Int64')
        elif output_type == 'float':
            result = result.round(2)
        else:
            raise ValueError("Invalid 'output_type' value. It must be either 'int' or 'float'.")
        return result

    # 1. Count
    @staticmethod
    def stream_group_count(df, group_columns, value_column, output_type='float'):
        """
        Computes the total number of items in each group.
        """
        StreamAggregationsScratch._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = df.groupby(group_columns).size().reset_index(name='count')
        result["count"] = StreamAggregationsScratch._format_output(result["count"], output_type)
        return result

    # 2. First and Last
    @staticmethod
    def stream_group_first_last(df, group_columns, value_column, output_type='float'):
        """
        Computes the first and last item for each group.
        """
        StreamAggregationsScratch._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = df.groupby(group_columns).agg(first=(value_column, 'first'),
                                               last=(value_column, 'last')).reset_index()
        result["first"] = StreamAggregationsScratch._format_output(result["first"], output_type)
        result["last"] = StreamAggregationsScratch._format_output(result["last"], output_type)
        return result

    # 3. Mean and Median
    @staticmethod
    def stream_group_mean_median(df, group_columns, value_column, output_type='float'):
        """
        Computes the mean and median for each group.
        """
        StreamAggregationsScratch._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = df.groupby(group_columns).agg(mean=(value_column, 'mean'),
                                               median=(value_column, 'median')).reset_index()
        result["mean"] = StreamAggregationsScratch._format_output(result["mean"], output_type)
        result["median"] = StreamAggregationsScratch._format_output(result["median"], output_type)
        return result

    # 4. Minimum and Maximum
    @staticmethod
    def stream_group_min_max(df, group_columns, value_column, output_type='float'):
        """
        Computes the minimum and maximum for each group.
        """
        StreamAggregationsScratch._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = df.groupby(group_columns).agg(min=(value_column, 'min'),
                                               max=(value_column, 'max')).reset_index()
        result["min"] = StreamAggregationsScratch._format_output(result["min"], output_type)
        result["max"] = StreamAggregationsScratch._format_output(result["max"], output_type)
        return result

    # 5. Standard Deviation and Variance
    @staticmethod
    def stream_group_std_var(df, group_columns, value_column, output_type='float'):
        """
        Computes the standard deviation and variance for each group.
        """
        StreamAggregationsScratch._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = df.groupby(group_columns).agg(std=(value_column, 'std'),
                                               var=(value_column, 'var')).reset_index()
        result["std"] = StreamAggregationsScratch._format_output(result["std"], output_type)
        result["var"] = StreamAggregationsScratch._format_output(result["var"], output_type)
        return result

    # 6. Mean Absolute Deviation
    @staticmethod
    def stream_group_mad(df, group_columns, value_column, output_type='float'):
        """
        Computes the mean absolute deviation for each group.
        """
        StreamAggregationsScratch._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        def mad(group_data):
            values = group_data[value_column].dropna().tolist()
            if not values:
                return None
            mean = sum(values) / len(values)
            return sum(abs(x - mean) for x in values) / len(values)
        result = df.groupby(group_columns).apply(mad).reset_index(name="mad")
        result["mad"] = StreamAggregationsScratch._format_output(result["mad"], output_type)
        return result

    # 7. Product
    @staticmethod
    def stream_group_prod(df, group_columns, value_column, output_type='float'):
        """
        Computes the product of all items in each group.
        """
        StreamAggregationsScratch._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = df.groupby(group_columns).agg(prod=(value_column, 'prod')).reset_index()
        result["prod"] = StreamAggregationsScratch._format_output(result["prod"], output_type)
        return result

    # 8. Sum
    @staticmethod
    def stream_group_sum(df, group_columns, value_column, output_type='float'):
        """
        Computes the sum of all items in each group.
        """
        StreamAggregationsScratch._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = df.groupby(group_columns).agg(sum=(value_column, 'sum')).reset_index()
        result["sum"] = StreamAggregationsScratch._format_output(result["sum"], output_type)
        return result
