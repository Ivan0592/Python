# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.



a = int(input('Введите: n '))
d = int(input('Введите: a '))
n = int(input('Введите: d ')) 
progressive = [a + (i - 1) * d for i in range(1, n + 1)] 
print(*progressive)