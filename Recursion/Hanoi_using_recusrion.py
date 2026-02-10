# ## Tower of hanoi using recursion.
# **Topic:** *Tower of Hanoi (Recursion)*
# **Explanation:** You have three pegs: **A** (source), **B** (auxiliary), and **C** (target).
# A stack of discs sits on **A**, smallest on top. You must move the whole stack to **C** by moving one disc at a time and
# never placing a larger disc on a smaller one.
# Recursion idea:
# * For **1 disc**: move disc 1 from **A** to **C**.
# * For **2 discs**: move disc 1 from **A**→**B**, move disc 2 from **A**→**C**, move disc 1 from **B**→**C**.
# * For **3 discs**: first solve the 2-disc problem **A**→**B**, then move disc 3 **A**→**C**, then solve the 2-disc problem **B**→**C**.
# General rule for **n**:
# 1. Move **n−1** discs from **source** to **auxiliary**, 2) move disc **n** from **source** to **target**, 3) move **n−1** discs
# from **auxiliary** to **target**.
# **Exercise:**
# Write a function `solve_hanoi(n, source='A', auxiliary='B', target='C')` that:
# * Prints each move exactly in the format: `Moving <disc> from <source> to <target>.`
# * Uses recursion: base case `n == 1`, recursive case for `n > 1` using the general rule above.
# * Returns the **total number of moves** performed.
# **Example:**
# ```python
# # 1 disc
# solve_hanoi(1)
# # Output:
# # Moving 1 from A to C.
# # Returns: 1
# ```
# ```python
# # 2 discs
# solve_hanoi(2)
# # Output:
# # Moving 1 from A to B.
# # Moving 2 from A to C.
# # Moving 1 from B to C.
# # Returns: 3
# ```
#
# ```python
# # 3 discs
# solve_hanoi(3)
# # Output:
# # Moving 1 from A to C.
# # Moving 2 from A to B.
# # Moving 1 from C to B.
# # Moving 3 from A to C.
# # Moving 1 from B to A.
# # Moving 2 from B to C.
# # Moving 1 from A to C.
# # Returns: 7
# ```

# def move_disk(start, end):
#     tower= ['A', 'B', 'C']
#     print(f' Moving from {start} to {end}.')
#
#
# def solve_hanoi(n, start=1, end=3):
#     if n == 1:
#         return move_disk(start, end)
#     else:
#         other = 6 - (start + end)
#         solve_hanoi(n -1, start, other)
#         move_disk(start, end)
#         solve_hanoi(n-1, other, end)
#
#
# print(solve_hanoi(3))


def solve_hanoi(n, source='A', auxiliary='B', target='C'):
    # Base Case: Only one disc to move
    if n == 1:
        print(f"Moving 1 from {source} to {target}.")
        return 1

    # Step 1: Move n-1 discs from source to auxiliary
    # We "hit" the code again here
    count1 = solve_hanoi(n - 1, source, target, auxiliary)

    # Step 2: Move the largest disc (n) from source to target
    print(f"Moving {n} from {source} to {target}.")
    current_move = 1

    # Step 3: Move the n-1 discs from auxiliary to target
    count2 = solve_hanoi(n - 1, auxiliary, source, target)

    # Return the total sum of moves
    return count1 + current_move + count2


# Testing with 3 discs
total_moves = solve_hanoi(2)
print(f"Returns: {total_moves}")

