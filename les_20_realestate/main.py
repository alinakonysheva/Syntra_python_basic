from realestate import RealEstate, RealEstateList
from inputs import GetInput, validate_number_within_range
from utils import print_spacer


def do_main():
    type_estate = validate_number_within_range(
        GetInput.get_int, 'Type van uw plot (1: huis, 2: appartement, 3: grond, 4: handelspand): ', 1, 4,
        'Incorrect estate type')
    epc = validate_number_within_range(
        GetInput.get_int, 'Type EPC (0-2000): ', 0, 2000,
        'Incorrect EPC value')
    address = GetInput.get_text('Type adres van uw plot: ')
    description = GetInput.get_text('Type omschrijving van uw plot: ')
    price = validate_number_within_range(GetInput.get_float, 'Type prijs van uw plot: ', 0, 10000000,
                                         'Price has to be positive and less than 10000000')
    new_est = RealEstate(address, price, description, epc, type_estate)
    print(new_est)

if __name__ == '__main__':
    do_main()
