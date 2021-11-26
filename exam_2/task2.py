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

C_NUMBER_LINES = 2
C_SET_ALPHABET_BIG_LETTERS = {'D', 'T', 'W', 'E', 'R', 'A', 'P', 'V', 'K', 'H', 'L',
                              'J', 'O', 'X', 'I', 'F', 'Q', 'S', 'B', 'C', 'Y', 'M', 'Z', 'U', 'N', 'G'}


def is_containing_all_letters(text: str):
    origin_text = text
    if len(text) < 26:
        return 'Nee', 'lijn is te kort'
    text = text.upper()
    list_letter_out_text = []
    for letter in text:
        if letter.isalpha():
            list_letter_out_text.append(letter)
    try:
        set_with_all_letters = set(list_letter_out_text)
        if set_with_all_letters == C_SET_ALPHABET_BIG_LETTERS:
            return 'Ja. De', 'lijn bevat welk elk letter van alfabet', origin_text

    except Exception as e:
        return 'Nee, weet niet waarom'


with open('file_for_strings.txt', 'a+', encoding='UTF-8') as file:
    for line in range(C_NUMBER_LINES):
        file.write(f"{input('Beste gebruiker, een paar lijnen tekst in te geven: ')}\n")
    file.seek(0)
    f = file.readlines()
    for num, line in enumerate(f, 1):
        print(f'{num} - {is_containing_all_letters(line)}')
