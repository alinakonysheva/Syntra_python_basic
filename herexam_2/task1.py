# 1. Maak een programma dat de gebruiker vraagt om een woord van minstens 2 en maximaal 10 letters in te geven.
# Er mogen geen cijfers of tekens ingegeven worden. De gebruiker krijgt slechts “5 beurten” om dit correct te doen.
# Gebruik een recursieve functie voor de 5 beurten en geen loop. Toon dan van elke letter de plaats in het alfabet
# Voorbeeld output
# Uw ingegevens woord is : bal letter b – plaats 2 in alfabet letter a – plaats 1 in alfabet letter l –
# plaats 12 in alfabet
import string

# Generate constants


C_WORD_LENGTH_MIN = 2
C_WORD_LENGTH_MAX = 10


class Letter:
    __letter = ''
    __number = 0
    list_with_letters = list(string.ascii_lowercase)
    list_with_numbers = [i + 1 for i in range(len(list_with_letters))]
    dict_with_num_let = dict(zip(list_with_letters, list_with_numbers))

    def __init__(self, letter):
        self.__letter = letter
        self.__number = self.dict_with_num_let[self.__letter]

    def __str__(self):
        return f'letter {self.__letter} – plaats {self.__number} in alfabet'


class Word:
    __letters = []

    def __init__(self, word: str):
        self.__word = word
        self.__len_min = C_WORD_LENGTH_MIN
        self.__len_max = C_WORD_LENGTH_MAX
        self.__letters = list(map(lambda x: Letter(x), word))

    def print_out(self):
        for letter in self.__letters:
            print(letter)


def input_from_user():
    word = input('Geef, alstublieft, een woord van minstens 2 en maximaal 10 letters'
                 ' Er mogen geen cijfers of tekens ingegeven worden.  ')
    return word.strip().lower()


def word(value: str, count=0):
    if count <= 5:
        word_length = len(value)
        if C_WORD_LENGTH_MAX >= word_length >= C_WORD_LENGTH_MIN:
            list_with_all_letters = list(filter(lambda x: x.isalpha(), value))
            if len(list_with_all_letters) == len(value):
                w = Word(value)
                w.print_out()
            else:
                count += 1
                print('Er mogen geen cijfers of tekens ingegeven worden')
                return word(input_from_user(), count)

        else:
            print('een woord van minstens 2 en maximaal 10 letters')
            count += 1
            return word(input_from_user(), count)


def do_run():
    word(input_from_user())


if __name__ == '__main__':
    do_run()
