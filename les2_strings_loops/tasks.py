# mylist = ['1', '2', '3']
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
#
# #################
# second_list = []
# number = int(input('enter a number  '))
# if number % 2 == 0:
#     second_list.append(number / 2)
#     second_list.sort()
# else:
#     second_list.append(number)
#
# number = int(input('enter a number  '))
# if number % 2 == 0:
#     second_list.append(number / 2)
#     second_list.sort()
# else:
#     second_list.append(number)
#
# number = int(input('enter a number  '))
# if number % 2 == 0:
#     second_list.append(number / 2)
#     second_list.sort()
# else:
#     second_list.append(number)
#
# print(second_list)

# for i in range(9):
#     print(i)

# task 1
# try:
#     list_of_numbers = []
#     for i in range(5):
#         i = int(input('give me any number between 1 end 10   '))
#         list_of_numbers.append(i)
#     print(list_of_numbers)
# except ValueError as e:
#     print('that has to be a number')
#
# ######################
# # task 2
# try:
#     list_of_numbers_2 = []
#     for i in range(5):
#         i = int(input('give me any number between 1 end 60   '))
#         if i % 9 == 0:
#             list_of_numbers_2.append(i)
#     print(list_of_numbers_2)
# except ValueError as e:
#     print('that has to be a number')

# task 3
text_for_counting = input('enter some text: ')
array_with_numbers_from_the_text = []
array_with_letters_from_the_text = []
for symbol in text_for_counting:
    if symbol.isnumeric():
        array_with_numbers_from_the_text.append(symbol)
    if symbol.isalpha():
        array_with_letters_from_the_text.append(symbol)
print(f'number of numbers in your text is {len(array_with_numbers_from_the_text)}\n\
number of letters in your text is {len(array_with_letters_from_the_text)} ')

