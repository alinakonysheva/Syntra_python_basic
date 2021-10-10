import sys
# Maak een programma dat de huidige directory afdrukt en alle files en folders gaat afdrukken
'''import os
my_dir = os.getcwd()
print(my_dir)
for i in os.listdir(my_dir):
   print(i)'''

# Maak een file “dummy.txt” aan, zet die op je systeem in je documenten map. Maak een kopie naar een andere map
'''import shutil
my_file = '/Users/ally/Documents/dummy.txt'
to_file = '/Users/ally/Documents/test.txt'
if os.path.exists(my_file):
    shutil.copy(my_file, to_file)'''

# In je documenten of development folder druk daar alle files af (kies zelf een extensie .jpg, .jpeg, .txt
# of gewoon .py files)
'''import os

print('\n\n --- glob --- \n\n')
import glob
mydir = '/Users/ally/Documents/Dutch'
print(os.path.exists(mydir))
# сделать лист из файлов с расширением pages в определенной папке 
mylist = glob.glob(os.path.join(mydir, '*.pages'))

for item in mylist:
    print(item)'''

print(sys.version)
print(sys.path)

import sys
params_length = len(sys.argv)
print(params_length)