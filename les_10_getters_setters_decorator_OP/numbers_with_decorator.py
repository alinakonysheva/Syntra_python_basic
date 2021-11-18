class Numbers:
    first_number = 0
    second_number = 0

    def __init__(self, first=0, second=0):
        self.first_number = first
        self.second_number = second

    def get_sum(self):
        '''
        to sum given numbers
        :return: sum
        '''
        try:
            sum_ = self.first_number + self.second_number
        except ValueError:
            return 0
        return sum_

    def get_subtraction(self):
        '''
        to subtract first number out second number
        :return: subtraction
        '''
        try:
            subtraction = self.first_number - self.second_number
        except ValueError:
            return 0
        return subtraction

    def get_multiplication(self):
        '''
        to multiply given numbers
        :return: multiplication
        '''
        try:
            multiplication = self.first_number * self.second_number
        except ValueError:
            return 0
        return multiplication

    def get_division(self):
        '''
        to divide first number by second number
        :return: result of division. If second number = 0, them returns str 'infinity'
        '''
        try:
            if self.second_number != 0:
                division = self.first_number * self.second_number
            else:
                return 'infinity'
        except ValueError:
            return 0
        return division
