from operator import le
lst_20 = []

# общий список значений = последняя комбинация 1-я в списке
with open('my.txt', 'r') as file:
    for line in file:
        lst_new = [int(item) for item in line.split()]
        lst_20.append(lst_new)
#lst_coincidences = []
# a = 0
# b = 10


def identical_lines(a, b, number): #одинаковое колличество строк
    lst_coincidences = []
    while b <= len(lst_20):
        coun = 0
        for i in range(a, b): # проходы от a до b (от 0 до 10, от 1 до 11, от 2 до 12....)
            for j in lst_20[i]:
                if j == number:
                    coun += 1
        lst_coincidences.append(coun)
        a += 1
        b += 1
    return lst_coincidences

def growth_identical_lines(): #увеличение колличества строк
    a = 0
    b = 10
    number = 1
    while b <= len(lst_20):
        print(f'{b - a} строк: {identical_lines(a, b, number)}')
        b += 1

growth_identical_lines()


#lst_20.reverse()
#print(lst_20)
# m_45 = 10
# number = 1
# print(f'{number}:')
# while m_45 <= 45:
#     lst_coincidence = []
#     coun = 0
#     a = 0
#     while a <= len(lst_20): 
#         for i in range(a,len(lst_20)): 
#             for j in lst_20[i]: 
#                 if j == number: 
#                     coun += 1 
#             if i == a + m_45: 
#                 #print(f'С {a} по {a + 10}: {c oun}')
#                 lst_coincidence.append(coun) 
#                 coun = 0 
#                 break 
#         a += 1 
#     lst_coincidence.sort() 
#     one = lst_coincidence[0] 
#     two = lst_coincidence[-1] 
#     print(f'{m_45} строк: нет {two + 1} и {one - 1}')
    
#     m_45 += 1

