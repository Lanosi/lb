# 1
# word = str(input())
# print(word[0] == word[-1])

# 2
# word = str(input())
# print("++++"+word+"-----")

# 3
# s = str(input())
# s0 = str(input())
# print(s.count(s0))

# 4
# word = str(input())
# number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# cnt = 0
# for i in word:
#     if i in number:
#         cnt += 1
# print(cnt)
#Сдал


#5
Xstring = input("Введите строку вида <цифра>±<цифра>±...")
summ = int(Xstring[0])  # первая цифра

for i in range(1, len(Xstring), 2):
    if Xstring[i] == '+':
        summ += int(Xstring[i + 1])
    elif Xstring[i] == '-':
        summ -= int(Xstring[i + 1])

print(f"Результат: {summ}")


