import re

pattern_iso_str = '^[0-9]{4}-([0-9]{2}|[0-9]{1})-([0-9]{2}|[0-9]{1}&)'


class GetInput:

    @staticmethod
    def _get_input_item(text: str, result_type: int = 0, retry_count: int = 0) -> any:
        """get the input

        Args:
            text (str) : text to display
            result_type (int, optional): used for converting the result to a type
                                         0 -> default -> string
                                         1 -> converts result to an int
                                         2 -> convert result to float
                                         3 -> check of the format looks like isostring, returns str if looks like that
                                         returns None if str doesn't look like isostring
            retry_count: asks to input 5 times and to

        Returns:
            any (int, str): result of the input
        """
        result = ''

        try:
            result = input(text).strip()
            if result_type == 1:
                result = int(result)
            elif result_type == 2:
                result = float(result.replace(',', '.'))
            elif result_type == 3:
                temp = re.match(pattern_iso_str, result)
                if temp:
                    result = temp.string
                else:
                    if retry_count < 3:
                        print(f'you have {3 - retry_count} more attempts to give a correct input')
                        result = GetInput._get_input_item(text, result_type, retry_count + 1)
                    else:
                        return None
        except Exception as e:
            if retry_count < 3:
                print(f'you have {3 - retry_count} more attempts to give a correct input. ERROR: {e}')
                result = GetInput._get_input_item(text, result_type, retry_count + 1)

        return result

    @staticmethod
    def get_text(text: str):
        some_text = GetInput._get_input_item(text, result_type=0)
        return some_text

    @staticmethod
    def get_float(text: str):
        some_float = GetInput._get_input_item(text, result_type=2)
        return some_float

    @staticmethod
    def get_int(text: str):
        some_int = GetInput._get_input_item(text, result_type=1)
        return some_int

    @staticmethod
    def get_isostr(text: str):
        some_isostr = GetInput._get_input_item(text, result_type=3)
        return some_isostr


def validate_number_within_range(func, arg, min_, max_, text_error):
    try:
        int_value = func(arg)
        if min_ <= int_value <= max_:
            return int_value
        else:
            print(text_error, f'value({int_value}) has to be within a range ({min_}, {max_})')
            raise ValueError
    except Exception as e:
        print(e, f'not possible to get int from your value from {func}')

