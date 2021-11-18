# Maak een programma dat de gebruiker 5 namen en een salaris vraagt,
# is er geen salaris dan nemen we als default 2000 euro.
# Druk deze lijst dan af

number_of_employees = 5
list_of_emps = []

def get_salary():
    name = input('give me a name of an employee  ')
    salary = input('give me a salary of an employee  ')
    if salary == '':
        salary = 2000
    return name, salary

for employee in range(number_of_employees):
    list_of_emps.append(get_salary())

for item in list_of_emps:
    print(f'name: {item[0]}, salary: {item[1]}')
