# advanced strings
'''
len()
.replace('i', 'j') -- заменяет один символ другим
.lower() -- lowercase
.upper() -- uppercase
.find('tekst') находит текст или символ


------
Slicing
text = 'banaan'
text[:3] = ban
text[3:] = aan
text[-4:] = naan
text[:-4] = ba
text[2:6] = naan
--------
.split(',') - разделение строки по запятой, например
'#'.join(mijn_lijst) -- gaat van een lijst saenplakken
.strip() - spacies vootaan en achteraan wissen
.title() - gaat camelcase tekst maken
.startwith('a') - начинается с а
.isalpha()(letters) -- проверяет на буквенности, если все буквы, то возвращает true
.isdigit() (все ли цифры)
'''


mytext = 'mijn Naam is Alina'
print(mytext.lower().replace('naam', 'voornaam'))
'''
Exeptions
try:
  print(x)
except NameError:
  print("Variable x is not defined")
  если добавить sys.exit(0) -- то дальше ничего работать не будет
else: -- выполняется если try отработал
  print("Something else went wrong")

finally:
всегда выполяется, вне зависимости от ошибок
'''
'''
mylist = list(('1', '2', '3'))

.append() - добавляет элемент в конец списка
.insert(позиция, значение)
.remove(значение)
.pop() -- удаляет последнее значение
.pop(1) -- удаляет первое значение, на первой позиции
.clear() -- опустошает значение листа

'''

'''
для for x in list:
для каждого элемента из списка делать что-то

range(n) -- от 0 до предпоследнего элемента, n - 1
range(k, l) -- от k до l - 1


i = 0
valid_input = False
while i < 10 and valid_input == False:
    waarde = str(input("geef een getal poging{}:".format(i+1)))
    if waarde.isnumeric():
    print(waarde)
    valid_input = True
    i +=1
'''