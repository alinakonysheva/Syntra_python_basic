from datetime import datetime, date, time
from uuid import uuid4
from json import loads, dumps


class Event:
    __invitor_name: str = ''
    __party_date: any = None
    __party_start: time = None
    __party_end: time = None
    __phone_number: str = ''  # can be +- inside
    __party_place: str = ''
    __party_features: str = ''
    __created = None

    def __init__(self, invitor_name: str, party_date: any, party_start: time, party_end: time, phone_number: str,
                 party_place, party_features: str = ''):
        self.__form_id = uuid4().urn[9:]
        self.__created = datetime.now()
        self.__invitor_name = invitor_name
        self.__party_date = party_date
        self.__party_start = party_start
        self.__party_end = party_end
        self.__party_place = party_place
        self.__phone_number = phone_number
        self.__party_features = party_features
        self.id_guest_list = []

    def __str__(self) -> str:
        return f'[{self.form_id}]: {self.created} - {self.invitor_name} - {self.party_date} \n ' \
               f'{self.party_start} - {self.party_end} - {self.phone_number} - {self.party_features}'

    @property
    def form_id(self) -> str:
        return self.__form_id

    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        self.__phone_number = value.strip()

    @property
    def invitor_name(self) -> str:
        return self.__invitor_name

    @invitor_name.setter
    def invitor_name(self, value: str):
        self.__invitor_name = value.strip()

    @property
    def party_features(self) -> str:
        return self.__party_features

    @party_features.setter
    def party_features(self, value: str):
        self.__party_features = value.strip()

    @property
    def created(self) -> datetime:
        """
        an instance created on this date
        """
        return self.__created

    @property
    def party_date(self) -> any:
        return self.__party_date

    @party_date.setter
    def party_date(self, value: str) -> any:
        today = date.today()

        try:
            party_date = date.fromisoformat(value)
            if party_date < today:
                raise ValueError('party_date can not be set earlier than today')
            self.__party_date = party_date

        except Exception as e:
            print(f'Incorrect input date string ({value}):', e)
            self.__party_date = None

    @property
    def party_start(self) -> time:
        return self.__party_start

    @party_start.setter
    def party_start(self, value: time):
        """

        :type value: time of party's start
        """
        self.__party_date = value

    @property
    def party_end(self) -> time:
        return self.__party_end

    @party_end.setter
    def party_end(self, value: time):
        """

        :type value: time of party's end
        """
        self.__party_end = value

    @property
    def to_dict(self) -> dict:
        return {'id': self.form_id, 'title': self.title, 'created': self.created.isoformat(sep=' '),
                'pid': self.pid, 'text': self.text, 'status': self.status,
                'list_users': self.user_list, 'deadline': self.__deadline}

    @to_dict.setter
    def to_dict(self, value: dict):
        self.__id = value["id"]
        self.__invitor_name = value["title"]
        self.__text = value["text"]
        self.__created = datetime.strptime(value["created"], "%Y-%m-%d %H:%M:%S")
        self.__pid = value["pid "]
        self.__status = value["status"]
        self.__list_users = value["list_users"]
        self.__deadline = value["deadline"]

    @property
    def to_json(self):
        return dumps(self.to_dict, default=str)

    @to_json.setter
    def json(self, value):
        my_dict = loads(value)
        self.to_dict = my_dict

    """
    # As an input is a isodate string with a date in a format 9999-12-31.
    # If str was in a format 9999-12-31 and if deadline is earlier than today
    # then returns deadline as date.
    # If str was not on correct format or earlier than today then None.
    #:param value: isodate str, YYYY-MM-DD
    # returns: deadline as date or None
    """

    @property
    def user_list(self) -> list:
        return self.__list_users

    def create_new_task(self):
        """
        # to create a new task from already existing class instance
        """
        copy_ = self.createFromJson(self.to_json)
        copy_.__id = uuid4().urn[9:]
        copy_.__created = datetime.now()
        return copy_

    @classmethod
    def createWithProperties(cls, title, pid, text):
        """
        # to create an instance of Task
        """
        task = cls(title, pid, text)
        task.__invitor_name = title
        task.__text = text
        task.__pid = pid
        return task

    @classmethod
    def createFromJson(cls, value):
        """
        # to create an instance of Task from json
        """
        my_dict = loads(value)
        task = cls(my_dict["title"], my_dict["pid"], my_dict["text"])
        task.__id = my_dict["id"]
        task.__created = datetime.fromisoformat(my_dict["created"])
        task.__status = my_dict["status"]
        return task
