import math

# 1
# for x in range(-500, 501):
#     if abs(x) / 100 >= 1 and 200 <= abs(x) <= 299 or 400 <= abs(x) <= 499:
#         print(x)

# 2
# N = int(input())
# i1 = 1
# i2 = 1
# while N > i2:
#     fibI = i1 + i2
#     i2 = i1
#     i1 = fibI
#     print(i2)

# 3
n = int(input())


def y(n):
    if n < 3:
        return 0
    if n >= 3:
        return 1 / (abs(y(n - 3) + math.sin(y(n - 1)) ** 2 + math.cos(y(n - 2)) ** 2)) ** 0.5

print(y(n))
