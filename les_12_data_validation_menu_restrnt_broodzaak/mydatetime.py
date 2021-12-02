from datetime import datetime, timedelta

class MyDateTime():
    __date = datetime.now()
    
    def __init__(self, value=None):
        if value is not None:
            self.mydate = value
        else:
            self.mydate = datetime.now()
    
    @property
    def mydate(self):
        return self.__date
    
    @mydate.setter
    def mydate(self, value):
        if value is not None and type(value) is datetime:
            self.__date = value
        else:
            print('mydate not set')
    
    @property 
    def yesterday(self):
        return self.mydate + timedelta(days=-1) 

    @property
    def tomorrow(self):
        return self.mydate + timedelta(days=+1) 

    @property
    def today(self):
        return datetime.now() 

    @property
    def last_month(self):
        year, month, day = self.mydate.year, self.mydate.month - 1, self.mydate.day
        if month < 1:
            year -= 1
            month = 12
        
        return datetime(year, month, day, self.mydate.hour, self.mydate.minute, self.mydate.second)


    @property
    def next_month(self):
        year = self.mydate.year 
        month = self.mydate.month + 1
        day = self.mydate.day
        if month > 12:
            year += 1
            month = 1
        
        return datetime(year, month, day, self.mydate.hour, self.mydate.minute, self.mydate.second)

    @property
    def next_year(self):      
        return datetime(self.mydate.year + 1, self.mydate.month, self.mydate.day, 
            self.mydate.hour, self.mydate.minute, self.mydate.second)


    @property
    def last_year(self):       
        return datetime(self.mydate.year - 1, self.mydate.month, self.mydate.day, 
            self.mydate.hour, self.mydate.minute, self.mydate.second)


    def __str__(self):
        return self.doprint(self.mydate)


    def doprint(self, adate):
        return '{}'.format(adate.strftime("%d-%m-%Y %H:%M:%S"))

