from res_menu import Menu, create_menu_list

class Order():
    __menus = {}
    __price = 0.00
    __table = 0

    def __init__(self, table):
        self.__menus = {}
        self.__price = 0.00
        self.table = table
    
    @property
    def price(self):
        return round(self.__price, 2)


    @property
    def table(self):
        return self.__table


    @table.setter
    def table(self, value):
        self.__table = value


    def add_menu(self, menu: Menu):
        # key value
        # unieke nummer menu = key
        # value = vorige value + 1
        self.__menus[menu.number] = self.__menus.get(menu.number, 0) + 1
        self.__calculate__price(menu.price)

    def __calculate__price(self, price):
        self.__price = self.__price + price

    @property 
    def menus(self):
        return self.__menus

def __test_create_order():
    menus = create_menu_list()
    order = Order()
    order.add_menu(menus[0])
    order.add_menu(menus[1])
    order.add_menu(menus[0])
    print(order.price)
    

def create_order(table, menus)-> Order:
    if menus is not None:
        order = Order(table)
        for menu in menus:
            order.add_menu(menu)
        return order
    else:
        raise Exception('we can not create a menu without orders')

        
def print_order(order):
    if order is not None:
        print('bestelling voor tafel: {}'.format(order.table))
        print('totale prijs= {}'.format(order.price))
        for x,y in order.menus.items():
            print('menu {} - {}x'.format(x, y))
    else:
        print('bestelling is leeg')


if __name__ == '__main__': 
    __test_create_order()  
