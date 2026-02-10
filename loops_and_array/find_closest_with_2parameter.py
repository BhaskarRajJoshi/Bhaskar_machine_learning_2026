
def sq_distance(o1, o2):
    x1, y1 = o1
    x2, y2 = o2

    return (x2-x1)**2+(y2-y1)**2


def ab_distance(o1, o2):
    x1, y1 = o1
    x2, y2 = o2

    return abs((x2 - x1) + (y2 - y1))


def find_closest(x_new, x, y, distance=sq_distance):
    minimum1 = 'None'
    closest = 'None'
    for i, xx in enumerate(x):
        dist = distance(x_new, xx)
        if minimum1 == 'None' or dist < minimum1:
            minimum1 = dist
            closest = i
    return y[closest]


print(find_closest([2, 10], [[1, 2], [2, 4], [3, 10]], [1000, 2000, 5000]))
print(find_closest([6, 1], [[1, 2], [2, 4], [3, 10]], [1000, 2000, 5000], ab_distance))
