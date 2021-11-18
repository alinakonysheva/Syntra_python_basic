from random import sample
# Maak een lotto spel. Vraag de gebruiker om 6 getallen en druk dan af als hij de winnende combinatie heeft
# output
# --- Lotto ---
# --- kies uw 6 cijfers ---
# Geef een getal op (getal 1): 1 Geef een getal op (getal 2): 2 Geef een getal op (getal 3):
# 3 Geef een getal op (getal 4): 4 Geef een getal op (getal 5): 5 Geef een getal op (getal 6): 6
# - De winnende combinatie is : [4, 7, 15, 17, 25, 30] - we gaan nu kijken als u gewonnen heeft
# U heeft 1 correct cijfers
# U heeft de volgende cijfers correct: [4]
# лучше делать условие вместо while , sys.exit -- лучше использовать, вместо break, break как ручные тормоза



header = '--- Lotto ---'
rules_of_lotto = ''
range_lotto_min = 1
range_lotto_max = 50
size_of_lottofield = 6


def creation_of_win_combination(range_lotto_min_, range_lotto_max_, size_of_lottofield_):
    try:
        win_combination = sample(range(range_lotto_min_, range_lotto_max_), size_of_lottofield_)
    except ValueError:
        print('de grotte van de lottokaart moet kleiner zijn dan de reeks getallen die bij het spel betrokken zijn')

    print(f'{header:>20}\n --- kies uw {size_of_lottofield_} cijfers --- \n \
Cijfers moeten tussen {range_lotto_min_} en {range_lotto_max_} zijn')
    return win_combination


def get_user_combination(size_of_lottofield_, range_lotto_min_,range_lotto_max_):
    user_combination = []

    for guess in range(size_of_lottofield_):
        while True:
            try:
                user_number = int(input(f'Uw huidige lotto kaart -- {user_combination}. \n Geef een getal op (getal {guess + 1}) -- '))
                if user_number > range_lotto_max_:
                    print(f'Uw getal is groter dan {range_lotto_max_}')
                elif user_number < range_lotto_min_:
                    print(f'Uw getal is minder dan {range_lotto_min_}')
                elif user_number in user_combination:
                    print(f'Uw getal staat al op uw lotto card')
                else:
                    break
            except ValueError:
                print('dat moet een getal zijn')
        user_combination.append(user_number)
        return user_combination

    win_combination = creation_of_win_combination(range_lotto_min, range_lotto_max, size_of_lottofield)

    print(f'De winnende combinatie is : {win_combination}')

    # random.sample gives as unique results, user has to enter unique results, so we can use sets

    lucky_numbers = list(set(win_combination) & set(user_combination))
    print(f'U heeft {len(lucky_numbers)} correct cijfers')
    if len(lucky_numbers):
        print(f'U heeft de volgende cijfers correct: {lucky_numbers}')

