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
        person = cls(name, gift)
        return person

    def __str__(self):
        return f'{self.__name}: {self.__gift}'


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
            total_budget += int(pers.gift)
        return total_budget

    def count_max(self, ) -> any:

        max_el = sorted(self.people, key=lambda item: int(item.gift), reverse=True)[0]
        return max_el

    def count_min(self, ) -> any:

        min_el = sorted(self.people, key=lambda item: int(item.gift))[0]
        return min_el

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
        result = C_DEFAULT_GIFT

    return result


def create_budget() -> Budget:
    users_quit = ''
    budget = Budget()
    while users_quit != C_STOP_CHAR:
        pers_name = get_input(f'de naam van een persoon')
        pers_gift = get_input(f'het bedrag voor dit persoon', 1)
        person = Person.createWithProperties(pers_name, pers_gift)
        budget.add_people(person)
        users_quit = input('Type \'n\' als geen andere mensen een cadeau krijgen')

    return budget


def do_output(budget: Budget):
    """
    to print a result
    :param budget: is an instance of Budget
    :print: names, gifts and the total budget of gifts
    """
    if budget:
        print('-' * 45)
        highest = budget.count_max()
        lowest = budget.count_min()
        print(f'Persoon {highest.name} krijgt het meeste namelijk {highest.gift} euro')
        print(f'Persoon {lowest.name} krijgt het minste namelijk {lowest.gift} euro')

        print('Lijst van alle personen:')
        for i in range(len(budget.people)):
            print(f'Persoon {budget.people[i].name}: {budget.people[i].gift} euro')

        print('-' * 45)
        print()
        print(f'Totaal : {budget.calculate_gifts()} euro')
    else:
        print('budget was not created')


def main():
    do_output(create_budget())


if __name__ == '__main__':
    main()
