from sys import stdout
from time import sleep

def print_message(message, end='\n'):
    character_list = list(message) if (type(message)==str) else []
    for character in character_list:
        print(character, end='')
        stdout.flush()
        sleep(0.025)
    print('', end=end)