# 1. Maak een programma dat de gebruiker vraagt om zijn leeftijd en naam. Indien de gebruiker
# minstens 18 jaar is vraag dan ook als hij een rijbewijs heeft of niet Als output willen we het
# volgende zien:
# Hallo “naam”, u bent x jaar. U bent A en B.
# A = meerderjarig of minderjarig
# en B = indien ouder dan 65 “en gepensioneerd”.
# Voorbeeld output:
# Hallo Voornaam Familienaam u bent 68 jaar.
# U bent meerderjarig en gepensioneerd.
# U heeft een rijbewijs
# Hallo Voornaam Familienaam u bent 68 jaar.
# U bent meerderjarig en gepensioneerd.
# Hallo Voornaam Familienaam u bent 40 jaar.
# U bent meerderjarig.
# U heeft een rijbewijs
# Hallo Voornaam Familienaam u bent 40 jaar.
# U bent meerderjarig.
# Hallo Voornaam Familienaam u bent 16 jaar.
# U bent minderjarig.
# De gebruiker mag slechts 5x een verkeerde waarde ingeven bij de leeftijd anders stopt het
# programma. Geef een foutmelding dan “U heeft 5 pogingen gehad om een correcte leeftijd in te
# geven, het programma stopt nu”. Gebruik hiervoor een recursieve functie en geen loop !

C_AGE_18 = 18
C_AGE_PENSION = 65
C_ATTEMPTS = 5
C_OUTPUT_HALLO = 'Hallo'
C_OUTPUT_UBENT = 'U bent'
C_OUTPUT_JAAR = 'jaar'


class Person:
    __name = ''
    __age = 0
    __driving_license = False

    def __init__(self, name, age, driving_license):
        self.__name = name
        self.__age = age
        self.__driving_license = driving_license

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__driving_license = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: str):
        self.__age = value

    @property
    def driving_license(self):
        return self.__driving_license

    @driving_license.setter
    def driving_license(self, value: str):
        self.__driving_license = value


def get_input():
    """
    :return: 0 if user gave correct information, 1 -- if his/her attempt to input information failed
    """
    age = input('Uw leeftijd: ')
    try:
        age = int(age)
        name = input('Uw naam: ')
        if age < C_AGE_18:
            print(f'{C_OUTPUT_HALLO} {name}, {C_OUTPUT_UBENT} {age} {C_OUTPUT_JAAR}')
            print('U bent minderjarig')

        else:
            license_ = input('Als u een rijbewijs heeft, druk \'y\', als geen rijbewijs, druk \'n\' ')

            if age >= C_AGE_PENSION:
                print(f'{C_OUTPUT_HALLO}{name}, {C_OUTPUT_UBENT} {age} {C_OUTPUT_JAAR}')
                print(f'{C_OUTPUT_UBENT} meerderjarig en gepensioneerd')
            else:
                print(f'{C_OUTPUT_HALLO}{name}, {C_OUTPUT_UBENT} {age} {C_OUTPUT_JAAR}')
                print(f'{C_OUTPUT_UBENT} meerderjarig')
            if license_.strip().lower() == 'y':
                print('U heeft een rijbewijs')
            else:
                print('U heeft geen rijbewijs')
        return 0
    except Exception as e:
        print(f'Uw leftijd moet een cijfer zijn, {e}')
        return 1


def start_rec(failed_attempts=0):
    """

    :param failed_attempts:
    :return: self up to 5 attempts
    """
    if failed_attempts == C_ATTEMPTS:
        print(f"U heeft {C_ATTEMPTS} pogingen gehad om een correcte leeftijd in te geven, het programma stopt nu")
    else:
        result = get_input()
        start_rec(failed_attempts + result)


start_rec(0)
