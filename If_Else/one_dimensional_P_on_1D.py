# ## Is point on line?
# ### **Topic:** *Is Point P on Line in 1D?*
# ---
# ### **Simple Explanation:**
# In one-dimensional space (like a number line), a line segment is just the portion between two points 
# — for example, between point A and point B.
# We want to check whether a third point P lies *on* this segment. That means P should be:
# * Greater than or equal to the smaller of A and B, **and**
# * Less than or equal to the larger of A and B.
# In simple terms, P is “between” A and B — or equal to one of them.
# For example:
# * If A = 2, B = 5, and P = 3 → P is between 2 and 5 → ✅
# * If A = -5, B = -2, and P = -3 → P is between -5 and -2 → ✅
# * If A = -5, B = -2, and P = -6 → P is outside the range → ❌
# * If A = 2, B = 5, and P = 2 → P is between 2 and 5 → ✅
# It doesn’t matter whether A is smaller than B or the other way around — we always check the range 
# between them.
# ---
# ### **Exercise:**
# Write a function `is_point_on_line_1d(a, b, p)` that returns `True` if point `p` lies on the line 
# segment between `a` and `b`, and `False` otherwise.
# ---
# ### **Example Usage:**
# ```python
# is_point_on_line_1d(2, 5, 3)      # Output: True  
# is_point_on_line_1d(5, 2, 3)      # Output: True  
# is_point_on_line_1d(2, 5, 6)      # Output: False  
# is_point_on_line_1d(4, 4, 4)      # Output: True  (A single point segment)
# is_point_on_line_1d(4, 4, 5)      # Output: False
# # With negative numbers:
# is_point_on_line_1d(-5, -2, -3)   # Output: True  
# is_point_on_line_1d(-5, -2, -6)   # Output: False  
# is_point_on_line_1d(-2, -5, -4)   # Output: True  
# is_point_on_line_1d(-1, 3, 0)     # Output: True
# ```

def is_point_on_line_1d(a, b, p):
    # if p>=a and p<=b:
        # return True
    # elif p>=b and p<=a:
        # return True
    # else:
        # return False 
#    if min(a,b)<=p<=max(a,b):
#          return True
#    else:
#         return False
    # if (p>=a and p<=b) or (p>=b and p<=a):
    #     return True
    # else:
    #     return False
    if a<=p<=b or b<=p<=a:
        return True
    else:
        return False
print(is_point_on_line_1d(2, 5, 3))      # Output: True  
print(is_point_on_line_1d(5, 2, 3))     # Output: True  
print(is_point_on_line_1d(2, 5, 6))    # Output: False  
print(is_point_on_line_1d(4, 4, 4))      # Output: True  (A single point segment)
print(is_point_on_line_1d(4, 4, 5))      # Output: False
# With negative numbers:
print(is_point_on_line_1d(-5, -2, -3))   # Output: True  
print(is_point_on_line_1d(-5, -2, -6))   # Output: False  
print(is_point_on_line_1d(-2, -5, -4))   # Output: True  
print(is_point_on_line_1d(-1, 3, 0))     # Output: True