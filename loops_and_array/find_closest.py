def find_closest(x_exp, x, y):
    minimum = None
    closest = None
    for i in range(len(x)):
        xx = x[i][0]
        diff = abs(xx-x_exp)
        if minimum == None:
            minimum = diff
            closest = i
        elif minimum > diff:
            minimum = diff
            closest = i
    return y[closest]


# print(find_closest(1.2, [[1,], [2,], [3,]], [1000, 2000, 5000]))
# print(find_closest(3.1, [[1,], [2,], [3,]], [1000, 2000, 5000]))
print(find_closest(3.5, [[1,], [2,], [3,]], [1000, 2000, 5000]))
# print(find_closest(2.7, [[1,], [2,], [3,]], [1000, 2000, 5000]))
# print(find_closest(1.6, [[1,], [2,], [3,]], [1000, 2000, 5000]))
# print(find_closest(2.5, [[1,], [2,], [3,]], [1000, 2000, 5000]))
# print(find_closest(2.6, [[1,], [2,], [3,]], [1000, 2000, 5000]))
