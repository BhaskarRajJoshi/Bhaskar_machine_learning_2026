# ## Calculate Hypotense
# ### 🧠 Topic: **Calculate Hypotenuse**
# #### 📘 Understanding the Terms (in simple language):
# When you have a right-angled triangle (a triangle where one of the angles is exactly 90 degrees), the longest side of the triangle is called the **hypotenuse**. It’s the side that is **opposite the right angle**.
# The other two sides (the ones that make the right angle) are usually called the **base** and the **height** (or **perpendicular**).
# To calculate the length of the hypotenuse, we use something called the **Pythagorean Theorem**.
# The formula is:
# ```
# hypotenuse² = base² + height²
# ```
# To find the hypotenuse, we need to take the square root of the sum of the squares of the base and height:
# ```
# hypotenuse = √(base² + height²)
# ```
# #### 🔧 Task:
# Write a function named `calculate_hypotenuse` that takes two arguments:
# * `base`: the length of the base (a number)
# * `height`: the length of the height/perpendicular side (a number)
# It should return the length of the hypotenuse (a number).
# Use the formula:
# ```
# hypotenuse = (base² + height²) ** 0.5
# ```
# #### 💡 Examples:
# ```python
# Input: calculate_hypotenuse(3, 4)
# Output: 5.0
# ```
# Why?
# Because √(3² + 4²) = √(9 + 16) = √25 = 5.0
# ---
# ```python
# Input: calculate_hypotenuse(5, 12)
# Output: 13.0
# ```
# Why?
# Because √(25 + 144) = √169 = 13.0
# ---
# ```python
# Input: calculate_hypotenuse(0, 0)
# Output: 0.0

def calculate_hypotenuse(base, height):
    
    hypotenuse = (base**2+ height **2) **0.5
    # print(type(hypotenuse))
    # print(type(base))
    # print(type(height))
    return f' The calculated hypotenuse is : {hypotenuse}'


print(calculate_hypotenuse(3, 4.0))
print(calculate_hypotenuse(5, 12))
print(calculate_hypotenuse(5.0, 12.0))
print(calculate_hypotenuse(0, 0))