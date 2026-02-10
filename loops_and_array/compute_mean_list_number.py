# ## *Compute Mean of a List of Numbers*
# **Explanation:**
# The *mean* (often called the *average*) of a list of numbers is found by adding up all the numbers and then dividing by how many numbers there are.
# For example, if we have the numbers `[2, 4, 6, 8]`, the sum is `2 + 4 + 6 + 8 = 20`.
# There are `4` numbers in the list.
# So, the mean is `20 / 4 = 5`.
# This is a useful way to find the central value of a group of numbers.
# **Exercise:**
# Write a function `compute_mean(numbers)` that takes a list of numbers and returns their mean (average).
# If the list is empty, return `0`.
# **Example:**
# ```python
# compute_mean([2, 4, 6, 8])      # Output: 5.0
# compute_mean([10, 20, 30])      # Output: 20.0
# compute_mean([])                # Output: 0
# ---

def compute_mean(numbers):
    a= numbers
    b = 0
    for i in range(len(a)):
        b += a[i]
    if b > 0:
        return b/len(a)
    else:
        return 0


print(compute_mean([2, 4, 6, 8]))
print(compute_mean([10, 20, 30]))
print(compute_mean([]))
