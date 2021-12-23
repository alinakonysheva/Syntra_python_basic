class GetInput:
    @staticmethod
    def _get_input_item(text: str, result_type: int = 0, retry_count: int = 5) -> any:
        """get the input

        Args:
            text (str) : text to display
            result_type (int, optional): used for converting the result to a type
                                         0 -> default -> string
                                         1 -> converts result to an int
                                         2 -> convert result to float

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
        except Exception as e:
            if retry_count < 5:
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

