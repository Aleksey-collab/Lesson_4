# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)


num = int(input("До какого числа после запятой вывести число Пи "))
PI = (1/16**0) * (4/(8 * 0 + 1) - 2/(8 * 0 +4) - 1/(8 * 0 + 5) - 1/(8 * 0 + 6))

for k in range(1, num):
    PI += (1/16**k) * (4 / (8 * k + 1) - 2 / (8 * k +4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
print(PI)
print(round(PI, num))