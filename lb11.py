#1
# import numpy as np
#
# array = np.array([
#     [1, -2, 3],
#     [4, -5, 6],
#     [7, -8, 9],
#     [10, -11, 12],
#     [13, -14, 15],
#     [16, -17, 18]
# ])
#
# size = 10
# count = 0
#
# for i in range(array.shape[0]):
#     row_sum = np.sum(array[i, :])
#     if abs(row_sum) > size:
#         print(f"Строка {i+1} превышает пороговое значение с суммой: {row_sum}")
#         count += 1
#
# print(f"Количество строк, превышающих пороговое значение: {count}")

#2
# import numpy as np
#
# array = np.random.randint(-10, 10, size=(7, 3))
#
# size = 7
#
# found_valid_row = False
#
# for i in range(array.shape[0]):
#     exceeded = False
#     for j in range(array.shape[1]):
#         for k in range(j + 1, array.shape[1]):
#             if abs(array[i, j] - array[i, k]) > size:
#                 exceeded = True
#                 break
#         if exceeded:
#             break
#     if not exceeded:
#         print(f"Сумма элементов строки {i + 1}: {np.sum(array[i, :])}")
#         found_valid_row = True
#     else:
#         break
#
# if not found_valid_row:
#     print("Ни одна строка не удовлетворяет условию.")

#3
import numpy as np

# Заданный массив C1, C2, ..., Cn
C = np.array([1, 2, 3])

# Создаем двумерный массив
array = np.array([
    [1, 0, 3],
    [0, 5, 6],
    [7, 0, 9]
])

# Находим индексы элементов главной диагонали
diag_indices = np.diag_indices(min(array.shape))

# Находим сумму элементов главной диагонали
diag_sum = np.sum(array[diag_indices])

# Изменяем столбцы массива, удовлетворяющие условию
for i in range(array.shape[1]):
    if array[i, i] == 0:
        array[:, i] += C[0]

print("Измененный массив:")
print(array)
print("Сумма элементов главной диагонали:", diag_sum)
