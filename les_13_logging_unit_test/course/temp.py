

'''
import json
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

if __name__ == '__main__':
    js = {"name":"Cristian", "address":{"street":"Sesame","number":122}}
    j = json.loads(js)
    print(j)
    u = User(**j)
    print(u)



import unittest

class TestUser(unittest.TestCase):

    def test_user_activation(self):
        pass

    def test_user_points_update(self):
        pass

    def test_user_level_change(self):
        pass

if __name__ == '__main__':
    unittest.main()
'''