import math
#1
# summ = 0
# x = int(input())
# for i in range(1,31):
#     summ += math.sin(2 * i + 7)*x / (2 * i - 1)
# print(5 * x + summ)
#
# s = 0
# i = 1
# while i <= 30:
#     s += math.sin(2 * i + 7)*x / (2 * i - 1)
#     i += 1
# print(5 * x + s)

#2
s = 0
for i in range(1, 16):
    for j in range(1, 9):
        s += math.sin(math.pi/i/j)/math.factorial(i)
print(s)


s = 0
for i in range(1, 16):
    j = 1
    while j <= 8:
        s += math.sin(math.pi/i/j)/math.factorial(i)
        j += 1
print(s)


s = 0
i = 1
while i <= 15:
    for j in range(1, 9):
        s += math.sin(math.pi/i/j)/math.factorial(i)
    i += 1
print(s)


s = 0
i = 1
while i <= 15:
    j = 1
    while j <= 8:
        s += math.sin(math.pi/i/j)/math.factorial(i)
        j += 1
    i += 1
print(s)