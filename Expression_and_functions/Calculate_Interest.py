## Calculate Interest

### **Topic:** *Calculate Interest*

#### **Explanation:**
# When someone deposits or borrows money, the amount often grows over time due to *interest*. There are two common types of interest: **Simple Interest** and **Compound Interest**.
# In this exercise, we'll focus on **Simple Interest**.

# * **Principal (P):** The original amount of money deposited or borrowed.
# * **Rate of Interest (R):** The percentage charged or earned on the principal each year.
# * **Time (T):** The number of years the money is deposited or borrowed for.

# The formula to calculate **Simple Interest** is:

# Interest = (Principal × Rate × Time) / 100
# This gives us the amount of money earned or paid as interest after the given time.

#### **Problem Statement:**

# Write a function named `calculate_interest` that takes the following three arguments:

# * `principal` (amount of money deposited or borrowed),
# * `rate` (rate of interest per year, as a percentage),
# * `time` (duration in years),

# and returns the simple interest calculated using the formula above.

#### **Example Usage:**

# calculate_interest(1000, 5, 2)   # Output: 100.0
# calculate_interest(1500, 4.3, 3) # Output: 193.5
# calculate_interest(500, 10, 0)   # Output: 0.0

def calculate_interest(principal,rate,time):
    interest= (principal * rate * time) / 100
    
    return f'The calculated intereset is :{interest}'


print(calculate_interest(1000, 5, 2) )  # Output: 100.0
print(calculate_interest(1500, 4.3, 3) ) # Output: 193.5
print(calculate_interest(500, 10, 0) )  # Output: 0.0  
