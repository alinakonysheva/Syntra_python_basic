# Vraag een gebruiker welk broodje hij wilt hebben.
# Hij krijgt de keuze uit 5 broodjes: smos, martino, krab, tonijn, kip curry.
# De broodjes krijgen een nummer en de gebruiker krijgt een keuzelijst te zien.
# De broodjes slagen we op in een dictionary in een aparte file.

from broodjes import buns as range_buns

choice_not_done = True
chosen_buns = []
while choice_not_done:
    try:
        for number_bun, name_bun in range_buns.items():
            print(f'druk {number_bun}: als u {name_bun[0]} wilt, dat kost {name_bun[1]}')
        user_choice = int(input('Welk broodje wilt u hebben?   '))
        if user_choice in range_buns.keys():
            chosen_buns.append(range_buns[user_choice])
            print(f'U hebt al {chosen_buns} gekozen, dat kost {chosen_buns}')
            choice_not_done = input('Zou u graag nog één broodje kiezen? Als nee,\
druk gewoon \'enter\', als ja -- druk een letter of een cijfer  ')
        else:
            print('Geen geldige keuze')
    except ValueError:
        print('druk gewoon cijfer')

