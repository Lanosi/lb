import math

def main():
    try:
        a, b = 1 , 2.9
        print("Введите h")
        h = float(input())
        x = a
        k = int((b-a)/h)+1
        for i in range(k):
            y = 0.5 * x ** 2 - 1 - math.log10(abs(x - 3))
            print(x, y)
            x += h

    except ValueError:
        print("Только числа")
        main()

if __name__ == '__main__':
    main()




