import math

# a=math.log10(100)

# print(a)

def mylog10(log,left,right):

    guess = (left+right)/2

    return f'The log of the number {log} is {guess} and value {10**guess}'


a = mylog10(456,2.65600000001,2.6620000001)
print(a)

# Q: What is Log? log10(10) = 1 log10(100) = 2
# log(N) = number of zeros in a number. 2000 -> 3.3
# A**B = N B = logA(N)
# B ** d = N
# d = logB(N)
# B ** logB(N) = N
# log(A*B) = log(A) + log(B) # zeros get added when we are multiplying - 10 * 100 = 1000
#
# c = math.log10(20)

# print(c)
#
# d = math.log10(56)
# print(d)
# #
e= math.log10(456)
print(e)

# e = 10 ** d
#
# print(e)
#
