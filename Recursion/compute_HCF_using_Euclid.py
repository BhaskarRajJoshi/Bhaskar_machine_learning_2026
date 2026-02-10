# ## Compute HCF using Euclid's Method with Recursion*
# **Topic:** *Compute HCF/GCD using Euclid's Method with Recursion*
# ### **Explanation:**
# HCF stands for **Highest Common Factor**, also known as **GCD (Greatest Common Divisor)**. It is the largest number that evenly divides
# two numbers.
# For example:
# * The HCF of 12 and 18 is 6, because 6 is the biggest number that divides both 12 and 18 without a remainder.
# **Euclid’s Method** is a smart and efficient way to compute the HCF. It works like this:
# * If `b` is 0, the HCF is `a`.
# * Otherwise, HCF of `a` and `b` is the same as the HCF of `b` and `a % b`.
# This method keeps reducing the problem until it finds the HCF. We can use **recursion** to apply this method repeatedly until we
# get the answer.
# ### **Exercise:**
# Write a function named `compute_hcf(a, b)` that takes two positive integers `a` and `b` and returns their HCF using
# Euclid's method with recursion.
# * You should **use recursion** to solve this problem.
# * The function should return an integer.
# ### **Example Usage:**
# ```python
# compute_hcf(12, 18)     # Output: 6
# compute_hcf(100, 25)    # Output: 25
# compute_hcf(17, 13)     # Output: 1
# compute_hcf(0, 5)       # Output: 5
# > 💡 *Hint: Try to express the logic using the rule: HCF(a, b) = HCF(b, a % b)*
# > Remember that recursion means your function will call itself with smaller values until it reaches a stopping point.

def compute_hcf(a, b):
    if b == 0:
        return a
    else:
        return compute_hcf(b, a % b)
   # condition (0,5) is not working
    # if a > b:
    #     a, b = b, a
    # r = b % a
    # if r == 0:
    #     return a
    # return compute_hcf(r, a)


print(compute_hcf(12, 18))    # Output: 6
print(compute_hcf(100, 25))    # Output: 25
print(compute_hcf(17, 13))    # Output: 1
print(compute_hcf(0, 5))       # Output: 5
print(compute_hcf(10, 25))
print(compute_hcf(3050, 4025))
