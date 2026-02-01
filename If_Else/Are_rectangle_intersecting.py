# Are rectangles (with sides parallel to axes) intersecting?
# Topic: Are Rectangles Intersecting?
# Explanation:
# A rectangle on a 2D plane can be defined by its two opposite corners — the bottom-left and the top-right.
# For example, suppose a rectangle has its bottom-left corner at (1, 2) and top-right corner at (4, 5). This rectangle stretches
# from x = 1 to x = 4 and from y = 2 to y = 5.
#
# Two rectangles are said to intersect if they share any area — even a single point on their boundary counts. If one is completely to
# the left, right, above, or below the other, then they do not intersect.
#
# Exercise:
# Write a function are_rectangles_intersecting(rect1, rect2) that takes two rectangles and returns True if they intersect, otherwise
# returns False.
#
# Each rectangle is represented as a tuple of two points: ((x1, y1), (x2, y2)), where
#
# (x1, y1) is the bottom-left corner
# (x2, y2) is the top-right corner
# Function Signature:
# def are_rectangles_intersecting(rect1: tuple, rect2: tuple) -> bool:
# Example Usage:
# # Rectangles overlap partially
# are_rectangles_intersecting(((0, 0), (3, 3)), ((2, 2), (5, 5)))
# # Output: True
#
# # One rectangle is completely to the right of the other
# are_rectangles_intersecting(((0, 0), (1, 1)), ((2, 2), (3, 3)))
# # Output: False
#
# # Touching at corner
# are_rectangles_intersecting(((0, 0), (2, 2)), ((2, 2), (4, 4)))
# # Output: True
#
# # One rectangle inside another
# are_rectangles_intersecting(((0, 0), (5, 5)), ((1, 1), (2, 2)))
# # Output: True
# ✅ Note to Learners:
# Try to reason geometrically: Two rectangles do not intersect if:
#
# One is entirely to the left of the other
# One is entirely to the right of the other
# One is entirely above the other
# One is entirely below the other
# If none of these cases apply, the rectangles must intersect!

def are_rectangles_intersecting(rect1: tuple, rect2: tuple) -> bool:


    if rect1[0][0]<=rect2[0][0]<=rect1[1][0] or rect1[0][1]<=rect2[0][1]<=rect1[1][1]:
        return True
    else:
        return False

print(are_rectangles_intersecting(((0, 0), (3, 3)), ((2, 2), (5, 5))))
print(are_rectangles_intersecting(((0, 0), (1, 1)), ((2, 2), (3, 3))))
print(are_rectangles_intersecting(((0, 0), (2, 2)), ((2, 2), (4, 4))))
print(are_rectangles_intersecting(((0, 0), (5, 5)), ((1, 1), (2, 2))))