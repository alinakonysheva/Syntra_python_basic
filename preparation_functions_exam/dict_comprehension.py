import random

result = {i: random.randint(-100, 100) for i in range(10)}

print(result)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k: v * 2 for (k, v) in dict1.items()}
print(double_dict1)
dict1_keys = {k * 2: v for (k, v) in dict1.items()}
print(dict1_keys)

# Use dictionary comprehension
numbers = range(10)
new_dict_comp = {n: n ** 2 for n in numbers if n % 2 == 0}

# Initialize `fahrenheit` dictionary
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}

# Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5) / 9) * (x - 32), fahrenheit.values()))

# Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)

celsius_2 = {k: (float(5) / 9) * (v - 32) for (k, v) in fahrenheit.items()}

print(celsius_2)
