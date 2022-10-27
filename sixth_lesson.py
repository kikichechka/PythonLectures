
from random import randint

# coefficients = []
# extent = int(input('Введите степерь многочлена: '))
# for i in range(extent + 1):
#     num = randint(-10, 10)
#     if num != 0:
#         coefficients.append(num)
# print(coefficients)
# resul = []
# for i in range(len(coefficients)):
#     if coefficients[i] == -1 and extent - i != 0:
#         st = ('-X^' + str(extent - i))
#     elif coefficients[i] != 0 and extent - i == 0:
#         st = (str(coefficients[i]))
#     elif coefficients[i] == 1 and extent - i == 1:
#         st = ('X')
#     elif coefficients[i] != 0 and extent - i == 1:
#         st = (str(coefficients[i]) + 'X')
#     else:
#         st = (str(coefficients[i]) + 'X^' + str(extent - i))
#     if '-' not in st and i > 0:
#         resul.append('+')
#     resul.append(st)
# resul.append(str('= 0'))
# print(*resul)
# with open('4.txt', 'w') as file:
#         file.writelines(resul)

extent = int(input('Введите степерь многочлена: '))
coefficients = [randint(-10, 10) for _ in range(extent + 1)]
print(coefficients)
resul = []

for i, coefficient in enumerate(coefficients):
    if coefficient != 0:
        if coefficient == -1 and extent - i != 0:
            st = ('-X^' + str(extent - i))
        elif coefficient != 0 and extent - i == 0:
            st = (str(coefficient))
        elif coefficient == 1 and extent - i == 1:
            st = ('X')
        elif coefficient == 1 and extent - i > 1:
            st = ('X^' + str(extent - i))
        elif coefficient != 0 and extent - i == 1:
            st = (str(coefficient) + 'X')
        else:
            st = (str(coefficient) + 'X^' + str(extent - i))
        if '-' not in st and i > 0 and resul:
            resul.append('+')
        resul.append(st)

resul.append(str('= 0'))
print(*resul)


# def fun3(l):
#     l_2 = set(l)

#     for i in l:
#         if i not in l_2:
#             l.remove(i)
#     return l
# print(fun3(lst))
# list_1 = [randint(0,100) for i in range (10)]
# print('Исходный список ', list_1)
# new_list =[]
# [new_list.append(i) for i in list_1 if i not in new_list ]
# print('Список без повторных элементов ', new_list)

lst = [1, 45, 99, 34, 99, 1, 101, 65]
fun3 = list(filter(lambda x: lst.count(x) == 1, lst))
print('Исходный список ', lst)
print(f'Cписок неповторяющихся элементов: {fun3}')


# def recovery(file_name):
#     with open(file_name, 'r') as file:
#         data_in_file = list(file.read())

#     print(data_in_file)

#     num = tuple(data_in_file[i] for i in range(len(data_in_file)) if i%2 == 0)
#     equal = tuple(data_in_file[i] for i in range(len(data_in_file)) if i%2 != 0)
#     data = list(zip(num, equal))
#     encoding = ''
#     num = 0

#     for value in data_in_file:
#         if value.isdigit():
#             num = int(value)
#         else:
#             encoding += value*num
#     return encoding

# print(recovery('3.txt'))

def multiply(x, y):
  return x*y

def recovery(file_name):
    with open(file_name, 'r') as file:
        data_in_file = list(file.read())
    num = list(int(data_in_file[i]) for i in range(len(data_in_file)) if i%2 == 0)
    equal = tuple(data_in_file[i] for i in range(len(data_in_file)) if i%2 != 0)
    result = map(multiply, num, equal)
    print(*result, sep='')

recovery('3.txt')
