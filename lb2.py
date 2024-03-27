import math
#1
# def main():
#     print("Введите x y")
#     try:
#         x = int(input())
#         y = int(input())
#         R = 3
#         a = 2
#         b = 1
#         if (x-a)**2 + (y-b)**2 <= R**2:
#             print("она лежит внутри окружности")
#         elif (x-a)**2 + (y-b)**2 > R**2:
#             print("она лежит снаружи окружности")
#     except ValueError:
#         print("Только целые числа")
#         main()
#
# if __name__ == '__main__':
#     main()
#2
# def main():
#     try:
#         print("Введите d")
#         d = int(input())
#         d1 = None
#         if d > 4: d1 = d + 3
#         elif d == 4: d1 = d**2 - math.sin(d)
#         else: d1 = 4*d**3-1
#         print(d1)
#
#     except ValueError:
#         print("Только целые числа")
#         main()
#
# if __name__ == '__main__':
#     main()
#3
def main():
    try:
        print("Введите x")
        x = int(input())
        y = None
        if x <= -5: y = -3
        elif -5 <= x <= -3: y = x + 3
        elif -3 <= x <= 3: y = (9-x**2)**0.5
        elif 3 <= x <= 8: y = 0.6*x-1.8
        elif 8 <= x: y = 3
        print(y)


    except ValueError:
        print("Только целые числа")
        main()

if __name__ == '__main__':
    main()
