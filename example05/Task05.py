# 35. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 

data = []
# # ЧТЕНИЕ ДАННЫХ ИЗ ФАЙЛА

for f in range(1, 2+1):
    LESSON_4 = f'new{f}.txt'

    with open(LESSON_4, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
            data.append(line)


res = " + ".join(i for i in data)

# # # СОЗДАНИЕ И ЗАПИСЬ В ФАЙЛ
with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(f'{res}')