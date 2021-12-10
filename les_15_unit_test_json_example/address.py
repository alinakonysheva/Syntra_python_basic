import json
from inputs import get_input_item

class Address():
    __zip = ''
    __city = ''
    __street = ''
    __nr = ''
    __country = ''

    def __init__(self, street, nr, zip, city, country):
        self.__street = street
        self.__nr = nr
        self.__zip = zip
        self.__city = city
        self.__country = country

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, value:str):
        self.__street = value

    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, value:str):
        self.__zip = value

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, value: str):
        self.__city = value

    @property
    def nr(self) -> str:
        return self.__nr
    
    @nr.setter
    def nr(self, value: str):
        self.__nr = value 

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, value: str):
        self.__country = value

    def __str__(self) -> str:
        return "{} {}, {} {}, {}".format(self.street, self.nr, 
                                         self.zip, self.city, 
                                         self.country)

    def copy(self, value):
        if value is not None and type(value) == Address:
            self.street =  value.street
            self.nr =  value.nr
            self.country =  value.country
            self.zip =  value.zip
            self.city =  value.city
            self.country = value.country
            
    @property
    def to_dict(self) -> dict:
        return dict(
            street=self.street,
            nr=self.nr,
            zip=self.zip,
            city=self.city,
            country=self.country
        )

    @property
    def to_json(self):
        return json.dumps(self.to_dict)


    def from_dict(self, value):
        self.street = value["street"]
        self.nr = value["nr"]
        self.zip = value["zip"]
        self.city = value["city"]
        self.country = value["country"]
        
    def from_json(self, value):
        d = json.loads(value)
        self.from_dict(d)

def create_adress(street='', nr='', zip='', city='', country='') -> Address:
     return Address(street, nr, zip, city, country)


def get_adress_fields(adr: Address):
    if adr is not None and type(adr) == Address:
        adr.street = get_input_item('Geef uw straat: ')
        adr.nr = get_input_item('Geef uw nr: ')    
        adr.zip = get_input_item('Geef uw postcode: ')
        adr.city = get_input_item('Geef uw gemeente: ')
        adr.country = get_input_item('Geef uw land: ')
