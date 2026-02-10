# ## *Compute Root Mean Square Error (RMSE) in n-dimensions*
# **Explanation:**
# When we try to measure how close our predicted values are to the actual values, we use something called the *Root Mean Square Error
# (RMSE)*. It tells us, on average, how far our predictions are from the actual values.
# The RMSE is calculated in three steps:
# 1. Subtract each predicted value from the actual value to find the **error**.
# 2. Square each error (to make them positive).
# 3. Find the **average** of these squared errors.
# 4. Take the **square root** of this average.
# In *n-dimensions*, both the actual and predicted values are given as lists (or vectors). For example,
# if the actual values are `[2, 3, 4]` and the predicted values are `[3, 2, 5]`, the errors are `[2-3, 3-2, 4-5] = [-1, 1, -1]`.
# Squaring them gives `[1, 1, 1]`. The average is `1`, and the square root of `1` is `1`. So, the RMSE is `1`.
# ---
# **Exercise:**
# Write a function `compute_rmse(actual, predicted)` that:
# * Takes two lists of equal length: `actual` and `predicted`.
# * Returns the Root Mean Square Error between them.
# ---
# **Example Usage:**
# ```python
# compute_rmse([2, 3, 4], [3, 2, 5])
# # Output: 1.0
# compute_rmse([1, 2, 3], [1, 2, 3])
# # Output: 0.0
# compute_rmse([2, 3, 4], [3, 1, 7])

# def compute_rmse(a, b):
#     c = []
#     d = []
#     sums = 0
#     for i, x in enumerate(a):
#         c.append(x - b[i])
#     for i in range(len(c)):
#         d.append(c[i]**2)
#     for i in range(len(d)):
#         sums += d[i]
#     avg = sums/len(d)
#     sqrt = avg ** 0.5
#
#     return f' The RMSE is {sqrt}'
# print(compute_rmse([2, 3, 4], [3, 2, 5]))
# print(compute_rmse([1, 2, 3], [1, 2, 3]))
# print(compute_rmse([2, 3, 4], [3, 1, 7]))


def compute_rmse(a, b):
    c = []
    sums = 0
    for i, x in enumerate(a):
        c.append(x - b[i])
    for i in c:
        sums += i**2
    avg = sums/len(c)
    sqrt = avg ** 0.5

    return f' The RMSE is {sqrt}'


print(compute_rmse([2, 3, 4], [3, 2, 5]))
print(compute_rmse([1, 2, 3], [1, 2, 3]))
print(compute_rmse([2, 3, 4], [3, 1, 7]))
