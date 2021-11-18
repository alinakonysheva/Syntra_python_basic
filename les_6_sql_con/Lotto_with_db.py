import sys
import mysql.connector
from random import sample

header = '--- Lotto ---'
rules_of_lotto = ''
range_lotto_min = 1
range_lotto_max = 50
size_of_lottofield = 6
# random.sample Return a k length list of unique elements chosen from the population sequence.
try:
    win_combination = sample(range(range_lotto_min, range_lotto_max), size_of_lottofield)
except ValueError:
    print('de grotte van de lottokaart moet kleiner zijn dan de reeks getallen die bij het spel betrokken zijn')

print(f'{header:>20}\n --- kies uw {size_of_lottofield} cijfers --- \n \
Cijfers moeten tussen {range_lotto_min} en {range_lotto_max} zijn')

C_DB_NAME = 'lotto'
table_win_numbers = "CREATE TABLE `win_numbers` (\
  `id` int(11) NOT NULL AUTO_INCREMENT,\
  `number` tinyint(11) NOT NULL,\
  PRIMARY KEY (`id`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"

table_user_numbers = "CREATE TABLE `user_numbers` (\
  `id` int(11) NOT NULL AUTO_INCREMENT,\
  `number` tinyint(11) NOT NULL,\
  PRIMARY KEY (`id`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"


try:
    cnx = mysql.connector.connect(user='root',
                                  password='Sandal11',
                              host='127.0.0.1',
                              database='lotto')
    cursor = cnx.cursor()

    cursor.execute("drop table IF EXISTS lotto.win_numbers")
    cursor.execute("drop table IF EXISTS lotto.user_numbers")
    cursor.execute(table_user_numbers)
    cursor.execute(table_win_numbers)
    cnx.commit()
    add_new_number = True
    guess = 1
   # list_with_user_numbers_check = []

    while add_new_number and guess < 7:
        user_number = int(input(f'Geef een getal op (getal {guess}) -- '))
        cursor.execute(f"INSERT INTO lotto.user_numbers (number) VALUES('{user_number}');")
        cnx.commit()
       # list_with_user_numbers_check.append(user_number)
        guess += 1
    cursor.execute("select id, number from lotto.user_numbers;")
    list_with_user_numbers = cursor.fetchall()
    print(list_with_user_numbers)
   # print(list_with_user_numbers_check)
except mysql.connector.Error as err:
    print(f"Failed database: {err}")
    sys.exit()

lucky_numbers = []

# переделать в табличку, добавить сейчас, дату добавления, id игры
for item in list_with_user_numbers:
    if item[1] in win_combination:
        lucky_numbers.append(item[1])

cnx.close()



# добавить триггер на добавление нового элемента 