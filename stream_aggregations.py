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
        
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        if not all(col in df.columns for col in group_columns):
            raise ValueError(f"One or more columns in '{group_columns}' not found in Data.")
        if value_column not in df.columns:
            raise ValueError(f"Column '{value_column}' not found in Data.")
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
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = {}
        for group, group_data in df.groupby(group_columns):
            result[group] = len(group_data)
        result_df = pd.DataFrame(
            list(result.items()),
            columns=group_columns + ["count"]
        )
        result_df["count"] = StreamAggregations._format_output(result_df["count"], output_type)
        return result_df

    # 2. First and Last
    @staticmethod
    def stream_group_first_last(df, group_columns, value_column, output_type='float'):
        """
        Computes the first and last item for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = []
        for group, group_data in df.groupby(group_columns):
            values = group_data[value_column].dropna().tolist()
            first = values[0] if values else None
            last = values[-1] if values else None
            result.append(group + (first, last))
        result_df = pd.DataFrame(result, columns=group_columns + ["first", "last"])
        result_df["first"] = StreamAggregations._format_output(result_df["first"], output_type)
        result_df["last"] = StreamAggregations._format_output(result_df["last"], output_type)
        return result_df

    # 3. Mean and Median
    @staticmethod
    def stream_group_mean_median(df, group_columns, value_column, output_type='float'):
        """
        Computes the mean and median for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = []
        for group, group_data in df.groupby(group_columns):
            values = group_data[value_column].dropna().tolist()
            mean = sum(values) / len(values) if values else None
            median = sorted(values)[len(values) // 2] if values else None
            result.append(group + (mean, median))
        result_df = pd.DataFrame(result, columns=group_columns + ["mean", "median"])
        result_df["mean"] = StreamAggregations._format_output(result_df["mean"], output_type)
        result_df["median"] = StreamAggregations._format_output(result_df["median"], output_type)
        return result_df

    # 4. Minimum and Maximum
    @staticmethod
    def stream_group_min_max(df, group_columns, value_column, output_type='float'):
        """
        Computes the minimum and maximum for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = []
        for group, group_data in df.groupby(group_columns):
            values = group_data[value_column].dropna().tolist()
            min_val = min(values) if values else None
            max_val = max(values) if values else None
            result.append(group + (min_val, max_val))
        result_df = pd.DataFrame(result, columns=group_columns + ["min", "max"])
        result_df["min"] = StreamAggregations._format_output(result_df["min"], output_type)
        result_df["max"] = StreamAggregations._format_output(result_df["max"], output_type)
        return result_df

    # 5. Standard Deviation and Variance
    @staticmethod
    def stream_group_std_var(df, group_columns, value_column, output_type='float'):
        """
        Computes the standard deviation and variance for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = []
        for group, group_data in df.groupby(group_columns):
            values = group_data[value_column].dropna().tolist()
            if not values:
                result.append(group + (None, None))
                continue
            mean = sum(values) / len(values)
            var = sum((x - mean) ** 2 for x in values) / len(values)
            std = var ** 0.5
            result.append(group + (std, var))
        result_df = pd.DataFrame(result, columns=group_columns + ["std", "var"])
        result_df["std"] = StreamAggregations._format_output(result_df["std"], output_type)
        result_df["var"] = StreamAggregations._format_output(result_df["var"], output_type)
        return result_df

    # 6. Mean Absolute Deviation
    @staticmethod
    def stream_group_mad(df, group_columns, value_column, output_type='float'):
        """
        Computes the mean absolute deviation for each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = []
        for group, group_data in df.groupby(group_columns):
            values = group_data[value_column].dropna().tolist()
            if not values:
                result.append(group + (None,))
                continue
            mean = sum(values) / len(values)
            mad = sum(abs(x - mean) for x in values) / len(values)
            result.append(group + (mad,))
        result_df = pd.DataFrame(result, columns=group_columns + ["mad"])
        result_df["mad"] = StreamAggregations._format_output(result_df["mad"], output_type)
        return result_df

    # 7. Product
    @staticmethod
    def stream_group_prod(df, group_columns, value_column, output_type='float'):
        """
        Computes the product of all items in each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = []
        for group, group_data in df.groupby(group_columns):
            values = group_data[value_column].dropna().tolist()
            prod = 1
            for val in values:
                prod *= val
            result.append(group + (prod,))
        result_df = pd.DataFrame(result, columns=group_columns + ["prod"])
        result_df["prod"] = StreamAggregations._format_output(result_df["prod"], output_type)
        return result_df

    # 8. Sum
    @staticmethod
    def stream_group_sum(df, group_columns, value_column, output_type='float'):
        """
        Computes the sum of all items in each group.
        """
        StreamAggregations._validate_inputs(df, group_columns, value_column)
        if isinstance(group_columns, str):
            group_columns = [group_columns]
        result = []
        for group, group_data in df.groupby(group_columns):
            values = group_data[value_column].dropna().tolist()
            result.append(group + (sum(values),))
        result_df = pd.DataFrame(result, columns=group_columns + ["sum"])
        result_df["sum"] = StreamAggregations._format_output(result_df["sum"], output_type)
        return result_df
