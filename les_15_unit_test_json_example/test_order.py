import unittest
from datetime import date, datetime
from person import create_person
from sigar import Sigar, create_sigar
from order import Order, create_order

C_NUMBER = 100

C_1_NAME = 'Cohiba'
C_1_PRICE = 2.4
C_1_LENGTH = 15
C_1_COUNTRY = 'Cuba'
C_1_TYPE = 2
C_1_MILD = 'bitter'

C_2_NAME = 'Ashton'
C_2_PRICE = 2.1
C_2_LENGTH = 15.6
C_2_COUNTRY = 'Cuba'
C_2_TYPE = 1
C_2_MILD = 'mild'

class TestOrder(unittest.TestCase):

    def create_sigar(self, sigartype: int) -> Sigar:
        """create sigars helper function

        Args:
            sigartype (int): create a sigar of type 1 or type 2

        Returns:
            [Sigar]: sigar object
        """
        if sigartype == 2:
            return create_sigar(C_2_NAME, C_2_LENGTH, C_2_PRICE, C_2_COUNTRY, C_2_TYPE) 
        else:
            return create_sigar(C_1_NAME, C_1_LENGTH, C_1_PRICE, C_1_COUNTRY, C_1_TYPE) 


    def setUp(self):
        p = create_person('Kristof', 'Degros', 1979, 9, 2, 1)
        self.person = p
        self.order = Order(p, C_NUMBER)
        s1 = create_sigar(C_1_NAME, C_1_LENGTH, C_1_PRICE, C_1_COUNTRY, C_1_TYPE)
        self.order.add_sigar(s1)
    
    def test_price(self):
        self.assertEqual(self.order.price, C_1_PRICE)

    def test_price(self):
        self.assertEqual(self.order.nr, C_NUMBER)

    def test_create_order(self):
        o = create_order(self.p, 1)
        self.assertEqual(o.nr, 1)
        self.assertEqual(len(o.sigars), 0)
        self.assertEqual(o.price, 0.0)
        self.assertEqual(o.price_minimum, 10.0)
        now = datetime.today()
        self.assertEqual(o.date.year, now.year)
        self.assertEqual(o.date.month, now.month)
        self.assertEqual(o.date.day, now.day)
        

    def test_sigar_length(self):
        self.assertEqual(len(self.order.sigars), 1)

    def test_add_sigar(self):
        self.order.add_sigar(self.create_sigar(2))
        self.assertEqual(len(self.order.sigars), 2)

    def test_date(self):
        now = datetime.today()
        self.assertEqual(self.order.date.year, now.year)
        self.assertEqual(self.order.date.month, now.month)
        self.assertEqual(self.order.date.day, now.day)
        self.assertGreaterEqual(self.order.date.hour, 0)
        self.assertGreaterEqual(self.order.date.minute, 0)
        self.assertGreaterEqual(self.order.date.second, 0)              
       
    def test_minimum_met(self):
        # initial price 2.4
        self.assertEqual(self.order.minimum_met, False)
        self.order.add_sigar(self.create_sigar(1))
        # price +2.4 -> 4.8 
        self.assertEqual(self.order.minimum_met, False)
        self.order.add_sigar(self.create_sigar(2))
        # price +2.4 -> 7.2
        self.assertEqual(self.order.minimum_met, False)
        self.order.add_sigar(self.create_sigar(2))
        # price +2.1 -> 9.3
        self.assertEqual(self.order.minimum_met, False)
        # price +2.4 -> 11.7        
        self.order.add_sigar(self.create_sigar(1))
        self.assertEqual(self.order.minimum_met, True)
        '''
        # remove item -2.4
        self.order.del_sigar(self.create_sigar(1))
        self.assertEqual(self.order.minimum_met, False)
        '''

    def test_nr(self):
        self.assertEqual(self.order.nr, C_NUMBER)
        with self.assertRaises(AttributeError) as cm:
            self.order.nr = 1900
            self.assertIn("can't set attribute", str(cm.exception))

    def test_person(self):
        self.assertIsNotNone(self.order.person)
        order = Order(None, C_NUMBER)
        self.assertRaises(ValueError, order.person)


        

if __name__ == '__main__':
    unittest.main()
