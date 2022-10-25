
from itertools import count
from random import randint


#1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

lst = ('абв синий красный абвгдейка зеленый')
lst2 = list(x for x in lst.split() if 'абв' not in x)
print(lst2)

#2 Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

flag = True if randint(0, 1) == 0 else False
candyes = 2021
move = 28

def move_man():
    while True:
            man = int(input('\nВаш ход: '))
            if 0 < man <= move:
                return man 
            else:
                print('Не жульничайте 😸. Взять нужно от 1-й до 28-ми конфет.')

def move_bot():
    return randint(1, move)

def play(candyes, flag):
    print('******* Игра в конфеты ********\nВзять можно до 28 конфет за раз.')
    while True:
        if flag:
            candyes -= move_man()
            print(f'Осталось {candyes} конфет')
            flag = False
        else:
            b = candyes - (move + 1) if move*2 >= candyes >= move + 1 else move_bot()
            candyes -= b
            print(f'\nБот взял {b} конфет.\nОсталось {candyes} 🍭🍬')
            flag = True

        if candyes <= move:
            print('Конец игры!', end= ' ')
            print('Вы выигрыли🎉✨') if flag else print('Вы проигрыли☹')
            break

while True:     
    print("\033[H\033[J")
    play(candyes, flag)
    repeat = int(input('Повторить игру?(да - 1, нет - 0):'))
    if repeat == 1:
        play(candyes, flag)  
    else: break

#3 Создайте программу для игры в ""Крестики-нолики"".

tic_tac_toe = [['•', '•', '•'], ['•', '•', '•'], ['•', '•', '•']]
man = 'x'
bot = '0'

def print_field(tic_tac_toe):
    print('  1   2   3')
    for i in range(len(tic_tac_toe)):
        print(i + 1, end= ' ')
        print(*tic_tac_toe[i], sep=' | ')
        print(' -----------')

def move_man_play_tic_tac_toe(tic_tac_toe):
    while True:
        x,y = map(int,input('Ваш ход. Введите координаты через пробел: ').split())       
        if 1 <= x <= 3 and 1 <= x <= 3 and '•' in tic_tac_toe[y - 1][x - 1]:
            tic_tac_toe[y - 1][x - 1] = 'x'
            break

def move_bot_play_tic_tac_toe(tic_tac_toe):
    for i in range(len(tic_tac_toe)):
        for j in range(0, 3):
            if '•' in tic_tac_toe[i][j]:
                tic_tac_toe[i][j] = '0'
                if check(bot) == 2:
                    print_field(tic_tac_toe)
                    return
                else: 
                    tic_tac_toe[i][j] = '•'

    for i in range(len(tic_tac_toe)):
        for j in range(0, 3):
            if '•' in tic_tac_toe[i][j]:
                tic_tac_toe[i][j] = 'x'
                if check(man) == 2:
                    tic_tac_toe[i][j] = '0'
                    print_field(tic_tac_toe)
                    return
                else: 
                    tic_tac_toe[i][j] = '•'

    while True:
        lst = [randint(0, 2) for _ in range(2)]
        if '•' in tic_tac_toe[lst[0]][lst[1]]:
            tic_tac_toe[lst[0]][lst[1]] = '0'
            print_field(tic_tac_toe)
            break

def check(player): 
    if tic_tac_toe[0].count(player) == 3: return 2
    if tic_tac_toe[1].count(player)== 3: return 2
    if tic_tac_toe[2].count(player) == 3: return 2
    if '•' not in [element for a_list in tic_tac_toe for element in a_list]: return 1
    if tic_tac_toe[0][0] == player and tic_tac_toe[1][1] == player and tic_tac_toe[2][2] == player: return 2
    if tic_tac_toe[0][2] == player and tic_tac_toe[1][1] == player and tic_tac_toe[2][0] == player: return 2
    if tic_tac_toe[0][0] == player and tic_tac_toe[1][0] == player and tic_tac_toe[2][0] == player: return 2
    if tic_tac_toe[0][1] == player and tic_tac_toe[1][1] == player and tic_tac_toe[2][1] == player: return 2
    if tic_tac_toe[0][2] == player and tic_tac_toe[1][2] == player and tic_tac_toe[2][2] == player: return 2
    return 0

def play_tic_tac_toe():
    print('******* Крестики❌ нолики⭕ ********')
    while True:
        move_man_play_tic_tac_toe(tic_tac_toe)
        if check(man) == 1:
            print_field(tic_tac_toe)
            print('Конец игры! Ничья.')
            break
        if check(man) == 2:
            print_field(tic_tac_toe)
            print('Конец игры! Поздравляем, Вы выиграли👏🎉🥇.')
            break

        move_bot_play_tic_tac_toe(tic_tac_toe)
        if check(bot) == 1:
            # print_field(tic_tac_toe)
            print('Конец игры! Ничья.')
            break
        if check(bot) == 2:
            # print_field(tic_tac_toe)
            print('Конец игры! К сожалению Вы проиграли😿.')
            break

while True:     
    print("\033[H\033[J")
    play_tic_tac_toe()
    repeat2 = int(input('Повторить игру?(да - 1, нет - 0):'))
    if repeat2 == 0:
        break

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

def compression(file_name):
    with open(file_name, 'r') as file:
        data_in_file = list(file.read())

    element = data_in_file[0]
    encoding = ''
    coun = 0
    for i in data_in_file:
        if element == i:
            coun += 1
        else:
            encoding += str(coun) + element
            element = i
            coun = 1
    encoding += str(coun) + element
    return encoding


def recovery(file_name):
    with open(file_name, 'r') as file:
        data_in_file = list(file.read())
    encoding = ''
    num = 0
    for value in data_in_file:
        if value.isdigit():
            num = int(value)
        else:
            encoding += value*num
    return encoding


print(compression('2.txt'))
print(recovery('3.txt'))



