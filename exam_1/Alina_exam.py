from random import sample

go_on_lotto = True

while go_on_lotto:
    C_LOTTOCARD = ['stier', 'vis', 'dolfijn', 'beer',
                   'giraf', 'hond', 'muis', 'orka',
                   'octopus', 'kat', 'slang', 'lama',
                   'olifant', 'pinguin', 'vogel', 'emoe',
                   'koala', 'paard', 'zebra', 'kangoeroe']

    C_SIZE_OF_LOTTOCARD = 5

    print('-' * 15, 'WWF loterij', '-' * 15)

    for i in range(len(C_LOTTOCARD)):
        print(f'{C_LOTTOCARD[i]:<12}', end='')
        if i in [3, 7, 11, 15, 19]:
            print()

    print('-' * 45)

    user_combination = []

    while len(user_combination) != C_SIZE_OF_LOTTOCARD:

        user_animal = input(f'Uw huidige lotto kaart -- {user_combination}.\nKies afbeelding uit de lijst: ')

        if user_animal == '':
            print('Uw afbeeld moet niet leeg zijn')
        elif user_animal not in C_LOTTOCARD:
            print(f'Uw afbeeld moet uit de dieren die erboven staan worden gekozen ')
        elif user_animal in user_combination:
            print(f'Uw afbeeld staat al op uw lotto formulier')
        else:
            user_combination.append(user_animal)

    print('Uw gekozen afbeelden: ', end='')
    for animal in user_combination:
        print(animal, end=' ')
    print()

    win_combination_numbers = sample(range(0, len(C_LOTTOCARD)), C_SIZE_OF_LOTTOCARD)

    win_combination_animals = []

    for number in win_combination_numbers:
        win_combination_animals.append(C_LOTTOCARD[number])

    print(f'De winnende afbeeldingen zijn:  ', end='')
    print(*(animal for animal in win_combination_animals))

    lucky_animals = list(set(win_combination_animals) & set(user_combination))
    number_lucky_animals = len(lucky_animals)
    print(f'U heeft {number_lucky_animals} correct afbeeldingen')
    print('U heeft de volgende afbeeldingen correct:  ', end='')
    if number_lucky_animals:
        for animal in lucky_animals:
            print(animal, end=' ')

    for i in range(len(C_LOTTOCARD)):
        if C_LOTTOCARD[i] in user_combination and C_LOTTOCARD[i] in lucky_animals:
            C_LOTTOCARD[i] = f'{"*" * len(C_LOTTOCARD[i])}'
        if C_LOTTOCARD[i] in user_combination:
            C_LOTTOCARD[i] = f'{"-" * len(C_LOTTOCARD[i])}'

    print()
    print('-' * 15, 'Uw resultaat', '-' * 15)

    for i in range(len(C_LOTTOCARD)):
        print(f'{C_LOTTOCARD[i]:<12}', end='')
        if i in [3, 7, 11, 15, 19]:
            print()
    print('-' * 45)
    go_on_lotto = input('Zou u graag nog één keer spelen? Als nee,\
 druk gewoon \'enter\', als ja -- druk een letter of een cijfer  ')
