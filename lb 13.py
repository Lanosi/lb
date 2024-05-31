# 1
import math


def calculate_expression1(x):
    return abs(x - math.pi) * (math.e ** (3 * x))


def calculate_expression2(x):
    return math.log((1.7 * (x ** (1 / 3))) + (x * x ** (1 / 2)))


def main():
    x = float(input("Введите значение x: "))
    result = calculate_expression1(x) / calculate_expression2(x)
    print(result)


if __name__ == '__main__':
    main()

# 2
def main():
    x = float(input("Введите значение x: "))
    first_calculation = polynomial_expression1(x)
    second_calculation = polynomial_expression2(x)
    t = 1 + first_calculation / second_calculation
    print(t)


def polynomial_expression1(x):
    return 1 + x - 2 * x ** 2 + 3 * x ** 3 - 4 * x ** 4


def polynomial_expression2(x):
    return (x - 0.5) - 2 * (x - 0.5) ** 2 + 3 * (x - 0.5) ** 3 - 4 * (x - 0.5) ** 4


if __name__ == '__main__':
    main()

# 3
import math


def f1(x, a, b, z):
    return a + z * math.cos(2 * (b * x) ** 3)


def f2(x, a, b, z):
    return a + math.sin(x) ** 2 * (b / 2) + math.log(z * x)


def f3(x, a, b, z):
    return ((0.3 * b) + (abs(b) * a - z / 2 - math.cos(x)) ** 0.5) ** (1 / 3)


def main():
    x, a, b = map(int, input("Введите x a b: ").split())
    z = math.log(abs(b * x))

    if x < a:
        y = f1(x, a, b, z)
    elif a <= x <= b:
        y = f2(x, a, b, z)
    else:
        y = f3(x, a, b, z)

    print(y)


if __name__ == '__main__':
    main()
