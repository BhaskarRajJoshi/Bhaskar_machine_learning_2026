# # Chapter 3. If - Else + Recursion:
# ## Factorial using recursion
# **Topic:** *Factorial using Recursion*
# ### **Simple Explanation:**
# A **factorial** of a number is the result of multiplying all whole numbers from that number down to 1.
# For example:
# * The factorial of 5 is: `5 × 4 × 3 × 2 × 1 = 120`
# * The factorial of 3 is: `3 × 2 × 1 = 6`
# * The factorial of 1 is: `1`
# The factorial of 0 is defined as **1** (by convention).
# Now, there('s a smart way to compute factorials using something called **recursion**. '
#            'In recursion, a function calls itself with a smaller input to eventually solve a problem.)
# Example logic:
# * factorial(5) = 5 × factorial(4)
# * factorial(4) = 4 × factorial(3)
# * ...
# * factorial(1) = 1 (this is called the *base case*)
# So it keeps breaking the problem into smaller parts until it reaches 1.
# ### **Exercise:**
# Write a function `factorial_recursive(n)` that takes one argument `n` (a non-negative integer)
# and returns the factorial of that number using recursion.
# If `n` is 0, the function should return 1.
# ### **Example:**
# ```python
# factorial_recursive(5)  # Output: 120
# factorial_recursive(3)  # Output: 6
# factorial_recursive(0)  # Output: 1
# factorial_recursive(1)  # Output: 1
# > 💡 *Hint for learners:* Think about how you can express `factorial(n)` using `factorial(n-1)`.
# Also, make sure to stop when `n` reaches 0 or 1 — that's your base case.

def factorial_recursive(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        factorial = n * factorial_recursive(n-1)
        n -= 1
        return factorial


print(factorial_recursive(5))
print(factorial_recursive(3))
print(factorial_recursive(0))
print(factorial_recursive(1))


