# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
n = 10
init_lst = [random.randint(1,10) for i in range(n)]
print(init_lst)

def second_item(lst):
        if lst[1] == 1:
            return lst[1]
            
l = list(filter(second_item, [(init_lst[i], init_lst.count(init_lst[i])) for i in range(len(init_lst))]))

print([j[0] for j in l])