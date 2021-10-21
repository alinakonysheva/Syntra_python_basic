import sys
import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password='Sandal11',
                              host='127.0.0.1',
                              database='myconnection')
cursor = cnx.cursor()
C_DB_NAME = 'myconnection'
table_drivers = "CREATE TABLE `drivers` (\
  `id` int(11) NOT NULL AUTO_INCREMENT,\
  `name` varchar(45) NOT NULL,\
  `age` tinyint(250) NOT NULL,\
  PRIMARY KEY (`id`)\
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"


try:
    cursor.execute("drop table myconnection.drivers")
    cursor.execute(table_drivers)
    add_new_driver = True
    while add_new_driver:
        driver_name = input('geef me een naam van een chauffer:  ')
        driver_age = input('geef me een leeftijd van een chauffer:  ')
        cursor.execute(f"INSERT INTO myconnection.drivers (name, age) values('{driver_name}','{driver_age}');")
        add_new_driver = input('Zou u graag nog één chauffer toevoegen? Als ja,\
 druk een letter of een cijfer, als nee -- druk gewoon \'enter\' --   ')
    cursor.execute("select name, age from myconnection.drivers order by age asc;")
    list_with_tuples_age_name = cursor.fetchall()
    if list_with_tuples_age_name:
        for row in list_with_tuples_age_name:
            print(f'{row[0]} -- {row[1]}')
    else:
        print('geen gegevens gevonden')


# fetchone - > next ?
except mysql.connector.Error as err:
    print("Failed creating database: {}".format(err))
    exit(1)


cnx.close()

