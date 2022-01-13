import json
from inputs import GetInput


class Address:
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
    def street(self, value: str):
        self.__street = value

    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, value: str):
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
        return f"{self.street} {self.nr}, {self.city} {self.zip}, {self.country}"

    def copy(self, value):
        if value is not None and type(value) == Address:
            self.street = value.street
            self.nr = value.nr
            self.country = value.country
            self.zip = value.zip
            self.city = value.city
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


def get_address_fields(adr: Address):
    if adr is not None and type(adr) == Address:
        adr.street = GetInput.get_text('Geef uw straat: ')
        adr.nr = GetInput.get_text('Geef uw nr: ')
        adr.zip = GetInput.get_text('Geef uw postcode: ')
        adr.city = GetInput.get_text('Geef uw gemeente: ')
        adr.country = GetInput.get_text('Geef uw land: ')
