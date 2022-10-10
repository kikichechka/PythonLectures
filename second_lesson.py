from random import randint
from random import shuffle
separator = '\n************'

# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
print(separator)
data1 = input('Введите многозначное число: ')
sum = 0

for i in data1:
    if i.isdigit():
        sum += int(i)
print(f'Сумма цифр вещественного числа {data1} равна {sum}.')

# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
print(separator)
data2 = int(input('Введите число: '))
lst = []
factorial = 1

for i in range(1, data2 + 1):
    factorial *= i
    lst.append(factorial)
print(lst)

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
print(separator)
data3 = int(input('Введите число: '))
count = 1
sum3 = 0
dict = {}

while count <= data3:
    dict[count] = round((1 + 1/count) ** count, 2)
    count += 1
else:
    print(dict)

for i in dict:
    sum3 += dict[i] 
print(f'Сумма значений равна {sum3}')


# # Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
print(separator)
data4 = int(input('Введите число: '))
entered_list = []
list_data_from_file = []
final_list = []

for i in range(-data4, data4 + 1):
    entered_list.append(i)
print(entered_list)

with open('1.txt', 'r') as file:
    data_in_file = file.read()
    list_data_from_file = data_in_file.split()
list_data_from_file = [int(item) for item in list_data_from_file]

print(list_data_from_file)

for f in list_data_from_file:
    for l in entered_list:
        final_list.append(f * l)
print(final_list)


# Реализуйте алгоритм перемешивания списка.
print(separator)
start_list = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый']
my_final_list = []

#1-й способ
shuffle(start_list)
print(start_list)

#2-й способ
while len(start_list) > 0:
    i = randint(0, len(start_list) - 1)
    my_final_list.append(start_list[i])
    del start_list[i]
else:
    print(my_final_list)
