# Biztools: Iterator-Based Analytics for Scalable Business Intelligence
Drawing on the iterator-based approach of Python’s itertools, the biztools package aims to provide a solution for business analytics. By enabling lazy evaluation for business metric calculation like aggregations, rolling averages, and fiscal period calculations, this package is tailored for large datasets and scenarios such as streaming data and time-series analytics. The package will support analytics in the domains of financial simulations, KPI tracking, and data-driven operational decision-making, helping users compute insights without overwhelming system memory. 

The tools are implemented on **[Sales Data](https://github.com/Usashiroy/biztools-Iterator-Based-Analytics-for-Scalable-Business-Intelligence/blob/main/Biztools%20on%20Sales%20data/biztools%20on%20sales%20data.ipynb)** to extract valuable insights using dynamic aggregations, statistical analysis, and financial simulations. Stream aggregations track sales trends, while iterable statistics monitor order progress, highlighting potential delays. Lazy rolling windows smooth data by filtering out outliers for accurate trends. Combinatorial analytics perform Pareto analysis to pinpoint top products, and date utilities optimize scheduling by adjusting for working days. Stream KPIs monitor revenue growth, and financial simulations forecast future profitability, empowering businesses to make informed decisions and improve sales strategies.

To optimize underlying operations, we will be using:

- **Pandas**: For efficient tabular data handling, including data manipulation and analysis.
- **NumPy**: For vectorized operations on datasets, improving the performance of numerical computations.
- **datetime**: For date range generation and timestamp manipulation, essential for temporal data analysis.
- **math**: For basic numeric operations like calculations and constants (e.g., math.sqrt, math.pi).
- **scipy**: For statistical and scientific computations, such as correlation analysis, optimization, and more advanced mathematical operations.
- **collections.abc.Iterable**: To validate and ensure inputs are proper iterables when processing sequences.
- **itertools**: For efficient looping and iteration over large datasets and to simplify repetitive tasks.

Our work will focus on implementing the core functionality of the `biztools` package, leveraging these libraries to enhance performance, reliability, and scalability.

## 1. Stream Aggregations 📊
The StreamAggregations class provides methods to perform common group-based aggregations (such as sum, mean, count, min, max, etc.) on numerical **datasets**. It handles various aggregation operations, offering flexibility in output types, such as int and float.

### Features:
1. **stream_group_count**: Computes the total number of items in each group.
2. **stream_group_first_last**: Computes the first and last item for each group.
3. **stream_group_mean_median**: Computes the mean and median for each group.
4. **stream_group_min_max**: Computes the minimum and maximum for each group.
5. **stream_group_std_var**: Computes the standard deviation and variance for each group.
6. **stream_group_mad**: Computes the mean absolute deviation for each group.
7. **stream_group_prod**: Computes the product of all items in each group.
8. **stream_group_sum**: Computes the sum of all items in each group.

### Example Usage:
```
import pandas as pd
from stream_aggregations import StreamAggregations

# Sample Data
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Initialize and perform aggregations
aggregations = StreamAggregations()

# Count items in each group
count_df = aggregations.stream_group_count(df, group_columns=['Category'], value_column='Value')
print(count_df)

# Compute mean and median for each group
mean_median_df = aggregations.stream_group_mean_median(df, group_columns=['Category'], value_column='Value')
print(mean_median_df)
```
## 2. Iterable Statistics 🧮
IterableStatistics provides methods for statistical operations on general iterables (lists, tuples, sets, and strings). It offers operations like count, mode, mean, median, min, max, standard deviation, variance, sum, and more, making it a flexible tool for simple data collections.

### Difference from Stream Aggregations:
Unlike StreamAggregations (which works with DataFrames/Series), IterableStatistics works with any iterable, making it more general-purpose.

### Features:
1. **iterable_count**: Counts valid elements (non-None).
2. **iterable_mode**: Finds the most frequent element(s).
3. **iterable_mean_median**: Computes mean and median of numeric values.
4. **iterable_min_max**: Finds the minimum and maximum values.
5. **iterable_std_var**: Calculates standard deviation and variance.
6. **iterable_mad**: Computes Mean Absolute Deviation.
7. **iterable_product**: Calculates product of numeric values.
8. **iterable_sum**: Calculates sum of numeric values.
9. **iterable_first_last**: Retrieves the first and last elements of the iterable.

### Example Usage:
```
# Example for Count
iterables = [1, 2, 3, None, 5]
count = IterableStatistics.iterable_count(iterables)
print("Count:", count)  # Output: Count: 4

# Example for Mode
iterables = [1, 2, 2, 3, 3, 3]
mode = IterableStatistics.iterable_mode(iterables)
print("Mode:", mode)  # Output: Mode: [3]

# Example for Mean and Median
iterables = [1, 2, 3, 4, 5]
mean, median = IterableStatistics.iterable_mean_median(iterables)
print("Mean:", mean)  # Output: Mean: 3.0
print("Median:", median)  # Output: Median: 3

# Example for Min and Max
iterables = [1, 2, 3, 4, 5]
min_val, max_val = IterableStatistics.iterable_min_max(iterables)
print("Min:", min_val)  # Output: Min: 1
print("Max:", max_val)  # Output: Max: 5
```

## 3. Lazy Rolling Window 🔄
The LazyRollingWindow class allows users to efficiently apply a rolling window on a numeric dataset. It provides methods for calculating statistical properties, detecting outliers, filtering values, and detecting seasonality in rolling windows.

### Features:
1. **get_window_sum**: Returns the sum of the values in the current window.
2. **get_window_avg**: Returns the average of the values in the current window.
3. **get_window_std_dev**: Returns the standard deviation of the values in the current window.
4. **get_max_of_window**: Returns the maximum value in the current window.
5. **get_min_of_window**: Returns the minimum value in the current window.
6. **filter_window**: Applies a filter on the window based on a condition.
7. **detect_outliers**: Detects outliers in the current window using the IQR method.
8. **detect_seasonality**: Detects simple seasonality patterns in the current window.
9. **next_window**: Moves the window to the next step.

### Example Usage:
```
from lazy_rolling_window import LazyRollingWindow

# Data
data = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Initialize the LazyRollingWindow with data and window size of 3
rolling_window = LazyRollingWindow(data, window_size=3)

# Calculate the sum of values in the first window
print("Window Sum:", rolling_window.get_window_sum())

# Calculate the average of values in the first window
print("Window Avg:", rolling_window.get_window_avg())

# Detect outliers in the first window
print("Outliers:", rolling_window.detect_outliers())

# Detect seasonality in the first window
print("Seasonality:", rolling_window.detect_seasonality())

# Move to the next window
rolling_window.next_window()

# Get the sum in the next window
print("Next Window Sum:", rolling_window.get_window_sum())
```

## 4. Combinatorial Analytics 🔢
The CombinatorialAnalytics class provides methods for performing combinatorial and analytical operations on numerical datasets, including calculating correlations, finding subsets with a specific sum, generating combinations, analyzing growth paths, and applying Pareto analysis.

### Features:
1. **pairwise_correlation**: Calculates the Pearson correlation coefficient between two numeric iterables.
2. **subset_sum**: Finds subsets that sum up to a target value.
3. **generate_combinatorial_groups**: Generates all possible combinations of a given size.
4. **permutational_growth_paths**: Generates all permutations of the data.
5. **pareto_analysis**: Identifies the top contributing factors based on the Pareto principle.

### Example Usage:
```
from combinatorial_analytics import CombinatorialAnalytics

# Data
price = [100, 200, 300, 400, 500]
region = ['North', 'South', 'Southwest', 'East', 'West']

# Initialize and run Pareto analysis
comb_analytics = CombinatorialAnalytics(price)
top_contributors = comb_analytics.pareto_analysis(price, region, top_percentage=20)
print(top_contributors)
```

## 5. Iterator Dates Utils 🗓️

The IteratorDateUtils class provides utility functions for performing various date-related operations on iterable data, such as calculating business days, adding/subtracting business days, determining weekdays, and calculating date differences.

### Features:

1. **business_days_between_rows**: Calculates the difference between two rows e.g. a time series in days.
2. **iter_next_working_day**: Finds the next working day from the date.
3. **iter_business_days**: Calculates number of business days between two date columns.
4. **add_business_days**: Add business days to date.
5. **subtract_business_days**: Subtract business days from date.
6. **is_business_day**: Finds out if the date is a business day or not.
7. **weekday_name**: Returns the weekday.
8. **days_difference**: Calculates the number of days between dates.

### Example Usage:

```
from iterator_date_utils import IteratorDateUtils

#data
data = {
    "date": ["2023-12-01", "2023-12-02", "2023-12-03", "2023-12-04"]  # Includes a weekend
}
df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
num_days = 3

result_df = IteratorDateUtils.add_business_days(df, date_col="date", num_days=num_days, new_col_name="date_plus_3_business_days")
```

## 6. Stream KPI Calculations 📈

The StreamKpiCalculations class provides functions to calculate essential business metrics such as revenue growth, churn rate, and growth rate over time, with data validation and rounding for precision.

### Features:

1. **stream_revenue_growth**: Calculates the revenue growth between each row in a specified column.
2. **stream_churn_rate**: Calculates the churn rate between two columns (e.g., start and end of customer lifecycle).
3. **stream_growth_rate**: Calculates the growth rate between two columns.

### Example Usage:

```
from stream_kpi_calculations import StreamKpiCalculations

#Data
data = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "revenue": [1000, 1200, 1500, 1800]
})

# Calculate revenue growth
result = StreamKpiCalculations.stream_revenue_growth(data, revenue_col="revenue")

```

## 7. Financial Simulation 💰

The FinancialSimulation class provides methods for running simulations to project investment growth, calculate profit margins, and combine multiple scenarios for financial analysis.

### Types:

1. **simulate_investment_growth**: Simulates the growth of an investment over time.
2. **simulate_profit_margin**: Simulates the profit based on revenue and profit margin.

### Features:

1. **run_simulation**: Calculates the revenue growth between each row in a specified column.
2. **run_multiple_simulations**: Calculates the churn rate between two columns (e.g., start and end of customer lifecycle).

### Example Usage:

1. Simulate Investment Growth

```
from your_module_name import FinancialSimulation

# Simulate investment growth
final_value = FinancialSimulation.simulate_investment_growth(
    principal=1000, rate_of_return=0.05, years=10
)

```

2. Simulate Profit Margin

```
from your_module_name import FinancialSimulation

# Simulate profit margin
profit = FinancialSimulation.simulate_profit_margin(
    revenue=20000, profit_margin_percentage=0.2
)

```
## Conclusion:
The **biztools** package offers efficient, iterator-based solutions for scalable business intelligence, allowing businesses to handle large datasets with minimal memory usage. It provides powerful tools for real-time stream aggregations, statistical analysis, rolling window calculations, financial simulations, and KPI tracking, enabling data-driven decision-making in areas like sales, revenue growth, and forecasting. This approach optimizes performance while delivering valuable insights across various business functions.
