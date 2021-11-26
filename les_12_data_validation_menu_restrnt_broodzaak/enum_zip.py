from random import sample
# удаляем повторяющиеся элементы, внешний цикл -- длинный, внутренний цикл -- короткий
a = sample(range(1, 12), 5)
b = sample(range(1, 12), 7)

print(a)
print(b)

for el in b:
    while el in a:
        a.remove(el)

print(a)
print(b)
