# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

import time

ns_time = str(time.time_ns()//100)

lst = [1,2,3,4,5,6,7,8,9]
print(lst)

for i in range (0,len(lst)):
    for j in ns_time:
        if int(j) < len(lst):
            lst[i], lst[int(j)] = lst[int(j)],lst[i]
print(lst)