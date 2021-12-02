
class Menu():
    __items = []
    __price = 0.00
    __number = 0

    def __init__(self, number: int, price: float, *args):
        """constructor

        Args:
            number: number of the menu
            price (float): menu price
            args : list of items in the menu
        """
        self.__items = []
        self.__number = number
        self.__price = price
        for arg in args:
            self.__additem(arg)

    def __str__(self):
        return '{} - {} - {}'.format(self.number, self.price, self.items)

    @property
    def number(self):
        return self.__number
    
    @property
    def price(self):
        return self.__price
    
    @property
    def items(self):
        return self.__items

    def __additem(self, item: str):
        """function to add an item to add to my menu

        Args:
            item (str): text based description
        """
        self.__items.append(item)

   

def create_menu_list() -> list:
    menus = []
    menu = Menu(1, 35, 'dagsoep', 'vis', 'dessert')
    menus.append(menu)
    menus.append(Menu(2, 30, 'steak/friet', 'ijsje'))
    menus.append(Menu(3, 35, 'garnaalkroket', 'mosselen'))
    menus.append(Menu(4, 30, 'antipaste', 'paste', 'panna cotta'))
    return menus

def print_menu_list(menus):
    print('-'*20)
    print('menus')
    print('-'*20)
    for menu in menus:
        print(menu)

def __test_create_menu():
    menus = create_menu_list()
    for menu in menus:
        print('menu {}'.format(menu))
        

if __name__ == '__main__':
    print('module res_menu')
    __test_create_menu()



