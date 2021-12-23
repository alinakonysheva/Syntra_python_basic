from datetime import date


def set_deadline(value: str) -> any:
    """
    takes as input a isodate string with a date in a format 9999-12-31
    set the deadline if str was in the format day.month.year and if deadline is earlier than today
    :param value: str, YYYY-MM-DD
    """
    today = date.today()

    try:
        deadline = date.fromisoformat(value)
        if deadline < today:
            raise ValueError('deadline can not be set earlier than today')
        return deadline

    except Exception as e:
        print(f'Incorrect input date string ({value}):', e)
        return None


correct_date = '2021.01-01'
print(set_deadline(correct_date))

