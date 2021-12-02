
def get_input_item(text:str, result_type:int = 0) -> any:
    """get the input

    Args:
        text (str) : text to display
        result_type (int, optional): used for converting the result to a type
                                     0 -> default -> string
                                     1 -> converts result to an int

    Returns:
        any (int, str): result of the input 
    """
    result = ''

    try:
        result = input(text)
        if result_type == 1:
            result = int(result)
    except Exception as e:
        pass

    return result


