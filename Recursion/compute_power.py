# ## Compute power(x, n) using recursion where n is a positive integer.
# **Topic:** *Compute Power Using Recursion*
# **Explanation:** The *power* of a number means multiplying it by itself several times.
# For example, $x^n$ means multiplying $x$ by itself $n$ times.
# * $2^3 = 2 \times 2 \times 2 = 8$
# * $5^2 = 5 \times 5 = 25$
# Recursion is a method where a function calls itself to solve a smaller part of the same problem.
# For computing $x^n$ recursively:
# * If $n = 1$, the result is $x$.
# * Otherwise, $x^n = x \times x^{n-1}$.
# **Exercise:**
# Write a function `power(x, n)` that uses recursion to return $x^n$, where `n` is a positive integer.
# **Example:**
# ```python
# power(2, 3)   # Output: 8
# power(5, 2)   # Output: 25
# ```
# ## Compute power(x, n) using recursion where n is an integer i.e. it can be positive, negative or zero.
# **Topic:** *Compute Power using Recursion*
# **Explanation:** Power means multiplying a number by itself several times.
# For example, $2^3 = 2 \times 2 \times 2 = 8$. Here, $2$ is called the base, and $3$ is called the exponent.
# If the exponent is:
# * **Zero**, any non-zero base raised to the power of 0 is 1. (e.g., $5^0 = 1$)
# * **Positive**, it means multiplying the base that many times. (e.g., $3^2 = 3 \times 3 = 9$)
# * **Negative**, it means dividing 1 by the base raised to the positive exponent. (e.g., $2^{-3} = 1 / (2^3) = 1/8$)
# We can calculate power using **recursion**, where the function calls itself with a smaller exponent until it reaches the base case.
# **Exercise:**
# Write a function `compute_power(x, n)` that returns $x^n$ using recursion. Handle positive, negative, and zero values of $n$.
# **Example:**
# ```python
# compute_power(2, 3)   # Output: 8
# compute_power(2, -3)  # Output: 0.125
# compute_power(5, 0)   # Output: 1

def compute_power(x, n):
    if n > 0:
        return x * compute_power(x, n-1)
    elif n < 0:
        return 1 / compute_power(x, -n)
    else:
        return 1


print(compute_power(2, 3))
print(compute_power(2, -3))
print(compute_power(5, 0))
