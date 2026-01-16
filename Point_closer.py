# # Chapter 2. if - else
# ## Check if a point P is closer to point A or point B in 2D
# ### **Topic:** *Check if a Point is Closer to A or B in 2D*
# ### **Explanation:**
# In a 2D plane, a **point** is defined by its coordinates, usually written as (x, y). The **distance** between two points tells us how far apart they are.
# For example, if we have:
# * Point A = (x₁, y₁)
# * Point B = (x₂, y₂)
# * Point P = (x, y)
# We want to find out which point — A or B — is **closer** to point P.
# To figure this out, we calculate the distance from P to both A and B and then compare them.
# You don't need to use square roots — just compare the **squared distances** 
# (it’s faster and gives the same result for comparison).
# ---
# ### **Exercise:**
# Write a function `closer_point(p, a, b)` that takes:
# * `p`: a tuple representing the coordinates of point P
# * `a`: a tuple representing the coordinates of point A
# * `b`: a tuple representing the coordinates of point B
# The function should return:
# * `'A'` if P is closer to A
# * `'B'` if P is closer to B
# * `'Equal'` if the distances are the same
# ---
# ### **Example:**
# ```python
# closer_point((1, 2), (0, 0), (5, 5))     # Output: 'A'  
# closer_point((4, 4), (0, 0), (8, 8))     # Output: 'Equal'  
# closer_point((7, 3), (2, 3), (10, 3))    # Output: 'B'
# ```

def closer_point(p,a,b):
    # calcuate distance between p to A
    # distance_P_A = (p[0]-a[0])**2- (p[1]-a[1])**2
    # # calcuate distance between p to B
    # distance_P_B = (p[0]-b[0])**2- (p[1]-b[1])**2
    # # compare distances
    # if distance_P_A<distance_P_B:
    #     return 'A'
    # elif distance_P_A>distance_P_B:    
    #     return 'B'
    # else:
    #     return 'Equal'  
    (x,y)= p
    (x1,y1)= a
    (x2,y2)=b
    
    distance_pa=(x-x1)**2+(y-y1)**2
    distance_pb=(x-x2)**2+(y-y2)**2

    if distance_pa<distance_pb:
        return 'A'
    elif distance_pa>distance_pb:    
        return 'B'
    else:
        return 'Equal'  

a= closer_point((1, 2), (0, 0), (5, 5))     # Output: 'A' 
b= closer_point((4, 4), (0, 0), (8, 8))     # Output: 'Equal'
c= closer_point((7, 3), (2, 3), (10, 3))    # Output: 'B'

print(a)
print(b)
print(c)