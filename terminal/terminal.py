import socket
import datetime
import geocoder
import os
from time import sleep

tab = '    '
def show_info():    
    print('Terminal uTerm')
    print('Author: dz3n')
    print()
    print('Type "help" if you need help')
def show_help(commands):
    print('info        -> print information')
    print('ip          -> get your ip')
    print('date        -> get current date <year, month, day>')
    print('time        -> get current time <hours, minutes, seconds>')
    print('geolocation -> get your geolocation <city, region, country>')
    print('cls         -> clear shell')
    print('math        -> open math mode')
    print('tree        -> print content of input path')
def modify_string(string):
    return string.replace(" ", "")
def numbers_in_string(string):
        string = string.lower()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        numbers = '1234567890'
        for i in range(len(alphabet)):
            if alphabet[i] in string:
                return False
        for i in numbers:
            if i in string:
                return True
        return False
def is_empty(string):
    if string == '':
        return True
    for i in string:
        if i != ' ':
            return False
    return True
def math_mode():
    global tab
    print('Type "exit" to exit')
    while True:
        command = str(input(tab + '> '))
        if command == 'exit':
            print('You left math mode')
            break
        elif command != '' and not is_empty(command):
            if numbers_in_string(command):
                try:
                    print(tab + ' Answer: ' + str(eval(command)))
                except:
                    print(tab + ' Wrong expression')
            else:
                print(tab + ' Wrong expression')
def ask_root():
    global tab
    path = str(input(tab + "> Enter the path: "))
    tree(path)
def tree(path):
    global tab
    print(tab + 'Tree->')
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = tab + tab + ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = tab + tab + ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
commands = {
    'info' : 'show_info()',
    'ip' : 'print(socket.gethostbyname(socket.gethostname()))',
    'date' : 'print(datetime.date.today())',
    'time' : 'print(datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S"))',
    'geolocation' : 'print(geocoder.ip("me")[0])',
    'cls' : 'os.system(["cls", "cls"][os.name == os.sys.platform])',
    'help' : 'show_help(commands)',
    'math' : 'math_mode()',
    'tree' : 'ask_root()'
}
show_info()
while True:
    string = input('> ')
    string = modify_string(string)
    if string in commands:
        eval(commands[string])
    elif string == 'exit':
        print('Goodbuy!')
        sleep(2)
        break
    elif string != '' and not is_empty(string):
        print('Unknown command')
