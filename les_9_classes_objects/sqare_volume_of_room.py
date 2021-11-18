# maak een programma dat, lengte, breedte en hoogte vraagt van een kamer.
# Steek dit in een object, geef dan de oppervlakte en het volume van de kamer weer.

class Room:
    length = 0
    width = 0
    height = 0

    def __init__(self, first=0, second=0, third=0):
        self.length = first
        self.width = second
        self.height = third

    def get_perimeter(self) -> any:
        '''
        to count perimeter
        args: float, int
        :return: perimeter, int or float
        '''
        try:
            perimeter = 2 * self.length + 2 * self.width
        except ValueError:
            return 0
        return perimeter

    def get_volume(self) -> any():
        '''
        to count volume
        args: float, int
        :return: volume of the room
        '''
        try:
            volume = self.length * self.width * self.height
        except ValueError:
            return 0
        return volume


room = Room(2, 2, 3)

print(room.get_perimeter(), room.get_volume())
