# Maak een functie die zichzelf oproept en dan 5x

def call_self(n):
    if n < 5:
        print(n)
        return call_self(n + 1)
    else:
        return 'end'

print(call_self(0))