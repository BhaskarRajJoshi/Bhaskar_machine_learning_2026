# Is a point inside a rectangle?
# Topic: Is a Point Inside a Rectangle (with Sides Parallel to the Axes)?
#
# 🧠 Explanation:
# In geometry, a rectangle is a shape with four sides and four right angles.
# When the sides of a rectangle are parallel to the x and y axes,
# it means the edges of the rectangle are either horizontal or vertical—not slanted.
#
# To describe such a rectangle, we only need two opposite corners:
#
# The bottom-left corner (x1, y1)
# The top-right corner (x2, y2)
# A point has two values: x and y—its horizontal and vertical positions.
#
# To check if a point lies inside (or on the border of) the rectangle, we see if:
#
# The x value of the point is between x1 and x2, and
# The y value of the point is between y1 and y2.
# This assumes x1 < x2 and y1 < y2 (which means the first point is bottom-left
# and the second is top-right).
#
# ✅ Exercise:
# Write a function is_point_inside_rectangle(x1, y1, x2, y2, px, py) that
# returns True if the point (px, py) lies inside or on the boundary of
# the rectangle defined by corners (x1, y1) and (x2, y2), and False otherwise.
#
# 🔍 Example Usage:
# is_point_inside_rectangle(0, 0, 10, 5, 3, 2)   # Output: True
# is_point_inside_rectangle(0, 0, 10, 5, 10, 5)  # Output: True  (point on the corner)
# is_point_inside_rectangle(0, 0, 10, 5, 11, 5)  # Output: False (outside the rectangle)
# is_point_inside_rectangle(-5, -5, 5, 5, 0, 0)  # Output: True  (inside a rectangle with negative coordinates)
# Note: try with negative numbers and boundary points to test your understanding.


def is_point_inside_rectangle(x1, y1, x2, y2, px, py):
    if x1<=px<=x2 and y1<=py<=y2:
        return True
    else:
        return False

print(is_point_inside_rectangle(0, 0, 10, 5, 3, 2) )  # Output: True
print(is_point_inside_rectangle(0, 0, 10, 5, 10, 5))  # Output: True  (point on the corner)
print(is_point_inside_rectangle(0, 0, 10, 5, 11, 5) ) # Output: False (outside the rectangle)
print(is_point_inside_rectangle(-5, -5, 5, 5, 0, 0))  # Output: True  (inside a rectangle with negative coordinates))
print(is_point_inside_rectangle(-5, -5, 5, 5, -5, -4))