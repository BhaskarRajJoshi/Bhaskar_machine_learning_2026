# ## Division using recursion to find quotient and remainder
# ### **Topic:** *Division using Recursion to Find Quotient and Remainder*
# #### **Simple Explanation:**
# Division is the process of finding how many times one number (called the **divisor**) fits into another number
# (called the **dividend**).
# For example, in `17 ÷ 5`, the number 5 fits into 17 **three** times (that’s the **quotient**) and there are **2** left over
# (that’s the **remainder**), because:
# ```
# 5 + 5 + 5 = 15, and 17 - 15 = 2
# So, 17 ÷ 5 gives quotient = 3 and remainder = 2
# ```
# **Recursion** means solving a problem by breaking it into smaller versions of the same problem. In this case, we repeatedly subtract
# the divisor from the dividend and count how many times we do it until what’s left is smaller than the divisor (that’s the remainder).
# ---
# ### **Exercise:**
# Write a function `recursive_divide(dividend, divisor)` that returns a tuple `(quotient, remainder)` using recursion.
# You **must not** use the `//` or `%` operators.
# * `dividend`: a non-negative integer
# * `divisor`: a positive integer
# **Return:** A tuple of two integers: `(quotient, remainder)`
# ### **Example Usage:**
# ```python
# recursive_divide(17, 5)   # Output: (3, 2)
# recursive_divide(20, 4)   # Output: (5, 0)
# recursive_divide(7, 3)    # Output: (2, 1)
# recursive_divide(0, 1)    # Output: (0, 0)

# chatGpt used
# def recursive_divide(dividend, divisor):
#     if dividend < divisor:
#         return 0, dividend
#     elif dividend == divisor:
#         return 1, 0
#     elif dividend > divisor:
#         quotient, reminder = recursive_divide(dividend-divisor, divisor)
#         return 1 + quotient, reminder

def recursive_divide(num, den): # return m//n, m % n
    # 2 / 5 return 0, 2
    if num < den:
        return 0, num
    else:
        # 7/5 -> 1 + (7 - 5)/5 ->
        dividend, remainder = recursive_divide(num - den, den)
        return (1 + dividend), remainder


print(recursive_divide(17, 5))
print(recursive_divide(20, 4))
print(recursive_divide(7, 3))
print(recursive_divide(0, 1))
print(recursive_divide(5, 5))
