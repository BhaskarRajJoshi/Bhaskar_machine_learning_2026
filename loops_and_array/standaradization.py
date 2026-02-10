# ## Standardization
# ### Explanation:
# In data science and machine learning, different features (columns) can have very different ranges.
# For example, a person's **age** may range from 0 to 100, while their **salary** may range from 10,000 to 100,000.
# If we directly use these values, the large numbers (like salaries) may dominate the smaller ones (like age) in calculations.
# **Standardization** is a way to bring all values to a similar scale.
# We do this by subtracting the **mean** and dividing by the **standard deviation**:
# $$
# z = \frac{x - \mu}{\sigma}
# $$
# Where:
# * $x$ is the original value,
# * $\mu$ is the mean of all values,
# * $\sigma$ is the standard deviation of all values,
# * $z$ is the standardized value (also called a *z-score*).
# This process makes the data have a mean of 0 and a standard deviation of 1.
# ---
# ### Exercise:
# Write a function `standardize(data)` that takes a list of numbers and returns a new list where each number is standardized.
# *Hint:* You will need to calculate the mean and standard deviation first.
### Example:
# ```python
# standardize([1, 2, 3, 4, 5])
# # Output: [-1.2649, -0.6325, 0.0, 0.6325, 1.2649]
# standardize([10, 10, 10])
# # Output: [0.0, 0.0, 0.0]   (because all values are the same)
def standardize(data):
    a = data
    sum_l = 0
    for i in range(len(a)):
        sum_l += a[i]
    mean = (sum_l / len(a))
    sums = 0
    num1 = []
    for j in range(len(a)):
        num1.append(mean - a[j])
        num1[j] = (num1[j] ** 2)
        sums += num1[j]
    avg_sq = (sums / len(num1))
    standard_deviation = (avg_sq ** 0.5)
    num2 = []
    for i in range(len(a)):
        # print(f'Value of :{a[i]}')
        if (a[i] - mean) == 0 or standard_deviation == 0:
            num2.append(0)
        else:
            z = ((a[i] - mean) / standard_deviation)
            num2.append(z)
    return num2


print(standardize([1, 2, 3, 4, 5]))
print(standardize([10, 10, 10]))
