import os
from gettext import find

fio = 'даль лев анатольевич'

split = str.split(fio)[0]
lenf = int(len((split)))
print(f'полученная фамилия: {split}')
print(f'Длина фамилии: {lenf}')

okonchania = {"ев": "ева", "ов": "ова", "й": "ого", "ь": "я", "я": "и", "а": "ы", "ин": "ина"}

if split.find('ев', lenf-2) == lenf-2:
    print(str.title(split.replace('ев', 'ева', -1)))
if split.find('ов', lenf-2) == lenf-2:
    print(str.title(split.replace('ов', 'ова', -1)))
if split.find('ин', lenf-2) == lenf-2:
    print(str.title(split.replace('ин', 'ина', -1)))
if split.find('ой', lenf-2) == lenf-2:
    print(str.title(split.replace('ой', 'ого', -1)))
if split.find('ий', lenf-2) == lenf-2:
    print(str.title(split.replace('ий', 'ого', -1)))
if split.find('ь', lenf-1) == lenf-1:
    print(str.title(split.replace('ь', 'я', -1)))
if split.find('я', lenf-1) == lenf-1:
    print(str.title(split.replace('я', 'и', -1)))
if split.find('а', lenf-1) == lenf-1:
    print(str.title(split.replace('а', 'ы', -1)))