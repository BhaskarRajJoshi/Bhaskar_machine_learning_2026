# ## Find Manhattan Distance

# ### **Topic:** *Find Manhattan Distance*

# ---

# ### **Explanation:**

# When you want to measure the distance between two points on a grid (like in a city with square blocks), you don’t move diagonally. Instead, you move only **horizontally** and **vertically**, like a taxi driving along streets and avenues. This kind of distance is called the **Manhattan Distance**.

# The formula to calculate the Manhattan Distance between two points $(x1, y1)$ and $(x2, y2)$ is:

# $$
# \text{Manhattan Distance} = |x1 - x2| + |y1 - y2|
# $$

# Here, $|a|$ means the absolute value of $a$ — in other words, how far the number is from zero.

# For example:

# * From (2, 3) to (5, 1):
# $|2 - 5| = 3$ and $|3 - 1| = 2$, so distance = $3 + 2 = 5$

# ---

# ### **Exercise:**

# Write a function `manhattan_distance(x1, y1, x2, y2)` that takes the coordinates of two points and returns their Manhattan Distance.

# ---

# ### **Example:**

# ```python
# manhattan_distance(2, 3, 5, 1)  # Output: 5
# manhattan_distance(0, 0, 0, 0)  # Output: 0
# manhattan_distance(-1, -1, 1, 1)  # Output: 4
# ```

import logging
def manhattan_distance(x1, y1, x2, y2):
    calculate_distance = abs(x1-x2) + abs(y1-y2)
    logging.info ("The Manhattan distance has been calculated successfully.")
    return f' The Distance is :{calculate_distance}'

a= manhattan_distance(2, 3, 5, 1)  # Output: 5
b= manhattan_distance(0, 0, 0, 0)  # Output: 0
c= manhattan_distance(-1, -1, 1, 1)  # Output: 4

print(a,b,c)