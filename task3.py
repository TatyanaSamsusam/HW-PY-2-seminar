# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# *Пример:*
# Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

n = int(input('введите натуральное число: '))
lst = []
for i in range(1, n+1):
    lst.append((1+1/i)**i)

print(lst)
