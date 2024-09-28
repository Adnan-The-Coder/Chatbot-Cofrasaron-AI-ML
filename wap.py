# Count The Number of Alphabets and digits 
# Uppercase and Lowercase 
# Spaces 
# And the other characters 
from typing import Container


while True:
    print(' ')
    string = input("Please enter string: ")
    print(' ')

    if ' ' in string:
        print(string,'contains space')
    if string.islower() :
        print(string,"is in lowercase")
        print(' ')
    if string.isnumeric():
        print(string,'contains numbers')
    if string.isspace():
        print(' ')
        print(string,'contains only space')
    if string.isupper():
        print(' ')
        print(string,"is in uppercase")
    if 'exit' in string:
        print('Exitting...')
        exit()


    number_of_string = len(string)
    print('The number of characters in string are',number_of_string)