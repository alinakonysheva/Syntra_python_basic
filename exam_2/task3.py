# 3. Vraag een gebruiker om een lijst van medewerkers in te geven inclusief hun salaris. Indien hun
# salaris niet ingegeven wordt, gebruiken we als default 2000.
# Als output willen we het volgende zien
# Het gemiddelde loon is x euro
# Medewerker x heeft het hoogste loon: x euro
# Medewerker x heeft het laagste loon: x euro
# ------------------------------------------------------
# Lijst van alle medewerkers:
# Medewerker x : x euro
# Medewerker y : x euro
# Medewerker A : x euro

C_STOP_CHAR = 'n'
C_DEFAULT_SALARY: int = 2000


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


def get_list_staff_names() -> list:
    """

    :return: list of staff names
    """
    list_staff_names_ = list()
    staff_name = ''
    while staff_name != C_STOP_CHAR:
        staff_name = get_input('een naam van uw medewerker, en letter \'n\' als u wilt af te ronden')
        list_staff_names_.append(staff_name)
    return list_staff_names_[:-1]


def get_salaries(list_staff_names_: list) -> dict:
    """

    :param list_staff_names_: list of staff names
    :return: dict, where key is a name of a worker and value is a salary of this worker
    """
    names_salaries = {}
    for name in list_staff_names_:
        salary = get_input(f'een loon van uw medewerker {name}', 1)
        if salary == '':
            salary = C_DEFAULT_SALARY
        name_salary = {name: salary}
        names_salaries.update(name_salary)
    return names_salaries


def count_avg_max_min_salary(names_salaries: dict, type_stat=1) -> any:
    """

    :param names_salaries: dict with name: salary
    :param type_stat: 1 -- returns tuple (name, salary) with max salary
    type_stat: 2 list with tuples (name, salary) with min salary
    type_stat: 3 int with average salary
    :return: any, list with tuples of int
    """
    max_sal_number = max(names_salaries.values())
    min_sal_number = min(names_salaries.values())

    max_salary = [(name, salary) for name, salary in names_salaries.items() if salary == max_sal_number]
    min_salary = [(name, salary) for name, salary in names_salaries.items() if salary == min_sal_number]
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


def print_out(dict_names_salaries):
    print(f'Het gemiddelde loon is {count_avg_max_min_salary(dict_names_salaries, 3)} euro')
    for el in count_avg_max_min_salary(dict_names_salaries, 1):
        print(f'Medewerker {el[0]} heeft het hoogste loon: {el[1]} euro')
    for el in count_avg_max_min_salary(dict_names_salaries, 2):
        print(f'Medewerker  {el[0]} heeft het laagste loon {el[1]} euro')
    print('------------------------------------------------------')
    print('Lijst van alle medewerkers:')
    for k, v in dict_names_salaries.items():
        print(f'Medewerker {k} : {v} euro')


def do_run():
    list_staff_names = get_list_staff_names()
    dict_names_salaries = get_salaries(list_staff_names)
    print_out(dict_names_salaries)


do_run()
