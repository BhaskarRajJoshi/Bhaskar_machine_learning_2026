# ## Multiplication using recursion
# ### **Topic:** *Multiplication using Recursion*
# #### **Simple Explanation:**
# Multiplication means adding a number to itself a certain number of times.
# For example, 4 multiplied by 3 means:
# `4 + 4 + 4 = 12`.
# Recursion means a function that calls itself to solve smaller versions of the same problem.
# Instead of using the `*` (multiplication) operator directly, you can use recursion to repeatedly add a number.
# So, to multiply `a` and `b`, you can add `a` to the result of multiplying `a` and `b-1`.
# Also, consider that:
# * If `b` is 0, the result is 0 (anything multiplied by 0 is 0).
# * If `b` is negative, handle it by converting to positive, and then negating the result.#
# ### **Exercise:**
# Write a function `multiply_recursive(a, b)` that multiplies two integers using recursion (without using the `*` operator).
# * `a`: the first number (int)
# * `b`: the second number (int)
# Return the product of `a` and `b`.
# ### **Example Usage:**
# ```python
# multiply_recursive(4, 3)     # Output: 12

# multiply_recursive(5, 0)     # Output: 0
# multiply_recursive(7, -2)    # Output: -14
# multiply_recursive(-3, -3)   # Output: 9


def multiply_recursive(a, b):

    if b < 0:
        return multiply_recursive(-a, -b)
    if b == 0:
        return 0
    else:
        return a + multiply_recursive(a, b-1)


print(multiply_recursive(4, 3))
print(multiply_recursive(5, 0))
print(multiply_recursive(7, -2))
print(multiply_recursive(-3, -3))

