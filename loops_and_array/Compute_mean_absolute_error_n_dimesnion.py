# **Explanation:**
# The **Mean Absolute Error (MAE)** is a way of measuring how far our predictions are from the actual values.
# It is calculated by taking the **average of the absolute differences** between predicted values and actual values.
# For example, if the true values are `[3, 5, 2]` and the predicted values are `[2, 5, 4]`, the absolute errors are:
# * |3 - 2| = 1
# * |5 - 5| = 0
# * |2 - 4| = 2
# So the MAE is:
# $$
# \text{MAE} = \frac{1 + 0 + 2}{3} = 1
# $$
# In **N-dimensions**, each point can have multiple coordinates. The error is computed for each coordinate,
#     then averaged across all points.
# ---
# **Exercise:**
# Write a function `compute_mae(actual, predicted)` that:
# * Takes two lists of points (each point is a list of numbers, e.g. `[x, y, z, ...]`).
# * Returns the mean absolute error across all dimensions.
# ---
# **Example:**
# ```python
# # Example 1: 1-D
# actual = [3, 5, 2]
# predicted = [2, 5, 4]
# compute_mae(actual, predicted)
# # Output: 1.0
# # Example 2: 2-D
# actual = [[1, 2], [3, 4], [5, 6]]
# predicted = [[2, 2], [2, 5], [5, 7]]
# compute_mae(actual, predicted)
# # Output: 0.8888888888888888
# ```
# 👉 In the second example, the function computes absolute differences for each coordinate, sums them, and
# divides by total number of values (not just points).
# ---