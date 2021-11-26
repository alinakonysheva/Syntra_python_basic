# Maak een functie dat een lijst van getallen aanvaard en geef dan
# alle unieke waarden terug voorbeeld [1, 2, 3, 3, 4, 5] → [1, 2, 3, 4, 5]

def get_unique_values(list_: list) -> list:
    copy_list = list_.copy()
    result = []

    for el in copy_list:
        if el not in result:
            result.append(el)
    return result


print(get_unique_values([1, 2, 3, 3, 4, 5]))


def get_unique_values_2(list_: list) -> list:
    copy_list = list(set(list_.copy()))
    return copy_list


print(get_unique_values_2([1, 2, 3, 3, 4, 5]))


def get_unique_values3(list_: list) -> list:
    res = []
    result = [res.append(i) for i in list_ if i not in res]

    return res


print(get_unique_values3([1, 2, 3, 3, 4, 5]))
