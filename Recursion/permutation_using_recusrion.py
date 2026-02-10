# def permutation(x):
    # if len(x) == 1:
    #     print(x)
    # if len(x) == 2:
    #     for i in
    #     print(x)
    #     print(x[::-1])
    # if len(x) == 3:
    #     print(x)
    #     print(x[::-1])
    # for i in





# print(permutation('abc'))
letters = ['a', 'b', 'c']

# 1. Pick the first letter
for i in range(3):
    first = letters[i]

    # 2. Pick the second letter (but it can't be the same as the first!)
    for j in range(3):
        if j == i:
            continue  # Skip if we already used this letter
        second = letters[j]

        # 3. Pick the third letter (can't be the same as first or second!)
        for k in range(3):
            if k == i or k == j:
                continue  # Skip if already used
            third = letters[k]

            # Print the result
            print(first + second + third)