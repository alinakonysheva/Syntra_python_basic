import json

# leuk manier, gaat falen voor moeilijkere dingen
class Address(object):
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def __str__(self):
        return "{0} {1}".format(self.street, self.number)

class User(object):
    def __init__(self, name, address):
        self.name = name
        self.address = Address(**address)

    def __str__(self):
        return "{0} ,{1}".format(self.name, self.address)


import datetime

class UserOk():
    __name = ''
    __address = ''
    __bf = False
    __bt = True
    __mydate = "24/11/2021"

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def to_json(self):
        return dict(name=self.__name, address=self.__address, 
                    bt=self.__bt, bf=self.__bf, mydate=self.__mydate)

    def from_json(self, value):
        self.__name = value.get("name", '')
        self.__address = value.get("address", '')
        self.__bt = value["bt"]
        self.__bf = value["bf"]
        self.__mydate = value["mydate"]
        

    def __str__(self):
        return '{} - {}'.format(self.__name, self.__address)
       

def test_wrong():
    js = '''{"name":"Cristian", "address":{"street":"Sesame","number":122}}'''
    j = json.loads(js)
    print(j)
    u = User(**j)
    print(u)

def test_better():
    """
    u = UserOk('Kristof', 'Degros')
    j = json.dumps(u.to_json())
    print(j)
    """

    #test load
    myjson = """
            {
                "name": "Test",
                "address": "Load",
                "bt": true,
                "bf": false,
                "mydate": "25/11/2021"
            }
            """

    u = UserOk('', '')
    mydict = json.loads(myjson)
    u.from_json(mydict)
    print(u)




if __name__ == '__main__':
    # test_wrong()
    test_better()
