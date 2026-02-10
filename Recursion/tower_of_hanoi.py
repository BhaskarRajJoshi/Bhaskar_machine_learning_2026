# # ## Tower of hanoi using recursion.
# # **Topic:** *Tower of Hanoi (Recursion)*
# # **Explanation:** You have three pegs: **A** (source), **B** (auxiliary), and **C** (target).
# # A stack of discs sits on **A**, smallest on top. You must move the whole stack to **C** by moving one disc at a time and
# # never placing a larger disc on a smaller one.
# # Recursion idea:
# # * For **1 disc**: move disc 1 from **A** to **C**.
# # * For **2 discs**: move disc 1 from **A**→**B**, move disc 2 from **A**→**C**, move disc 1 from **B**→**C**.
# # * For **3 discs**: first solve the 2-disc problem **A**→**B**, then move disc 3 **A**→**C**, then solve the 2-disc problem **B**→**C**.
# # General rule for **n**:
# # 1. Move **n−1** discs from **source** to **auxiliary**, 2) move disc **n** from **source** to **target**, 3) move **n−1** discs
# # from **auxiliary** to **target**.
# # **Exercise:**
# # Write a function `solve_hanoi(n, source='A', auxiliary='B', target='C')` that:
# # * Prints each move exactly in the format: `Moving <disc> from <source> to <target>.`
# # * Uses recursion: base case `n == 1`, recursive case for `n > 1` using the general rule above.
# # * Returns the **total number of moves** performed.
# # **Example:**
# # ```python
# # # 1 disc
# # solve_hanoi(1)
# # # Output:
# # # Moving 1 from A to C.
# # # Returns: 1
# # ```
# # ```python
# # # 2 discs
# # solve_hanoi(2)
# # # Output:
# # # Moving 1 from A to B.
# # # Moving 2 from A to C.
# # # Moving 1 from B to C.
# # # Returns: 3
# # ```
# #
# # ```python
# # # 3 discs
# # solve_hanoi(3)
# # # Output:
# # # Moving 1 from A to C.
# # # Moving 2 from A to B.
# # # Moving 1 from C to B.
# # # Moving 3 from A to C.
# # # Moving 1 from B to A.
# # # Moving 2 from B to C.
# # # Moving 1 from A to C.
# # # Returns: 7
# # ```
#
# def move_1st_disk(disks, source, target):
#     print(f'Moving disk {disks} from Tower {source} to {target}')
# def move_2nd_disk(disks, source, auxi):
#     print(f'Moving disk {disks} from Tower {source} to {auxi}')
#
#
#
# def solve_hanoi(n):
#     if n == 1:
#         return move_1st_disk(1, 'A', 'C')
#     elif n == 2:
#         move_2nd_disk(1, 'A', 'B')
#         move_1st_disk(2, 'A', 'C')
#         move_1st_disk(1, 'B', 'C')
#     elif n == 3:
#         move_1st_disk(1, 'A', 'C')
#         move_2nd_disk(2, 'A', 'B')
#         move_2nd_disk(1, 'C', 'B')
#         move_1st_disk(3, 'A', 'C')
#         move_1st_disk(1, 'B', 'A')
#         move_1st_disk(2, 'B', 'C')
#         move_1st_disk(1, 'A', 'C')
#
#
# print(solve_hanoi(3))
#
# def solve_hanoi(n, source='A', auxi='B', target='C'):
#     if n == 1:
#         print(f'Moving disk {n} from {source} to {target}')
#         return 1
#     if n == 2:
#         print(f'Moving disk {n} from {source} to {auxi}')
#
# tower of hanoi
# def solve(disks, source, target, aux, tab=''):
#     print(f'solve({disks}, {source}, {target}, {aux})')
#     if disks == 1:
#         print(f"Move 1 from {source} to {target}")
#     elif disks == 2:
#         print(f'Move 1 from {source} to {aux}')
#         print(f'Move 2 from {source} to {target}')
#         print(f'Move 1 from {aux} to {target}')
#
#     elif disks == 3:
#         solve(2, source, aux, target)
#         print(f'Moving 3 from {source} to {target}')
#         solve(2, aux, target, source)
#     else:
#         solve(disks - 1, source, aux, target)
#         print(f'Moving {disks} from {source} to {target}')
#         solve(disks - 1, aux, target, source)
#     return



# def solve(disks, source, target, aux, tab=''):
#     print(f'{tab}>> solve({disks}, {source}, {target}, {aux})')
#     if disks == 1:
#         print(f"{tab}Move 1 from {source} to {target}")
#     else:
#         solve(disks-1, source, aux, target, tab + '  ')
#         print(f'{tab}Moving {disks} from {source} to {target}')
#         solve(disks-1, aux, target, source, tab + '  ')
# tower of hanoi

def solve(disks, source, target, aux, tab=''):
    steps = 0
    if disks > 0:
        print(f'{tab}>> solve({disks}, {source}, {target}, {aux})')
        steps += solve(disks-1, source, aux, target, tab + '  ')
        print(f'{tab}Moving {disks} from {source} to {target}')
        steps += 1
        steps += solve(disks-1, aux, target, source, tab + '  ')
    return steps


print(solve(4, 'A', 'C', 'B'))