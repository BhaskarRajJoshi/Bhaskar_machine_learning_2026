# ## *Compute Standard Deviation (SD) of a List of Numbers*
# **Explanation:**
# The *standard deviation* (SD) is a way to measure how spread out numbers are in a list.
# * If the numbers are very close to each other, the SD will be small.
# * If the numbers are spread far apart, the SD will be large.
# To compute the SD:
# 1. Find the *mean* (average) of the numbers.
# 2. Subtract the mean from each number and square the result.
# 3. Find the average of these squared differences.
# 4. Take the square root of that value.
# For example, for the list `[2, 4, 4, 4, 5, 5, 7, 9]`:
# * Mean = 5
# * Squared differences = \[9, 1, 1, 1, 0, 0, 4, 16]
# * Average of squared differences = 4
# * Standard Deviation = √4 = 2
# **Exercise:**
# Write a function `compute_sd(numbers)` that takes a list of numbers and returns the standard
# deviation.
# **Example:**
# ```python
# compute_sd([2, 4, 4, 4, 5, 5, 7, 9])   # Output: 2.0
# compute_sd([10, 10, 10, 10])           # Output: 0.0

def compute_sd(numbers):
    a = numbers
    sum_l = 0
    for i in range(len(a)):
        sum_l += a[i]
    mean = sum_l/len(a)
    sums = 0
    for j in range(len(a)):
        a[j] = mean - a[j]
        a[j] = a[j] ** 2
        sums += a[j]
    avg_sq = sums/len(a)
    standard_deviation = avg_sq ** 0.5

    return standard_deviation


print(compute_sd([2, 4, 4, 4, 5, 5, 7, 9]))
print(compute_sd([10, 10, 10, 10]))
