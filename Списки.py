# category = ["Drama", "Comedy", "Fantasy", "24", 24]
#
# print(category)
# print(len(category))
# for cat in category:
#     print(cat)
# print("Drama" in category)
# print("Races" in category)
#import random

# numbers = [i ** 2 for i in range(0, 10) if i ** 2 % 2 == 0]
# print(numbers)

#24.07.23

# numbers = [i for i in "Python"]
# for i in range(len(numbers)):
#     if numbers[i] == 'y':
#         numbers[i] += input()
# numbers += '+'
# print(numbers)
# print(len(numbers))
# #print(max(numbers))
# print(min(numbers))
# print(sorted(numbers))


# numbers =[(i ** 2 if i % 2 else i ** 2) for i in range(9, -1, -1)]
# print(numbers)
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# numbers += 'a'
# numbers += ['abcd']
# numbers += (['b'] * 5)
# numbers += [['a', 6, '+']]
# numbers = ['a'] + numbers
# print(numbers)
# #print(sorted(numbers, reverse=True))
# print(numbers[9:3:-1])


# numbers = list()
# counter = 0
# for i in range(5):
#     numbers += [int(input(f'Введите {i + 1}е значение: '))]
# print(numbers)
# n = int(input("Введите число для поиска: "))
# for number in numbers:
#     if n == number:
#         counter += 1
# print(f' Количество {n} в списке: {counter}')

# посчитать сумму и среднеарифметическое
# введенных пользователям чисел списка
# numbers = list()
# for i in range (5):
#     numbers += [int(input(f'Введите {i + 1}е значение: '))]
# print(numbers)
# print("Среднее арифметическое")
# print(sum(numbers) / len(numbers ) )


# numbers = [i ** 2 for i in range(0, 10)]
# print(numbers)
# numbers.insert(len(numbers), [56, 17])
# print(numbers)
# print(len(numbers))
# numbers.pop()
# print(numbers)
# numbers.clear()
# print(numbers)
# numbers += [9]
# print(numbers)
# numbers.reverse()
# print(numbers.index(9))
# print(numbers.sort())
# print(numbers)

#26.07.2023

# В списке целых, заполненном случайными числами,
# вычислить
# * Сумму отрицательных чисел
# * Сумму четных чисел
# * Сумму нечетных чисел
# * Произведение элементов с индексами кратными 3;
# * Произведение элементов между минимальным и максимальным элементом;
# * Сумму элементов находящихся между первым ипоследним
# положительными элементами

#import random
# from random import randint
#
# numbers = [randint(-100, 100) for _ in range(10)]
# sum_neg = sum([el for el in numbers if el < 0])
# sum_even = sum([el for el in numbers if el % 2 == 0])
# sum_odd = sum([el for el in numbers if el % 2])
# mult_3 = 1
# for i in range(0, len(numbers), 3):
#     mult_3 *= numbers[i]
# print(f'Сумма отрицательных: {sum_neg}')
# print(f'Сумма четных: {sum_even}')
# print(f'Сумма нечетных: {sum_odd}')
# print(f'Произведение кратных 3: {mult_3}')
# max_id = 0
# min_id = 0
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[max_id]:
#         max_id = i
#     if numbers[i] < numbers[min_id]:
#         min_id = i
# mult_min_max = 1
# if min_id < max_id:
#     for i in range(min_id + 1, max_id):
#         mult_min_max *= numbers[i]
# elif min_id > max_id:
#     for i in range(max_id + 1, min_id):
#         mult_min_max *= numbers[i]
# else:
#     mult_min_max =0
# print(f'Значение между min и max: {mult_min_max}')


# list1 = [1, 2, 3, 4, 5]
# print(list1)
# list2 = list1
# list2[1] = 'Hello'
# print(list2)
# print(list1)
# list2[5][0] = "World"
# print(list2)
# print(list1)
#
# for el in list2:
#     print(type(el))
#     if isinstance(el, list):
#         print(True)
#
# for i in range(len(list1)):
#     if isinstance(list1[i], list):
#         list2[i] = list1[i].copy()
#
# list[5][0] ="World"

# from random import randint
# list = [randint(-100, 100) for _ in range(10)]
# print(list)
# even = ([el for el in list if el % 2 == 0])
# odd = ([el for el in list if el % 2])
# neg = ([el for el in list if el < 0])
# pos = ([el for el in list if el > 0])
# print(even)
# print(odd)
# print(neg)
# print(pos)


# matrix = [['John', 112, 113],['Bob', 222, 223],['Alice', 331], 'QWERTY']
# for i in range(len(matrix)):
#     print(end='| ')
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=' | ')
#     print()


# from random import randint
#
# matrix = [[randint(0, 20) for _ in range(5)] for _ in range(5)]
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         print(matrix[i][j], end='\t')
#     print()
# print()
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if i + j:
#             print(matrix[i][j], end='\t')
# print()
# print()
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if j >= i:
#             print(matrix[i][j], end='\t')
#         else: