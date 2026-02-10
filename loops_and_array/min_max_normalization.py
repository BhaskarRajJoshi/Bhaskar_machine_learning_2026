# ## Min-Max Normalization
# ### Explanation:
# When we have numbers that are very different in scale (like exam scores out of 100 and salaries in thousands), it becomes hard to compare them directly.
# **Min-Max Normalization** is a way to rescale numbers so that they fall in a fixed range, usually **0 to 1**.
# The formula is:
# $$
# \text{normalized value} = \frac{(x - \min)}{(\max - \min)}
# $$
# * `x` = the original value
# * `min` = the smallest value in the dataset
# * `max` = the largest value in the dataset
# For example, if your dataset is `[10, 20, 30]` and you want to normalize `20`:
# $$
# \frac{20 - 10}{30 - 10} = \frac{10}{20} = 0.5
# $$
# So the normalized value is **0.5**.
# ---
### Exercise:
# Write a function `min_max_normalize(value, data)` that:
# * Takes two inputs:
#   * `value`: the number you want to normalize
#   * `data`: a list of numbers (dataset)
# * Returns the normalized value of `value` using min-max normalization.
# ---
# ### Example:
# ```python
# min_max_normalize(20, [10, 20, 30])
# # Output: 0.5
# min_max_normalize(10, [10, 20, 30])
# # Output: 0.0
# ---


def min_max_normalize(value, data):
    # a = data
    # a.sort()
    # b = len(a)
    # normalization = (value - a[0])/(a[b-1] - a[0])
    min1 = data[0]
    max1 = data[0]
    for i in range(len(data)):
        if data[i] < min1:
            min1 = data[i]
        if data[i] > max1:
            max1 = data[i]
    normalization = (value - min1)/(max1 - min1)

    return normalization


print(min_max_normalize(20, [10, 20, 30]))
print(min_max_normalize(10, [10, 20, 30]))


# a= [10, 20, 30]
# b = 20
#
# c = min(a)
# d = max(a)
#
# print (c,d)