from datetime import date


class SetDate:
    __birthday = None

    def __init__(self, birthday: str):
        self.__birthday = birthday

    @property
    def birthdate(self) -> any:
        return self.__birthday

    @birthdate.setter
    def birthdate(self, value: str) -> any:
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
            birthday = date.fromisoformat(value)
            if birthday > today:
                raise ValueError('Birthday can not be set later than today')
            self.__birthday = birthday

        except Exception as e:
            print(f'Incorrect input date string ({value}):', e)
            self.__birthday = None
