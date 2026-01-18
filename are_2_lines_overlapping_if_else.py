# ## Are two lines overlapping or touching in 1D
# ### **Topic:** *Are Two Lines Overlapping or Touching in 1D*
# ---
# ### 🧠 **Simple Explanation:**
# Imagine a number line — just a straight line with numbers going from negative to positive. You can draw a line segment between two points, like from -3 to 2. This segment includes every number between -3 and 2.
# Now, suppose you have **two such line segments**. You want to check:
# * Do they **overlap** (share some part)?
# * Do they **touch** (meet at exactly one point)?
# * Or are they **completely separate**?
# For example:
# * Line A: from -3 to 1
# * Line B: from 0 to 4
#   They **overlap**, because they both include 0 and 1.
# Or:
# * Line A: from -5 to -2
# * Line B: from -2 to 3
#   They **touch** at -2.
# ---
# ### 📘 **Exercise:**
# Write a function `are_lines_touching_or_overlapping(start1, end1, start2, end2)` that returns `True` if the two 1D line segments are overlapping or touching, and `False` if they are completely separate.
# 📌 Make sure your function works correctly even if the start is greater than the end — the order shouldn't matter.
# ---
# ### 🔍 **Example Usage:**
# ```python
# are_lines_touching_or_overlapping(1, 4, 3, 6)        # Output: True   (Overlap from 3 to 4)
# are_lines_touching_or_overlapping(1, 3, 3, 5)        # Output: True   (Touch at point 3)
# are_lines_touching_or_overlapping(1, 2, 3, 4)        # Output: False  (Completely separate)
# # Examples with negative numbers
# are_lines_touching_or_overlapping(-3, 1, 0, 4)       # Output: True   (Overlap from 0 to 1)
# are_lines_touching_or_overlapping(-5, -2, -2, 3)     # Output: True   (Touch at point -2)
# are_lines_touching_or_overlapping(-10, -6, -5, -1)   # Output: False  (No touch or overlap)
# are_lines_touching_or_overlapping(-2, -7, -4, -3)    # Output: True   (Overlap from -4 to -3, even with reversed inputs)
# ```
# ## Is a point inside a rectangle?
# **Topic:** *Is a Point Inside a Rectangle (with Sides Parallel to the Axes)

def are_lines_touching_or_overlapping(start1, end1, start2, end2):
    if start1>end1:
        start1,end1=end1,start1
    if start2>end2:
        start2,end2=end2,start2
    if end1<start2 or end2<start1:
        return False
    else:
        return True
#     if not (end1<start2 or end2<start1):
#         return True
#     else:
#         return False
#     if start1<=end2 and start2<=end1:
#         return True
#     else:
#         return False
print(are_lines_touching_or_overlapping(1, 4, 3, 6))        # Output: True   (Overlap from 3 to 4)
print(are_lines_touching_or_overlapping(1, 3, 3, 5))        # Output: True   (Touch at point 3)
print(are_lines_touching_or_overlapping(1, 2, 3, 4))        # Output: False  (Completely separate)
print(are_lines_touching_or_overlapping(-3, 1, 0, 4))       # Output: True   (Overlap from 0 to 1)
print(are_lines_touching_or_overlapping(-5, -2, -2, 3))     # Output: True   (Touch at point -2)
print(are_lines_touching_or_overlapping(-10, -6, -5, -1))   # Output: False  (No touch or overlap)  
print(are_lines_touching_or_overlapping(-2, -7, -4, -3))    # Output: True   (Overlap from -4 to -3, even with reversed inputs) 
print(are_lines_touching_or_overlapping(5, 1, 3, 4))        # Output: False  (Completely separate with reversed inputs)
print(are_lines_touching_or_overlapping(3, 5, 7, 2))        # Output: False  (Completely separate with reversed inputs)
print(are_lines_touching_or_overlapping(4, 1, 1, 6))        # Output: True   (Touch at point 1 with reversed inputs)
print(are_lines_touching_or_overlapping(6, 2, 4, 8))        # Output: True   (Overlap from 4 to 6 with reversed inputs)
print(are_lines_touching_or_overlapping(-1, -4, -3, -2))    # Output: True   (Overlap from -3 to -2 with reversed inputs)
print(are_lines_touching_or_overlapping(-2, -5, -6, -3))    # Output: True   (Overlap from -5 to -3 with reversed inputs)
print(are_lines_touching_or_overlapping(-1, -3, -5, -4))    # Output: False  (Completely separate with reversed inputs)
