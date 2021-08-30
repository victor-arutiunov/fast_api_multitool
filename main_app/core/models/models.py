from pony.orm import *

db = Database()

db.bind(provider='postgres', user='test_user',
        password='0000', host='', database='fast_api_multitool_db')


class Users(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    last_name = Optional(str)
    position = Optional(str)


db.generate_mapping(create_tables=True)


@db_session
def add_person():
    person1 = Users(name=input("Name: "), last_name=input(
        "Last name: "), position=input("Position: "))


@db_session
def show_persons():
    Users.select().show()


class Bcolors:
    '''
    Colors set
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


INITIAL = True

while True:
    if INITIAL:
        print(Bcolors.OKGREEN + "Initialization...")
        print(Bcolors.OKGREEN + 'Print "stop" to terminate the program')
        INITIAL = False
    command = input(Bcolors.HEADER + "Waiting for your commands, Captain: ")
    if command == 'show':
        show_persons()
    elif command == 'add':
        add_person()
    elif command == 'stop':
        print(Bcolors.WARNING + "Shut down program")
        break
    else:
        print(Bcolors.WARNING + "Wrong command")
