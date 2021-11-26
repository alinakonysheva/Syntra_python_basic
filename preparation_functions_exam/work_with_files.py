# файловый дескриптор:
# по умолчанию файл открывается на чтение, можно ничего не указывать
# file = open('1.txt', 'w') -- сначала перезапишет
# file = open('1.txt', 'a') -- добавить к уже написанному
# w, a -- файл создасться, если его не существует.
import os

file = open('1.txt', 'w+', encoding='UTF-8')
file.write('smth - smth\n ')
# переходим на самое начало файла
file.seek(0)
for line in file:
    name, salary = line.split(' - ')
    print(name, salary)

file.close()

# как узнать существует ли файл
print(os.path.exists('123.txt'))

# readlines() -- возвращает массив элементов, которые состоят из строк
file = open('123.txt')
print(file.readlines())
file.close()

# для чтения файла строчка за строчкой надо использовать readline
f = open('123.txt')
for line in f:
    # print(line, end='')
    # лушче срезать всю фигню у строки
    print(line.strip())

f.close()

# менджер контекста, чтобы не было пробелм с памятью
# он сам следит за памятью, закрывает, когда будет не нужно,
# можно потом


with open('123.txt') as file:
    for line in file:
        print(line.strip())
