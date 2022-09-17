# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


k = int(input("Введите число: "))

while k >= 0:
     num = random.randint(0, 100)
     if num == 0 and k == 0:
        print(" = 0")
     elif num == 0:
         k -= 1
         continue
     if k == 0:
        print(f"{num} = 0")
     elif k == 1:
        print(f"{num}x + ", end= "")
     else:
        print(f"{num}x**{k} + ", end= "")
     k -= 1