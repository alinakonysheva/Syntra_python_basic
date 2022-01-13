from uuid import uuid4

class Guest:
    __first_name: str = ''  # can be +- inside
    __last_name: str = ''

    def __init__(self, first_name: str, last_name: str = ''):
        self.__form_id = uuid4().urn[9:]
        self.__last_name = last_name
        self.__first_name = first_name

    def __str__(self) -> str:
        return f'[{self.form_id}]: {self.first_name} - {self.last_name} '

    @property
    def id(self) -> str:
        return self.__form_id

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        self.__first_name = value.strip()

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        self.__last_name = value.strip()


@property
    def to_dict(self) -> dict:
        return {'id': self.id, 'title': self.title, 'created': self.created.isoformat(sep=' '),
                'pid': self.pid, 'text': self.text, 'status': self.status,
                'list_users': self.user_list, 'deadline': self.__deadline}

    def to_json(self):
        return dumps(self.to_dict, default=str)

    @property
    def deadline(self) -> any:
        return self.__deadline

    @deadline.setter
    def deadline(self, value: str) -> any:
        """
        As an input is a isodate string with a date in a format 9999-12-31.
        If str was in a format 9999-12-31 and if deadline is earlier than today
        then returns deadline as date.
        If str was not on correct format or earlier than today then None.
        :param value: isodate str, YYYY-MM-DD
        returns: deadline as date or None
        """
        today = date.today()

        try:
            deadline = date.fromisoformat(value)
            if deadline < today:
                raise ValueError('deadline can not be set earlier than today')
            self.__deadline = deadline

        except Exception as e:
            print(f'Incorrect input date string ({value}):', e)
            self.__deadline = None

    @property
    def user_list(self) -> list:
        return self.__list_users_ids

    def create_new_task(self):
        """
        to create a new task from already existing class instance
        """
        copy_ = self.createFromJson(self.to_json())
        copy_.__id = uuid4().urn[9:]
        copy_.__created = datetime.now()
        return copy_

    @classmethod
    def createWithProperties(cls, title, pid, text):
        """
        to create an instance of Task
        """
        task = cls(title, pid, text)
        task.__title = title
        task.__text = text
        task.__pid = pid
        return task

    @classmethod
    def createFromJson(cls, value):
        """
        to create an instance of Task from json
        """
        my_dict = loads(value)
        task = cls(my_dict["title"], my_dict["pid"], my_dict["text"])
        task.__id = my_dict["id"]
        task.__created = datetime.fromisoformat(my_dict["created"])
        task.__status = my_dict["status"]
        task.__list_users_ids = my_dict["list_users"]
        return task

    def add_user_id(self, value: int) -> None:
        """
        to add user's id to the list of user ids
        @rtype: object
        """
        if value not in self.__list_users_ids:
            self.__list_users_ids.append(value)

    def remove_user_id(self, value: int) -> None:
        """
        to remove user's id from the list of user ids
        """
        self.__list_users_ids.remove(value)


class AbstractRepository:

    def __init__(self):
        pass

    def __get_filename(self, name: str):
        filename = name.strip()
        return filename

    def create_file(self, content: str, name: str):
        """
        to create file with content
        """
        try:
            with open(self.__get_filename(name), 'w') as f:
                f.write(content)
        # To Kristof: How to unittest?
        except Exception as e:  # pragma: no cover
            print(f'create_file: {e}')
            return False

        return True

    def read_file(self, name: str) -> str:
        """
        to read file
        """
        filename = self.__get_filename(name)
        contents = ''
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    contents = str(f.read())
            # To Kristof: How to unittest?
            except Exception as e:  # pragma: no cover
                print(f'read_file: {e}')

        return contents

    def del_file(self, name: str):
        """
        to delete file with content
        if path does not exist then raises ValueError
        """
        filename = self.__get_filename(name)
        if os.path.exists(filename):
            try:
                os.remove(filename)
            # To Kristof: How to unittest?
            except Exception as e:  # pragma: no cover
                print(f'delete_file: {e}')
        else:
            raise ValueError

