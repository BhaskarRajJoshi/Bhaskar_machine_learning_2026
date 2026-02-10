# ## Detect Outliers with Z-Score
# ### Explanation:
# When we analyze a list of numbers, sometimes some values are *much larger* or *much smaller* than the rest.
# These unusual values are called **outliers**.
# One way to detect outliers is by using the **z-score**.
# The z-score tells us how many standard deviations a number is away from the mean.
# * Formula:
#   $$
#   z = \frac{(x - \text{mean})}{\text{standard deviation}}
#   $$
# If the z-score of a number is greater than a threshold (commonly 2 or 3), we call it an outlier.
# For example:
# * A z-score of 0 means the number is exactly the mean.
# * A z-score of 2 means the number is 2 standard deviations away from the mean (possibly an outlier).
# ---
# ### Exercise:
# Write a function `find_outliers(nums, threshold)` that returns a list of numbers from `nums` that are outliers based on the
# given z-score threshold.
# **Arguments:**
# * `nums`: a list of numbers
# * `threshold`: a number (like 2 or 3) representing how far from the mean we consider values as outliers
# **Return:**
# * A list of numbers from `nums` that are outliers.
# ### Example:
# ```python
# find_outliers([10, 12, 12, 13, 12, 11, 90], 2)
# # Output: [90]
# find_outliers([5, 6, 7, 8, 9, 10, 100], 3)
# # Output: [100]

def find_outliers(nums, threshold):
    a = nums
    sum_l = 0
    for i in range(len(a)):
        sum_l += a[i]
    mean = round(sum_l / len(a))
    sums = 0
    num1 = []
    for j in range(len(a)):
        num1.append(mean - a[j])
        num1[j] = (num1[j] ** 2)
        sums += num1[j]
    avg_sq = round(sums / len(num1))
    standard_deviation = round(avg_sq ** 0.5)
    for i in range(len(a)):
        # print(f'Value of :{a[i]}')
        z = (abs((a[i] - mean) / standard_deviation))
        if z > threshold:
            print(f"The outliners number is : {a[i]} ")

    return f"The outliners number is : {a[i]} "


# print(find_outliers([10, 12, 12, 13, 12, 11, 90], 2))
# print(find_outliers([5, 6, 7, 8, 9, 10, 100], 3))
print(find_outliers([1, 2, 3, 4, 5], 1))
