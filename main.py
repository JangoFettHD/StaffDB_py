# -*- coding: utf-8 -*-
import json

# init
db_directory = "db.txt"
pension = 65
hours = 8


#######


class database:
    '''
    @staticmethod
    def element(index, db):
        return staff(db[staff][index - 1]["name"], db[staff][index - 1]["post"], db[staff][index - 1]["age"],
                     db[staff][index - 1]["cph"], db[staff][index - 1]["mf"])
    '''

    @staticmethod
    def printelement(index, db):
        print(database.getStaff(db["staff"][index]))

    @staticmethod
    def load():
        db = {}
        with open(db_directory, "r+") as f:
            content = str(f.read())
            f.seek(0)
            if not (len(content) == 0):
                json1_data = json.loads(content)
                db = json1_data
                print('\x1b[6;30;42m' + "@LOG: " + str(db) + '\x1b[0m')
        return db

    @staticmethod
    def save(db):
        f = open(db_directory, "r+")
        f.seek(0)
        f.truncate()
        temp = str(db)
        str_dct = temp.replace("\'", "\"")
        f.write(str_dct)
        f.close()

    @staticmethod
    def add_dct_to_db(dct, db):
        if "staff" in db.keys():
            db["staff"].append(dct)
        else:
            db["staff"] = [dct]
        database.save(db)

    @staticmethod
    def sumofpayments(db):
        err = '\033[91m' + "База данных пуста!" + '\033[0m'
        if "staff" in db.keys():
            if not (len(db["staff"]) == 0):
                summ = 0
                for i in range(len(db["staff"])):
                    persona = database.getStaff(db["staff"][i])
                    summ += persona.payroll_preparation(1)
                print(summ*input_int("Введите количество дней: "))
            else:
                print(err)
        else:
            print(err)

    @staticmethod
    def staffpensia(db):
        err = '\033[91m' + "База данных пуста!" + '\033[0m'
        if "staff" in db.keys():
            if not (len(db["staff"]) == 0):
                ye=input_int("Введите количество лет: ")
                for i in range(len(db["staff"])):
                    persona = database.getStaff(db["staff"][i])
                    if persona.years_until_retirement()==ye:
                        print(persona)
            else:
                print(err)
        else:
            print(err)


    @staticmethod
    def add(db):
        dct = {}

        name = ""
        while len(name) == 0:
            name = input("Введите ФИО: ")
        dct["name"] = name

        age = -1
        while int(age) < 1:
            age = input_int("Введите возраст: ")
        dct["age"] = age

        post = ""
        while len(post) == 0:
            post = input("Введите должность: ")
        dct["post"] = post

        cph = -1
        while int(cph) < 0:
            cph = input_int("Введите зарплату в час: ")
        dct["cph"] = cph

        mf = -1
        while float(mf) < 0:
            mf = input_float("Введите повышающий коэффициент: ")
        dct["mf"] = mf

        # pers = staff(dct["name"], dct["post"], dct["age"], dct["cph"], dct["mf"])
        database.add_dct_to_db(dct, db)

    @staticmethod
    def getStaff(dct):
        return staff(dct["name"], dct["post"], dct["age"], dct["cph"], dct["mf"])

    @staticmethod
    def printallstaff(db):
        err = '\033[91m' + "База данных пуста!" + '\033[0m'
        if "staff" in db.keys():
            if not (len(db["staff"]) == 0):
                for i in range(len(db["staff"])):
                    print(str(i + 1) + ") " + str(database.getStaff(db["staff"][i])))
            else:
                print(err)
        else:
            print(err)

    @staticmethod
    def remove(db):
        err = '\033[91m' + "База данных пуста!" + '\033[0m'
        if "staff" in db.keys():
            if not (len(db["staff"]) == 0):
                element = -1
                while True:
                    element = input_int("Введите id для удаления: ")
                    if 0 < element < len(db["staff"]) + 1:
                        break
                    else:
                        print('\033[91m' + "Такого элемента не существует!" + '\033[0m')
                db["staff"].pop(element - 1)
                database.save(db)
            else:
                print(err)
        else:
            print(err)


#######

class staff():
    name = "Steve"
    post = "Developer"
    age = 22
    cph = 50.00
    mf = 1.0

    def __init__(self, name, post, age, cph, mf):
        self.name = name
        self.post = post
        self.age = age
        self.cph = cph
        self.mf = mf

    def __str__(self):
        return "{0}, Должность: {1}, Возраст: {2}, Зарплата в час: {3}, Повышающий коэффициент {4}".format(self.name,
                                                                                                           self.post,
                                                                                                           self.age,
                                                                                                           self.cph,
                                                                                                           self.mf)

    def payroll_preparation(self, days):
        payroll_preparation = days * (self.cph * hours) * self.mf
        #print(payroll_preparation)
        return payroll_preparation

    def years_until_retirement(self):
        return pension - self.age


#######
'''
print(type(db))
db = database.load(db)
print(type(db))
database.printelement(0, db)
database.printallstaff(db)
database.add(db)
'''


def input_int(str="", err='\033[91m' + "Нужно вводить число, а не букву!" + '\033[0m'):
    while True:
        inp = ""
        try:
            inp = int(input(str))
        except ValueError:
            print(err)
        if isinstance(inp, int):
            return inp


def input_float(str="", err='\033[91m' + "Нужно вводить число, а не букву!" + '\033[0m'):
    while True:
        inp = ""
        try:
            inp = float(input(str))
        except ValueError:
            print(err)
        if isinstance(inp, float):
            return inp


def show_staff():
    err = '\033[91m' + "База данных пуста!" + '\033[0m'
    if "staff" in db.keys():
        if not (len(db["staff"]) == 0):
            index = -1
            while not (0 < index < len(db["staff"]) + 1):
                index = input_int("Введите id работника: ", '\033[91m' + "Данного работника не существует!" + '\033[0m')
            persona = database.getStaff(db["staff"][index - 1])
            print(persona)
            menu = ["Рассчитать заработок за нес-ко дней.", "Узнать ск-ко лет осталось до пенсии.", "Назад"]
            while True:
                print("Введите , что вы хотите сделать:")
                for i in range(len(menu)):
                    print("{0} - {1}".format(i + 1, menu[i]))
                selection = input_int(">>  ")
                if 0 < selection < (len(menu) + 1):
                    if selection == 1:
                        print(persona.payroll_preparation(input_int("Введите количество дней: ")))
                    elif selection == 2:
                        print(persona.years_until_retirement())
                    elif selection == 3:
                        break
                else:
                    print('\033[91m' + "Вы хотите открыть несуществующий элемент меню!" + '\033[0m')
        else:
            print(err)
    else:
        print(err)


def show_menu():
    menu = ["Добавить работника.", "Удалить работника.", "Показать всех работников.", "Выбрать работника.",
            "Вывести суммарную зарплату всех работников.", "Вывести работников, которым до пенсии осталось N лет.",
            "Выйти"]
    while True:
        print("Введите , что вы хотите сделать:")
        for i in range(len(menu)):
            print("{0} - {1}".format(i + 1, menu[i]))

        selection = input_int(">>  ")
        if 0 < selection < (len(menu) + 1):
            if selection == 1:
                database.add(db)
            elif selection == 2:
                database.remove(db)
            elif selection == 3:
                database.printallstaff(db)
            elif selection == 4:
                show_staff()
            elif selection == 5:
                database.sumofpayments(db)
            elif selection == 6:
                database.staffpensia(db)
            elif selection == 7:
                break
        else:
            print('\033[91m' + "Вы хотите открыть несуществующий элемент меню!" + '\033[0m')


db = database.load()
show_menu()
