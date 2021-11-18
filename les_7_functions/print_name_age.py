# Maak een programma dat de gebruiker om het volgende vraagt, naam, voornaam,
# leeftijd Maak een functie om deze gegevens af te drukken

def get_name_age():
    first_name = input('give me your first name, please  ')
    last_name = input('give me your last name, please  ')
    age = input('give me your age, please  ')
    return first_name, last_name, age


def print_name(first_name, last_name, age):
    print(f'{first_name}, {last_name}, {age}')


print_name(*get_name_age())