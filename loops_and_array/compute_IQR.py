# ## Compute IQR
# ### Explanation:
# The **Interquartile Range (IQR)** is a way to measure how spread out the middle values of a dataset are.
# It is the difference between the **third quartile (Q3)** and the **first quartile (Q1):**
# $$
# IQR = Q3 - Q1
# $$
# * **Q1 (first quartile)** is the value at the 25th percentile of the data (the point where 25% of the data is below it).
# * **Q3 (third quartile)** is the value at the 75th percentile of the data (the point where 75% of the data is below it).
# The IQR is useful for finding out how spread out the “middle” 50% of the data is and is often used to detect **outliers**.
# ---
# ### Exercise:
# Write a function `compute_iqr(data)` that takes a list of numbers and returns the IQR.
# **Hints:**
# * You can sort the data before finding quartiles.
# * Use Python’s `numpy.percentile` function or write your own logic.
# ---
# ### Example:
# ```python
# compute_iqr([1, 2, 3, 4, 5, 6, 7, 8, 9])
# # Q1 = 3, Q3 = 7 → IQR = 7 - 3 = 4
# compute_iqr([10, 20, 30, 40, 50, 60])
# # Q1 = 20, Q3 = 50 → IQR = 50 - 20 = 30
# ```
import numpy as np


def compute_iqr(data):
    data.sort()
    quartile = np.percentile(data, [25, 75], method='nearest')

    iqr = abs(quartile[0] - quartile[1])

    return f" Q1 (first quartile) is {quartile[0]} and Q3 (third quartile) {quartile[1]} and iqr is {iqr}"


print(compute_iqr([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(compute_iqr([10, 20, 30, 40, 50, 60]))
