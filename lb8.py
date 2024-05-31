x = float(input())

i_max = 500
c = x
summa = c
i = 1
eps = 0.001

while abs(c) > eps and i < i_max:
    dl = ((4 * i ** 2 - 2 * i) / (4 * i ** 2 - 2 * i - 6)) * x ** (2 * i + 1)
    c *= dl
    summa += c
    i += 1

print(summa, i)
last_form = 2 * (1 + x) ** 0.5 - 2
print(abs(last_form - summa), last_form)
