
# ## **Topic:** *Predict Y on a Straight Line (2D)*

# ---

# ### **Simple Explanation:**

# In math, a straight line in 2D is usually written in this form:

# ```
# y = m * x + c
# ```

# Here’s what the terms mean:

# * `x` is the input (like a point on the horizontal axis).
# * `y` is the output (like a point on the vertical axis).
# * `m` is the *slope* of the line, which tells us how steep the line is.
# * `c` is the *intercept*, or where the line crosses the y-axis.

# For example:
# If `m = 2`, `c = 3`, and `x = 4`, then:

# ```
# y = 2 * 4 + 3 = 8 + 3 = 11
# ```

# So, the value of `y` is `11`.

# ---

# ### **Exercise:**

# Write a function `predict(m, c, x)` that returns the value of `y` based on the formula:

# ```
# y = m * x + c
# ```

# #### **Arguments:**

# * `m` – slope of the line (a number)
# * `c` – y-intercept of the line (a number)
# * `x` – the x-coordinate (a number)

# #### **Return:**

# * The value of `y` calculated from the formula `y = m * x + c`

# ---

# ### **Example Usage:**

# ```python
# predict(2, 3, 4)     # Output: 11
# predict(-1, 5, 2)    # Output: 3
# ```

def predict(m, c, x):
    
    y = m*x +c
    return f' The prdiction value is: {y}'

a= predict(2, 3, 4)
b= predict(-1, 5, 2) 

print(a, b)
