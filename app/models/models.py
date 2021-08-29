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


add_person()
show_persons()
