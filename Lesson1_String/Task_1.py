# Входные данные "Abrakadabra"
# 1. Сначала выведите третий символ этой строки.
# 2. Во второй строке выведите предпоследний символ этой строки.
# 3. В третьей строке выведите первые пять символов этой строки.
# 4. В четвертой строке выведите всю строку, кроме последних двух символов.
# 5. В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# 6. В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# 7. В седьмой строке выведите все символы в обратном порядке.
# 8. В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего
# 9. В девятой строке выведите длину данной строки.

str = 'Abrakadabra'
print('String #1 -', str[2])
print('String #2 -', str[10])
print('String #3 -', str[:5])
print('String #4 -', str[:9])
print('String #5 -', str[2:11:2])
print('String #6 -', str[1:11:2])
print('String #7 -', str[::-1])
print('String #8 -', str[::-2])
print('String #9 -', len(str))