# -*- coding: utf-8 -*-
from model import Person
import view


def showAll():
    people_in_db = Person.getAll()
    return view.showAllView(people_in_db)


def showContactInfo():
    people_in_db = Person.getAll()
    return view.showContactInfo(people_in_db)


def start():
    view.startView()
    input = raw_input()
    if input == '1':
        return showAll()
    elif input == '2':
        return showContactInfo()
    else:
        return view.endView()


if __name__ == "__main__":
    start()
