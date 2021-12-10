# 2. Vraag de gebruiker om een ongekend aantal lijnen tekst in te geven.
# Print dan voor elke lijn af hoeveel hoofdletters en hoeveel kleine letters er gebruikt zijn.
# Elke lijn krijgt een volgnummer in de output.
# (Testen of het een hoofd of kleine letter is kan door isupper(), islower() op een karakter of string)
# Voorbeeld output:
# tekst 1: “Dit is een Test” hoofdletters: 2
# kleine letters: 10
# tekst 2: “Iets Anders” hoofdletters: 2
# kleine letters: 8

C_STOP_CHAR = 'n'


def input_from_user():
    line = input('Geef, alstublieft, een line van text:  ')
    return line


def get_lines() -> list:
    quit_ = ''
    list_with_lines = []
    while quit_ != C_STOP_CHAR:
        line = input_from_user()
        list_with_lines.append(line)
        quit_ = input('Als dat genoeg is, type letter \'n\'').strip().lower()
    return list_with_lines


def analyse_str(line: str) -> list:
    big_letters = 0
    small_letters = 0
    for letter in line:
        if letter.islower():
            small_letters += 1
        if letter.isupper():
            big_letters += 1
    return {line: (big_letters, small_letters)}


def print_output(list_with_lines: list):
    for num_str, str in enumerate(list_with_lines, 1):
        print(f'tekst {num_str}:', end=' ')
        print(str)
        tuple_with_count_letters = analyse_str(str)[str]
        print(f'hoofdletters: {tuple_with_count_letters[0]}, kleine letters: {tuple_with_count_letters[1]}')


def do_run():
    text = get_lines()
    print_output(text)


if __name__ == '__main__':
    do_run()
