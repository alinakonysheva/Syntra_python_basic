# 1 Maak een tekstfile met 10 lijnen tekst in, noem deze file pythontest.txt.
# Lees deze file helemaal in en druk deze af

import os

'''with open('pythontest.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line {i}\n')
f.close()

with open('pythontest.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()
reader.close()'''
# 2 Lees de eerste 5 lijnen van deze file in druk deze af

'''with open('pythontest.txt', 'r') as reader:
    for i in range(5):
        line = reader.readline()
        print(line, end='')
reader.close()
'''
# 3 Vraag de gebruiker om een lijn tekst en voeg deze lijn toe aan je tekstfile en druk dan de file af

'''user_text = input('give me a line of text:  ')
with open('pythontest.txt', 'a') as f:
    f.write(f'{user_text}\n')
f.close()
with open('pythontest.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()

reader.close()
'''

# 4 Maak een programma dat lijn per lijn van die file gaat inlezen en dit in een lijst gaat zetten.
# Tel het aantal lijnen en druk dan af

'''with open('pythontest.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    counter = 0
    list_of_lines = []
    while line != '':  # The EOF char is an empty string
        list_of_lines.append(line)
        counter += 1
        line = reader.readline()

reader.close()

print(list_of_lines)
'''
# Schrijf een programma dat het langste woord uit je tekstfile gaat zoeken en afdrukken
# (je kan gebruik maken van de functie split() om woord per woord te krijgen op een lijn

'''with open('pythontest.txt', 'r') as reader:
    text_ = reader.read()
    list_with_words = text_.split(' ')
    length_longest_word = 0
    for word in list_with_words:
        if len(word.strip()) > length_longest_word:
            length_longest_word = len(word)
            longest_word = word
print(longest_word, length_longest_word)
reader.close()'''

with open('pythontest.txt', 'r') as reader:
    text_ = reader.read()
    list_with_words = text_.split(' ')

print(list_with_words)

from collections import defaultdict

D = defaultdict(list)
for i, item in enumerate(list_with_words):
    D[item].append(i)
D = {k: len(v) for k, v in D.items() if len(v) > 1}
how_offen = 0
which_word = ''

for k, v in D.items():
    if how_offen < v:
        how_offen = v
        which_word = k
print(which_word, how_offen)

reader.close()

# Schrijf een programma dat het aantal woorden telt in je file en geef
# dan het minst gebruikte woord en het meest gebruikte woord weer
'''from collections import defaultdict

D = defaultdict(list)
for i, item in enumerate(list_with_words):
    D[item].append(i)
D = {k: len(v) for k, v in D.items() if len(v) > 1}
how_offen = 0
which_word = ''

for k, v in D.items():
    if how_offen < v:
        how_offen = v
        which_word = k
print(which_word, how_offen)

reader.close()

'''
