# ## find first derivaative of a function that takes only one argument. 
# ### **Topic:** *Find First Derivative of a Function*
# #### **Simple Explanation:**
# In mathematics, the *derivative* of a function tells us how fast the function's value is changing at 
# a particular point.
# Think of it like this: if you’re driving a car and your distance changes every second, then your speed
# is the derivative of your distance. Similarly, for any function, the derivative gives the 
# *rate of change*.
# We’ll use a simple numerical technique called the **difference method**:
# $$
# f'(x) \approx \frac{f(x + h) - f(x)}{h}
# $$
# This is called the **forward difference method**, where `h` is a very small number.
# ---
# ### **Exercise:**
# Write a function `approx_derivative(func, x, h)` that:
# * Takes a function `func` that accepts a single argument,
# * A value `x` where we want to find the derivative,
# * And a small number `h` (like `0.0001`),
# * Returns the approximate derivative of `func` at `x`.
# ---
# ### **Example Usage:**
# ```python
# def square(x):
#     return x * x
# def cube(x):
#     return x * x * x
# print(approx_derivative(square, 3, 0.0001))  # Output: Approx. 6
# print(approx_derivative(cube, 2, 0.0001))    # Output: Approx. 12
# ```
# ---
# ### **Note to Learner:**
# Try different values of `x` and different functions (like `math.sin`, `math.exp`, etc.) to see how the derivative changes.
# Make sure to import any libraries (like `math`) if needed.

import math 
def square(x):
    return x * x

def cube(x):
    return x * x * x

def trigno(x):
    return math.sin(x)* math.cos(x)

def area(x):
    return math.pi*x *x

def approx_derivative(func, x, h):
    
    return  f' The calculated derivate of function  {func.__name__} is , {(func(x + h) - func(x)) / h}'
    
# Example Usage
print(approx_derivative(square, 3, 0.0001))  # Output: Approx. 6
print(approx_derivative(cube, 2, 0.0001))    # Output: Approx. 12
print(approx_derivative(trigno, math.pi/4, 0.0001))  # Output: Approx. 0
print(approx_derivative(area, 5, 0.0001))    # Output: Approx. 31.415992653589793
         