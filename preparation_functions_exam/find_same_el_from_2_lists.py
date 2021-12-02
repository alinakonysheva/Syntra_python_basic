import random

a = [random.randint(-10, 10) for i in range(0, 10)]
b = [random.randint(-10, 10) for i in range(0, 10)]

print(a, '\n', b)

c = [i for i in a if i in b and i // 2 == 0]
print(c)
