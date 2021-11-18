# Maak de rij van fibonacci (toon alleen de eerste 10-15)
# Doet dit eerst met een niet recursieve functie en dan met een recursieve functie

n0 = 0
n1 = 1
count = 0
while count <= 15:
    print(n0)
    print(n1)
    count += 2
    temp = n1
    n0 = n1 + n0
    n1 = n0 + temp


