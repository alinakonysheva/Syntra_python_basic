from json import dumps, loads
from files import read_json_file, create_json_file


class BaseObject():

    def _get_dict(self) -> dict:
        return dict()

    def _set_dict(self, value):
        pass

    @property
    def as_dict(self) -> dict:
        return self._get_dict()
    
    @as_dict.setter
    def as_dict(self, value: dict):
        self._set_dict(value)

    @property
    def as_json(self) -> str:
        return dumps(self.as_dict)

    @as_json.setter
    def as_json(self, value: str):
        ddict = loads(value)
        self.as_dict = ddict
        


class BaseList():  
    __filename = 'base.json'
    __classtype = None

    def __init__(self, classtype, filename: str =''):
        self.__items = []
        if filename != '':
            self.__filename = filename
        self.__classtype = classtype

    @property
    def items(self) -> list:
        return self.__items

    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.__filename = value

    @property
    def as_dict(self) -> dict:
        mylist = []
        for item in self.items:
            mylist.append(item.as_dict)

        output = {}
        output['data'] = mylist

        return output

    @as_dict.setter
    def as_dict(self, value: dict):
        mylist = value["data"]
        self.__items = []
        for item in mylist:
            obj = self.__classtype.fromDict(item)
            self.items.append(obj)

    @property
    def as_json(self) -> str:
        return dumps(self.as_dict)

    @as_json.setter
    def as_json(self, value: str):
        if value != '':
            d = loads(value)
            self.as_dict = d

    def save(self):
        """save the list
        """
        create_json_file(self.as_json, self.__filename)

    def load(self):
        """load the contents of this list
        """
        filecontents = read_json_file(self.__filename)
        if filecontents != '':
            # clear stuff first
            self.__items = []
            self.as_json = filecontents

    
    def add(self, obj):
        """add an object to the internal list

        Args:
            obj (Object): an object
        """
        if obj is not None:
            self.__items.append(obj)
            return obj
            
    def remove(self, nr: int):
        """remove an object by id

        Args:
            nr (int): index in the list
        """
        if (nr > -1)and (nr < len(self.__items)):
            del self.__items[nr]


