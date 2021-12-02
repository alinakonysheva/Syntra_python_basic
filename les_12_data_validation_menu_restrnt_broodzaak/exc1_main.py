from datetime import datetime
from mydatetime import MyDateTime, format_date

def main():
    d = MyDateTime(datetime(2022, 2, 2))
    print('volgende maand: {}'.format(d.doprint(d.next_month)))
    print('vorige maand: {}'.format(d.doprint(d.last_month)))
    print('morgen: {}'.format(d.doprint(d.tomorrow)))
    print('gisteren: {}'.format(d.doprint(d.yesterday)))
    print('volgend jaar: {}'.format(d.doprint(d.next_year)))
    print('vorig jaar: {}'.format(d.doprint(d.last_year)))
    print('vandaag: {}'.format(d.doprint(d.today)))


if __name__ == '__main__':
    main()