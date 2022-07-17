# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('enter N: '))

if number < 0:
    number = number * -1

list_of_nums = [1]
for i in range(1,number):
    list_of_nums.append(list_of_nums[i-1] * (i+1))
print(list_of_nums)

