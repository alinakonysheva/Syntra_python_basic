class Person:
    first_name = ''
    last_name = ''

    def __init__(self, first='Unknown', last='Unknown'):
        self.first_name = first
        self.last_name = last

    def get_fullname(self, token=''):
        return self.first_name + token + self.last_name

    def set_lastname(self, lastname):
        self.last_name = lastname.upper()