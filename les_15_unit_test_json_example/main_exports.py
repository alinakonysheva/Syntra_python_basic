import json
from person import Person, get_person
from address import create_adress, get_adress_fields
from order import create_order
from shipment import create_shipment
from sigar import create_sigar
from inputs import get_input_item
from files_to_json_from_json import create_json_file, read_json_file


def main():
    # persoon aanmaken & adres
    person = get_person()
    print('geef uw adresgegevens in')
    get_adress_fields(person.address)
    # omzetten
    myjson = person.to_json
    # wegschrijven
    create_json_file(myjson)
    print(myjson)
    # pauze inlassen om file aan te passen
    get_input_item('pause, press anything to continue')

    '''
    # file terug inlezen
    person = Person('', '', 2000, 1, 1, 1)
    json_file_contents = read_json_file()
    person.from_json(json_file_contents)
    print(person)
    print(person.address)
    '''


if __name__ == '__main__':
    main()
