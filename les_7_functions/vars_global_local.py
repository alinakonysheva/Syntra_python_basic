# Maak een programma dat aan de gebruiker om getallen vraagt,
# tel deze altijd op en als de gebruiker wilt stoppen,
# druk dan het totaal af en maak gebruik van global variabele
total = 0

def sum_():
    global total
    number = 1
    while number != 0:
        try:
            number = int(input('give me number, please. If you want to quit -- press 0 '))
            total += number
        except Exception as e:
            return e
    return total


print(sum_())
