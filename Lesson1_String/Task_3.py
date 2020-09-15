# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Учитывать только английские буквы.

import re

str = 'AaBbCcDdEe1122sdad'
up = r'[A-Z]'
low= r"[a-z]"
upper_str = re.findall(up,str)
lower_str = re.findall(low,str)
print('В веденной строке', len(upper_str),'прописных и', len(lower_str), 'строчных букв.')


# Вводится строка, состоящая из слов, разделенных пробелами. Требуется посчитать количество слов в ней.

import re
str = 'Вводится строка, состоящая из слов, разделенных пробелами. Требуется посчитать количество слов в ней. ' \
      'The Office of Human Resources Management will revert to the Assembly in due course with a comprehensive proposal.'

condition = r"\w+"
onlyWords = re.findall(condition, str)
print('Количество слов в строке:', len(onlyWords))


# Вводится ненормированная строка, у которой могут быть пробелы в начале,
# в конце и между словами более одного пробела. Привести ее к нормированному
# виду, т.е. удалить все пробелы в начале и конце, а между словами оставить
# только один пробел.

import re
str = '   Капитан  сделал мне      очень  интересное     предложение. '
pattern = r"\s{2,}"
str = re.sub(pattern, ' ', str).strip()
print(str)
