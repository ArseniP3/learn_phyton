# Вводится строка, состоящая из букв и пробелов. Составить из входящих в нее букв несколько любых их сочетаний
# (слов) любой длины. Каждую букву строки можно использовать неограниченное количество раз.

str_text = 'Abraham Lincoln loves ice cream, I guess.'
str = str_text.lower()
a = str[0]
b = str[1]
c = str[26]
r = str[2]
h = str[4]
m = str[6]
l = str[8]
i = str[9]
n = str[10]
o = str[17]
v = str[18]
e = str[19]
s = str[20]
g = str[35]
u = str[36]
space = str[7]
point = str[40]
comma = str[31]
print(c+o+i+n+n+n+n+n+comma+a+point)
print(r+e+l+space+c+a+r+point)
print('-----------------------------------------------------')


# Вводится строка. Удалить из нее все пробелы. После этого определить, является ли она палиндромом (перевертышем),
# т.е. одинаково пишется как с начала, так и с конца.

#str = input('Введи любую строку, можешь использовать побольше пробелов:')
str = 'aaaa  aaaaaaaaaaaa  aaaaaaaaaaaaaa'
print('Введена строка -', str)
str_not_space = str.replace(' ','')
print('Введенная строка без пробелов -',str_not_space)

if str_not_space == str_not_space[::-1]:
    print('Строка является перевертышем.')
else:
    print('Строка не является перевёртышем.')
print('-----------------------------------------------------')



# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".

#str = input('Введи любую строку:')
str = 'ppqqwqwppasdadasd'
str_not_space = str.replace(' ', '')
i = 0
while i < len(str_not_space):

    if str_not_space.count(str_not_space[i])>1:
        x = str_not_space.count(str_not_space[i])
        str_not_space = str_not_space.replace(str_not_space[i],'', x-1)
    i = i+1
print(str_not_space)
print('-----------------------------------------------------')



# Найти в строке указанную подстроку и заменить ее на новую.
# Строку, ее подстроку для замены и новую подстроку вводит пользователь.

str = input('Введи строку, которая будет корректироваться: ')
print('Введена строка:',str)
str_old = input('Введи подстроку, которую хочешь заменить: ')

if str_old in str:
    str_new = input('Введи подстроку, которую хочешь вставить вместо старой:')
    str = str.replace(str_old, str_new)
    print(str)
else:
    print('Подстрока, которую ты хочешь заменить не найдена!!!')


# Вводится строка, содержащая буквы, целые неотрицательные числа и иные символы.
# Требуется все числа, которые встречаются в строке, поместить в отдельный целочисленный массив.
# Например, если дана строка "data 48 call 9 read13 blank0a", то в массиве должны оказаться числа 48, 9, 13 и 0.

import re

str = 'data 48 call 9 read13 blank0a12121212asdaas112  dasd12212c 098=- i0===9=9='
str_look = r"\d+"
str_result = re.findall(str_look, str)
print (str_result)
