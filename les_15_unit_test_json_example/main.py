from person import get_person
from address import create_adress, get_adress_fields
from order import create_order
from shipment import create_shipment
from sigar import create_sigar
from inputs import get_input_item

def main():
    person = get_person()
    print('geef uw adresgegevens in')
    get_adress_fields(person.address)
    print('-'*30)
    print('uw bestelling')
    # input vragen
    order = create_order(person, 1)
    sigars = [ create_sigar('1', 10.0, 2.0, 'Belgium', 1),
               create_sigar('2', 11.0, 3.0, 'Belgium', 2),
               create_sigar('3', 12.0, 4.0, 'Belgium', 0),
               create_sigar('4', 13.0, 6.0, 'Belgium', 3) ]
    for sigar in sigars:
        order.add_sigar(sigar)
    
    shipment = create_shipment(order, 4.95)
    is_same = get_input_item('is het leveradres hetzelfde als het adres van de persoon: (j voor j)').lower().strip() == 'j'
    if is_same:
        shipment.copy_address_from_person()
    else:
        print('ok geef dan het leveradres in')
        get_adress_fields(shipment.address)

    #output
    print('-'*30)
    print('uw bestelling')
    print('nr: {}'.format(order.nr))
    print('prijs bestelde goederen: {}'.format(order.price))
    print('bestelde sigaren')
    for sigar in order.sigars:
        print(sigar)

    
    print('totale prijs: {}'.format(order.price + shipment.price))
    print('leveradres is: {}'.format(shipment.address))

if __name__ == '__main__':
    main()



    
import unittest
  
