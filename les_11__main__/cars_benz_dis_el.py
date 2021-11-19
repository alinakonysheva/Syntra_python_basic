# Vraag de gebruiker om wagens in te geven, als types hebben we een E wagen, een hybride, een diesel,
# een benzine. Vraag de gebruiker om een type te selecteren en dan als input merk, kleur, model,
# verbruik, max snelheid, aantal personen en druk dan de eigenschappen van de wagen.
# Vraag om meerdere wagens in te geven. Druk dan af per type van wagen welke wagens zijn ingegeven.

class Vehicle:
    __brand = ''
    __color = ''
    __model = ''
    __consumption = 0.00
    __max_speed = 0.00
    __number_people = 0.00

    def __init__(self, brand, color, model, consumption, max_speed, number_people):
        self.__brand = brand
        self.__color = color
        self.__model = model
        self.__consumption = consumption
        self.__max_speed = max_speed
        self.__number_people = number_people



    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, value):
        self.__consumption = value

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        self.__max_speed = value

    @property
    def number_people(self):
        return self.__number_people

    @number_people.setter
    def number_people(self, value):
        self.__number_people = value


class ECar(Vehicle):
    type_energy = 'electricity'


class Diesel(Vehicle):
    type_energy = 'diesel'


class Petrol(Vehicle):
    type_energy = 'petrol'

class Hybrid(ECar):
    type_energy2 = 'petrol'


    def __init__(self, type_energy):
        self.__type_energy = type_energy

    @property
    def type_energy(self):
        return self.__type_energy

    @type_energy.setter
    def type_energy(self, value):
        self.__type_energy = value

def get_input(text: str, conversion_type: int = 0) -> any:
    """
        get input and convert
    Args:
        text ([str]): text to use in the display string for input
        restype (int, optional): convert or not. Defaults to 0.
            0 = default -> convert to string (not needed)
            1 = integer -> convert to integer

    Returns:
        any: int or str, depending on conversion type
    """
    try:
        inp = input(f'Geef uw conversion_type: ')
        if conversion_type == 1:
            result = int(inp)
        else:
            result = inp
    except Exception as e:
        print(e)
        result = 0

    return result


def create_list_vehicles() -> list[Vehicle]:
    list_vehicles = []
    return list_vehicles
