#1
# def main():
#     try:
#         print("Введите x,y")
#         x = int(input())
#         y = int(input())
#         if -4 <= x <= -2:
#             if y == 2.5*x+10 or y == x*0: print("На границе")
#             elif y < 2.5*x+10 and y > x*0: print("Внутри")
#             else: print("Внешняя часть")
#         elif -2 <= x <= 0:
#             if y == -2.5*x or y == x*0: print("На границе")
#             elif y < -2.5*x and y > x*0: print("Внутри")
#             else: print("Внешняя часть")
#         elif 0 <= x <= 2:
#             if y == -2.5*x or y == x*0: print("На границе")
#             elif y > -2.5*x and y < x*0: print("Внутри")
#             else: print("Внешняя часть")
#         elif 2 <= x <= 4:
#             if y == 2.5*x-10 or y == x*0: print("На границе")
#             elif y > 2.5*x-10 and y < x*0: print("Внутри")
#             else: print("Внешняя часть")
#         else:
#             print("Внешняя часть")
#
#     except ValueError:
#         print("Только целые числа")
#         main()
#
# if __name__ == '__main__':
#     main()

#2
def main():
    try:
        print("Введите x,y")
        x = int(input())
        y = int(input())
        if -2 <= x <= -1 and 0 <= y <= 2 and y >= (1-(x+1)**2)**0.5: print("M1")
        #if -1 <= x <= 0 and 0 >= y and y <= (1-(x+1)**2)**0.5 and y <= (1-x**2)**0.5: print("M2")
        if 0 >= y and y <= (1 - (x + 1) ** 2) ** 0.5 and y <= (1 - x ** 2) ** 0.5: print("M2")
        #if 0 <= x <= 2 and -1 <= y <= 1 and y**2 <= 1-(x-1)**2 and y**2 > 1 - x **2: print("M3")
        if y ** 2 <= 1 - (x - 1) ** 2 and y ** 2 > 1 - x ** 2: print("M3")
        if y**2 <= 1 - (x+1)**2 and (y+1)**2 <= 1 - x**2 and y**2 > 1 - x**2: print("M4")
        if -2 <= x <= 0 and -2 <= y <= -1 and (y+1)**2 > 1 - x**2: print("M5")


    except ValueError:
        print("Только целые числа")
        main()

if __name__ == '__main__':
    main()
