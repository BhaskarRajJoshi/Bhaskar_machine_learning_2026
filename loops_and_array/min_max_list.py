# ## Find Minimum and Maximum of a List
# ### Explanation:
# When you have a list of numbers, sometimes you want to know the **smallest number** (called the *minimum*) and the **largest number**
# (called the *maximum*) in that list.
# For example, in the list `[5, 8, 2, 10, 3]`, the smallest number is `2` and the largest number is `10`.
# Finding the minimum and maximum is useful in many real-world cases. For example:
# * In exam scores, the minimum score shows the lowest marks obtained by a student, and the maximum shows the highest marks.
# * In weather data, the minimum temperature tells the coldest reading of the day, and the maximum shows the hottest reading.
# ---
# ### Exercise:
# Write a function `find_min_max(numbers)` that takes a list of numbers as input and returns a tuple `(minimum, maximum)`.
# ---
# ### Example:
# ```python
# find_min_max([5, 8, 2, 10, 3])
# # Output: (2, 10)
# find_min_max([7, 7, 7, 7])
# # Output: (7, 7)
# ```

# def min_max(temp):
"""
a = [5, 8, 2, 10, 3]
min=a[0]
max= 0
for i in range(len(a)):
    if a[i]>max:
        max =a[i]
    if a[i]< min:
        min =a[i]
a.sort()
k =len(a)
print(a[0],a[k-1])
# print(a[i])
print(min)
print(max)
# a.sort()
# print(a)

# for key, value in enumerate(a):
#     print(key,value)
"""
def find_min_max(numbers):
    # a = numbers
    # a.sort()
    # b = len(a)
    #
    # return (a[0],a[b-1])
    min = numbers[0]
    max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
        if numbers[i] < min:
            min = numbers[i]

    return (min,max)

print(find_min_max([5, 8, 2, 10, 3]))
print(find_min_max([7, 7, 7, 7]))

a = [5, 8, 2, 10, 3]
b = a[::-1]
print(a)
print(b)


