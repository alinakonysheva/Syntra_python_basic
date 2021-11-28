# 2. Vraag de gebruiker om een paar lijnen tekst in te geven. Test voor elke lijn als elke letter van het
# alfbet gebruikt is in die lijn input.
# Als output willen we het volgende zien “Volgnummer – Nee/Ja – de ingegeven lijn”
# Voorbeeld output:
# 1 – Nee
# “De eerste lijn bevat niet elke letter van het alfabet”
# 2 – Ja
# “De tweede lijn bevat welk elk letter van alfabet (abcdefghijklmnopqrstuvwxyz)”
# 3 – Nee
# “lijn is te kort”

C_NUMBER_LINES = 3
C_SET_ALPHABET_BIG_LETTERS = {'D', 'T', 'W', 'E', 'R', 'A', 'P', 'V', 'K', 'H', 'L',
                              'J', 'O', 'X', 'I', 'F', 'Q', 'S', 'B', 'C', 'Y', 'M', 'Z', 'U', 'N', 'G'}

C_FIRST_LINE = 'De eerste lijn bevat'
C_SECOND_LINE = 'De tweede lijn bevat'
C_THIRD_LINE = 'De derde lijn bevat'
C_FORTH_LINE = 'De virde lijn bevat'

dict_output_lines = {1: C_FIRST_LINE, 2: C_SECOND_LINE, 3: C_THIRD_LINE, 4: C_FORTH_LINE}


def get_lines(number_lines) -> list:
    """
    to get text from user
    :param number_lines: how many lines we would like to have
    :return: list of lines from user
    """
    lines = []
    for el in range(number_lines):
        line = input('Uw lijn van text:  ')
        lines.append(line)
    return lines


def is_containing_all_letters(text: str) -> str:
    """
    to check
    :param text: string that will be checked for all letters of alphabet
    :return: text
    """
    origin_text = text
    if len(text) < 26:
        return 'Nee', 'lijn is te kort', origin_text
    text = text.upper()
    list_letter_out_text = []
    for letter in text:
        if letter.isalpha():
            list_letter_out_text.append(letter)
    try:
        set_with_all_letters = set(list_letter_out_text)
        if set_with_all_letters == C_SET_ALPHABET_BIG_LETTERS:
            return 'Ja', 'elk letter van alfabet', origin_text
        else:
            return 'Nee', 'niet elk letter van alfabet', origin_text

    except Exception as e:
        return ''


def do_run():
    text_from_user = get_lines(C_NUMBER_LINES)
    for count, value in enumerate(text_from_user, start=1):
        if is_containing_all_letters(value)[1] == 'lijn is te kort':
            print(f'{count} -- {is_containing_all_letters(value)[0]}\n{is_containing_all_letters(value)[1]}')
        else:
            print(
                f'{count} -- {is_containing_all_letters(value)[0]}\n{dict_output_lines[count]} {is_containing_all_letters(value)[1]} {is_containing_all_letters(value)[2]}')


do_run()
