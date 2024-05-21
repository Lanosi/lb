import math
from itertools import combinations


# 1
# a = 0.7
# x = -2 * a
# dx = a / 5
# def y(x):
#     if x <= 0: print((8 * a ** 3) / (x ** 2 + 4 * a ** 2))
#     elif x > 0: print(a * (math.e ** (x / a) + math.e ** (-x/a)))
#
# if __name__ == '__main__':
#     y(x)

# 2
# a = 3 * 10 ** 4
# b = 6 * 10 ** 4
# m = 4
# t1 = (a * b) ** 0.5 - m
# t2 = (a * b) ** 0.5
# for k in range(-30,61):
#     f = k ** 3 - 25 * k ** 2 + 50 * k + 1000
#     if t1 < f < t2 or f > m ** 8:
#         print(f)
#Показал

# 3
def main():
    try:
        print("Введите n значений X")
        n = int(input())
        print("Введите X нач")
        Xstart = int(input())
        print("Введите шаг HX")
        Xstep = int(input())

        print("Введите m значений Z")
        m = int(input())
        print("Введите Z нач")
        Zstart = int(input())
        print("Введите шаг HZ")
        Zstep = int(input())

        FinX = Xstart + n * Xstep
        FinZ = Zstart + m * Zstep

        Check = list()

        for x in range(Xstart, FinX+1, Xstep):
            for z in range(Zstart, FinZ+1, Zstep):
                answer = (z / x + x / z - math.pi ** 0.5) / (0.5 + 10.7 ** 1 / 3 + math.atan(x))
                print(answer)
                Check.append(answer)

        print(Check)
    except ValueError:
        print("Только целые числа")
        main()


if __name__ == '__main__':
    main()

#4
# x = 0.1
# while x < 10:
#     if (x - 2) * x ** 1/3 == -1:
#         print(x)
#         break
#     x += 0.1
#     print((x - 2) * x ** 1/3)
