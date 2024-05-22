# 1
n = int(input())


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(n):
    print(fib(i))

# 2
X = [1, -2, 3, -5, -7, 9, 6, -1, 0, 2]
cnt = 0
for i in X:
    if i < 0:
        cnt += 1

for i in range(len(X) - 1):
    if X[i] > 0 and X[i + 1] != 0:
        X[i] /= X[i + 1]
print(f"Количество отрицательных чисел {cnt}")
print(X)

# 3
A = [4, 3, -2, 0, 5, -22]
Mcnt = 0

for i in range(len(A)):
    if A[i] * A[i - 1] > Mcnt:
        Mcnt = A[i] * A[i - 1]
print(Mcnt)

# 4
A = [-2, 4.3, 0, 12, 135]
n = float(input())
for i in range(len(A)):
    if abs(A[i]) < n:
        print(f"номер этого элемента {i}")
        break
else:
    print("такой элемент не найден")
