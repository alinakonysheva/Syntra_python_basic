# Maak een programma dat de diameter van een cirkel vraagt en
# dan het volgende weergeeft: de straal en de diameter, de omtrek en de oppervlakte.

from math import pi


class Circle:
    __d = 0

    def __init__(self, d):
        self.d = d

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, value):
        self.__d = value

    def radius(self):
        r = self.__d / 2
        return r

    def perimeter(self):
        o = pi * self.__d
        return o

    def surface(self):
        s = (pi * self.__d ** 2) / 4
        return s


def get_input(text: str, conversion_type: int = 0) -> any:
    """
        get input and convert
    Args:
        text ([str]): text to use in the display string for input
        restype (int, optional): convert or not. Defaults to 0.
            0 = default -> convert to string (not needed)
            1 = integer -> convert to integer

    Returns:
        any: int or float, depending on conversion type
    """
    try:
        inp = input(f'Geef diameter van uw cirkel: ')
        if conversion_type == 1:
            result = int(inp)
        else:
            result = float(inp)
    except Exception as e:
        print(e, 'U moet een cijfer geven')
        result = 0

    return result


def do_output(circle: Circle):
    if circle is not None:
        print(f'de straal -- {circle.radius()} en de diameter {circle.d}')
        print(f'omtrek -- {circle.perimeter()}')
        print(f'oppervlakte -- {circle.surface()}')

    else:
        print('cirkel was not created')


def create_circle() -> Circle:
    """create  a circle object

    Returns:
        Circle: return a circle object
    """
    d = get_input('de diameter van een cirkel = ')

    return Circle(d)


def do_run():
    circle = create_circle()
    do_output(circle)


do_run()
