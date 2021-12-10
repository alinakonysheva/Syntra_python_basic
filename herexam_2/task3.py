# 3. Vraag een gebruiker om een lijst van personen in te geven inclusief het bedrag dat ze krijgen als eindejaarscadeau.
# Indien er geen bedrag is ingegeven, gebruiken we als default 20 euro
# Als output willen we het volgende zien
# Persoon x krijgt het meeste namelijk x euro
# Persoon x krijgt het minste namelijk x euro
# ------------------------------------------------------
# Lijst van alle personen:
# Persoon x : x euro
# Persoon y : x euro
# Persoon z : x euro
# ------------------------------------------------------
# Totaal : x euro
C_STOP_CHAR = 'n'
C_DEFAULT_GIFT: int = 20


class Person:
    __name = ''
    __gift = 0.00

    def __init__(self, name, gift):
        self.__name = name
        self.__gift = gift

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def gift(self):
        return self.__gift

    @gift.setter
    def gift(self, value):
        self.__gift = value

    @classmethod
    def createWithProperties(cls, name, gift=C_DEFAULT_GIFT):
        person = cls()
        person.__name = name
        person.__gift = gift
        return person

    def __str__(self):
        return f'Persoon {self.__name}: {self.__gift} euro'


class Budget:
    __people = []

    def __init__(self):
        self.__people

    @property
    def people(self):
        return self.__people

    @people.setter
    def people(self, value):
        self.__people = value

    def add_people(self, value: Person):

        """
        to add a person to a Budget
        :param value: type: Person
        """
        if value:
            self.__people.append(value)
        else:
            print('person does not exists, an instance of Person was not created')
            raise ValueError

    def calculate_gifts(self) -> any:
        """
        to calculate total budget
        :return: any: int of float
        """
        total_budget = 0
        for pers in self.__people:
            total_budget += pers.gift
        return total_budget

    def count_max_min_gift(type_stat=1) -> any:
        """
        to find the biggest and the smallest gift
        :param type_stat: 1 -- returns tuple (name, salary) with max salary
        type_stat: 2 list with tuples (name, salary) with min salary
        :return: any, list with tuples of int
        """
        list_with_pairs = []
        max_gift_money = 0
        min_gift_money = 0

        for person in self.__people:
            if max_gift_money <= person.__gift:
                max_gift_money = person.__gift
            if min_gift_money >= person.__gift:
                min_gift_money = person.__gift
            list_with_pairs.append((person.__name, person.__gift))

        max_gift = [el for el in list_with_pairs if el[1] == max_gift_money]
        min_gift = [el for el in list_with_pairs if el[1] == min_gift_money ]

        length_list_salary = len(names_salaries.values())
        if length_list_salary != 0:
            avg_salary = sum(names_salaries.values()) / length_list_salary
        else:
            print('Sorry, geen salarissen waren gegeven')
        if type_stat == 1:
            return max_salary
        if type_stat == 2:
            return min_salary
        if type_stat == 3:
            return avg_salary


def get_input(text: str, conversion_type: int = 0) -> any:
    """
        get input and convert
    Returns:
        any: int or str, depending on conversion type
        :param
        text ([str]): text to use in the display string for input
        conversion_type (int, optional): convert or not. Defaults to 0.
            0 = default -> convert to string (not needed)
            1 = integer -> convert to integer
    """

    try:
        inp = input(f'Geef, astublieft, {text}: ')
        if conversion_type == 1:
            result = int(inp)
        else:
            result = inp
    except ValueError:
        result = inp

    return result


def create_budget() -> Budget:
    users_quit = ''
    budget = Budget()
    while users_quit != C_STOP_CHAR:
        pers_name = get_input(f'De naam van een persoon: ')
        pers_gift = get_input(f'Het bedrag voor dit persoon: ')
        person = Person.createWithProperties(pers_name, pers_gift)
        budget.add_people(person)

    return budget


def do_output(budget: Budget):
    """
    to print a result
    :param budget: is an instance of Budget
    :print: names, gifts and the total budget of gifts
    """
    if budget:
        print('-' * 45)
        print(f'Uw broodje bestaat uit:\nGekozen brood: {bun.bread_type.name}')
        print(f'Uw beleg: ')
        for i in range(len(bun.stuffing)):
            print(bun.stuffing[i].name, end=' ')
        print()
        print(f'Uw toppings:')
        for i in range(len(bun.topping)):
            print(bun.topping[i].name, end=' ')
        print()
        print('-' * 45)
        print(f'De totale verkoopprijs was {calculate_purchase(bun)} euro')
    else:
        print('bun was not created')


def main():
    bun = create_bun()
    do_output(bun)


if __name__ == '__main__':
    main()
