# ## Find Distance 2D

# **Topic:** *Find Distance in 2D*

# ### 🧠 Explanation:

# In everyday life, when we move from one place to another, we cover a certain *distance*. In math, 
# especially in geometry, we often want to calculate the distance between two points on a 
# flat surface (called a 2D plane).

# Each point on this plane can be represented by two numbers:

# * the **x-coordinate** (horizontal position)
# * the **y-coordinate** (vertical position)

# Come up with the formula to calculate the distance between two points $(x1, y1)$ and $(x2, y2)$ 
# based on the **Pythagorean Theorem**, just like finding the hypotenuse of a right triangle.

# ---
import math

def find_distance_2d(x1,y1,x2,y2):
    
    # calculate_distance= ((x2-x1)**2+ (y2-y1)**2) **0.5
    calculate_distance_1= math.sqrt((x2-x1)**2+(y2-y1)**2)

    return f'The calculated distance_1 is :{calculate_distance_1}',f'Type of the column is :{type(calculate_distance_1)}'
# , f'The calculated distance is :{calculate_distance}'

print(find_distance_2d(1,5,7,9))
print(find_distance_2d(0, 0, 3, 4))     # Output: 5.0
print(find_distance_2d(1, 2, 4, 6))     # Output: 5.0