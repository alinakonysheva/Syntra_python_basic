from inputs import get_input_item
from temperature import get_year_input, create_yearlist, print_year, change_unit, read_file
from utils import print_spacer

def print_menu():
    print_spacer()
    print('Maak uw keuze')
    print_spacer()
    print('1. geef gegevens in voor een jaar')
    print('2. bekijk gegevens in voor een jaar')
    print('3. wijzig naar andere eenheid')
    print('4. inlezen')
    print('5. stoppen')   


def do_main():
    yearlist = create_yearlist()
    inp = 1
    while inp in [1, 2, 3, 4]:
        print_menu()
        inp = get_input_item('maak uw keuze: ', 1)
        if inp == 1:
            get_year_input(yearlist)
        elif inp == 2:
            print_year(yearlist)
        elif inp == 3:
            change_unit(yearlist)
        elif inp == 4:
            read_file(yearlist)
    yearlist.save()




if __name__ == '__main__':
    do_main()