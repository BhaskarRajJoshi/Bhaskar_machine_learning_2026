
# ## Given two points, write a function fit() to learn slope and intercept of the line going through them
# ### **Topic:** *Learn Line Equation from Two Points*
# ### **Explanation:**
# A straight line in a 2D plane can be described by the equation:
# $$
# y = mx + c
# $$
# Where:
# * `m` is the **slope** of the line.
# * `c` is the **intercept** — the value of `y` when `x = 0`.
# If you're given **two points** on the line, say `(x1, y1)` and `(x2, y2)`, you can calculate 
# the **slope** `m` like this:
# $$
# m = \frac{y2 - y1}{x2 - x1}
# $$
# Once you have the slope, you can use one of the points (say `(x1, y1)`) to calculate the intercept 
# `c` using:
# $$
# c = y1 - m \times x1
# $$
# For example, if your two points are (1, 2) and (3, 6):
# * Slope: `(6 - 2)/(3 - 1) = 4/2 = 2`
# * Intercept: `2 - (2 × 1) = 0`
# * So, the equation of the line is: `y = 2x + 0`
# ---
# ### **Exercise:**
# Write a function `fit(x1, y1, x2, y2)` that returns a tuple `(m, c)` representing the slope and intercept of the line passing through the two points `(x1, y1)` and `(x2, y2)`.
# ---

def fit(x1, y1, x2, y2):
    if (x2-x1) >0: 
        m=(y2-y1)/(x2-x1)
        c = (y1) -m*(x1)
        return f' The slope of the input is {m} and the intercept is {c}. The combined output is {(m,c)}'
    return f' The provided coordinates are invalid as {x2}-{x1} is equal to {x2-x1}'

a = fit(1, 2, 3, 6)       # Output: (2.0, 0.0)
print(a)

b = fit(1,2,1,6)
print(b)

c = fit(5,2,1,6)
print(c)

d= fit(0, 5, 2, 9)       # Output: (2.0, 5.0)
print(d)