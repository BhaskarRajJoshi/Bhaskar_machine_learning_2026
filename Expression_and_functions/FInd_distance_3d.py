# ## Find Distance 3D

# **Topic:** *Find Distance in 3D*

# ---

# ### 🧠 **Explanation:**

# In everyday life, we often measure the distance between two points—like how far your house is from school. In **3D space**, we do the same, but we also consider height or depth in addition to length and width.

# A point in 3D space is defined using three coordinates:

# * `x` (horizontal)
# * `y` (vertical)
# * `z` (depth)

# To calculate the **distance between two points** in 3D, say:

# * Point A: `(x1, y1, z1)`
# * Point B: `(x2, y2, z2)`

# Come up with 3D distance formula using the Pythagorean theorem into three dimensions.

# ---

# ### 🧪 **Exercise:**

# Write a function called `calculate_distance_3d(x1, y1, z1, x2, y2, z2)` that returns the distance between two 3D points.

# * The function should return the result as a float.
# * You can use the built-in `math.sqrt()` function to calculate the square root.

# ---

# ### ✅ **Examples:**

# ```

# calculate_distance_3d(0, 0, 0, 1, 1, 1)  # Output: 1.7320508075688772
# calculate_distance_3d(2, 3, 5, 2, 3, 5)  # Output: 0.0
# calculate_distance_3d(1, 2, 3, 4, 6, 9)  # Output: 7.810249675906654

# ```
import math 
def calculate_distance_3d(x1, y1, z1, x2, y2, z2):
    distance_3d= math.sqrt((x2-x1)**2+ (y2-y1)**2 + (z2-z1) **2)
    distance_other = ((x2-x1)**2+ (y2-y1)**2+ (z2-z1) **2)**0.5
    return f' distance using math.sqrt is :{distance_3d}', f'distnace using other formlua is :{distance_other}'


print(calculate_distance_3d(0, 0, 0, 1, 1, 1))
print(calculate_distance_3d(2, 3, 5, 2, 3, 5))
print(calculate_distance_3d(1, 2, 3, 4, 6, 9))

