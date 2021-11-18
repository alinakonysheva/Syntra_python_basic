# Maak 4 dieren aan een leeuw, giraf, kat, hond. Elk dier kan een geluid maken,
# heeft een lengte( klein, gemiddeld, groot, zeer groot) en een loopsnelheid uitgedrukt in seconde/meter.
# Steek al deze dieren in een lijst en druk dan voor elk dier zijn type af,
# zijn grootte en zijn loopsnelheid

class Animal:
    sound = ''
    length = 0.0
    velocity = 0.0

    def __str__(self):
        return f'{type(self).__name__}, {self.sound}'


class Lion(Animal):
    sound = 'roar'
    length = 1.5
    velocity = 45.0


class Cat(Animal):
    sound = 'Miaaauw'
    length = 0.5
    velocity = 15.0


class Dog(Animal):
    sound = 'Blaf'
    length = 0.7
    velocity = 25.0


class Giraffe(Animal):
    sound = 'yeu'
    length = 2.5
    velocity = 65.0


def create_list() -> list[Animal]:
    '''
    returns a list of objects which derive from animals
    :return: list[Animal]
    '''
    return [Cat(), Dog(), Lion(), Giraffe()]


list_ = create_list()


def get_atr_sound(Animal):
    return Animal.sound


print(*[sound for sound in list_])

# result = map(какаянибудь тут функия чтобы брать атрибуты, list_)
