gift_category = {1: 'cloth', 2: 'transport', 3: 'sport', 4: 'stuffed_toys'}


class Gift:

    def __init__(self, gift_name):
        self.__gift_name = gift_name
        self.__category = 0
        self.__length = 0
        self.__width = 0
        self.__height = 0
        self.__wrapping = Wrapper
        self.__wrapped = False
        pass


class Child:
    def __init__(self):
        pass


class Letter:
    address = ''
    gift_name = ''

    def __init__(self, address, gift_name):
        self.__address = address
        self.__gift_name = gift_name


class Wrapper:
    def __init__(self, color, type_shining, decoration):
        self.__color = color
        self.__type_shining = type_shining
        self.__decoration = decoration


class Adress:
    pass


class Delivery:
    def __init__(self):
        self.__child = None
        self.__gift = None
        self.__address = None
