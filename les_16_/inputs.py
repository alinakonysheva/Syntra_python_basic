def get_input_item(text: str, result_type: int = 0) -> any:
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
        pass

    return result
