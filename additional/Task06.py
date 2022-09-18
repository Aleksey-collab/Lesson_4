# Два различных натуральных числа называются дружественными, если первое из них равно сумме делителей второго числа, за исключением самого второго числа,
# а второе равно сумме делителей первого числа, за исключением самого первого числа. Требуется найти все пары дружественных чисел, 
# оба из которых принадлежат промежутку от M до N.
# Входные данные

# В первой строке находятся целые числа M и N(1 ≤ M≤ N≤ 1.000.000).
# Выходные данные

# В каждой строке вывести по паре чисел через пробел. Первое число пары должно быть меньше второго. Строки должны быть отсортированы в порядке возрастания первого числа пары.
#  Если пар дружественных чисел в промежутке нет, вывести "Absent".

def all_divider_sum(n):
    return sum(i for i in range(1, n) if n % i == 0)

def friend_num(lst):
    r = []
    for i in range(len(lst) - 1):
        M = lst[i]
        for j in range(i+1, len(lst)):
            K = lst[j]
            div_M = all_divider_sum(M)
            div_K = all_divider_sum(K)
            if div_M == K and div_K == M :
                r.append((div_M, div_K))
                
    return r
    
start = 200
end = 500

lst = [i for i in range(start,  end)]

result_lst = friend_num(lst)

if result_lst:
    for i in result_lst:
        print(min(i), max(i))
else:
    print('Absent')