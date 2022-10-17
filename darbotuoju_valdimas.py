from datetime import date, datetime
from darbotuoju_modelis import Darbuotojai, engine
from sqlalchemy.orm import sessionmaker
from tkinter import Tk, Frame, Label, Button, Entry, Listbox, SINGLE, END, RIGHT, LEFT, Y, PhotoImage
session = sessionmaker(bind=engine)()

def print_employee():
    print("----all staff----")
    employees = session.query(Darbuotojai).all()
    for employee in employees:
        print(employee)

def new_employee():
    print("---Naujas darbotuojas---")
    try:
        first_name = input("Vardas: ")
        last_name = input("Pavarde: ")
        birth_day = datetime.strptime(input("Gimimo data (YYYY-MM-DD): "), "%Y-%m-%d")
        position = input("Pareigos: ")
        salary = float(input("Atlyginimas: "))
        employed_from = datetime.strptime(input("Dirba nuo: (YYYY-MM-DD): "), "%Y-%m-%d")
    except ValueError:
        print("Klaida: patikinti ivesti, gal vietoj skaiciu ivesta raide")
        return
    else:
        employee = Darbuotojai(first_name, last_name, birth_day, position, salary, employed_from)
        session.add(employee)
        session.commit()
        print(f'naujas darbotuojas {employee} sukurtas SEKMINGAI!')

def input_employee():
    print_employee()
    try:
        employee_id = int(input("iveskite keiciamo darbotojo ID: "))
    except ValueError:
        print("Klaida: keiciamo darbotuojo ID ne skaicius!")
        return None
    else:
        if employee_id:
            employee = session.query(Darbuotojai).get(employee_id)
            if employee:
                return employee
            else:
                print(f"KLAIDA: Darbotuojas su ID: {employee_id} neegzistuoja.")
                return None

def update_employee():
    employee = input_employee()
    if employee:
        try:
            first_name = input(f"Vardas ({employee.first_name}): ")
            last_name = input(f"Pavarde ({employee.last_name}): ")
            position = input(f"Pareigos ({employee.position}): ")
            salary = float(input(f"Atlyginimas ({employee.salary}): ")  or 0)
            birth_day = datetime.strptime(input(f"Gimimo data ({datetime.date(employee.birth_day)}): "), "%Y-%m-%d")
            employed_from = datetime.strptime(input(f"Dirba nuo: ({datetime.date(employee.employed_from)}): "), "%Y-%m-%d")
        except ValueError:
            print("KLAIDA: kaina turi buti skaicius")
        else:
            if len(first_name) > 0:
                employee.first_name = first_name
            if len(last_name) > 0:
                employee.last_name = last_name
            if len(position) > 0:
                employee.position = position
            if salary > 0:
                employee.salary = salary
            if birth_day == True:
                employee.birth_day = birth_day
            if employed_from > True:
                employee.employed_from = employed_from 
            session.commit()
            print(f"Darbuotojas {employee} atnaujintas sekmingai")

def delete_employee():
   trinamas = input_employee()
   if trinamas:
    trinamas = session.query(Darbuotojai).get(trinamas)
    session.delete(trinamas)
    session.commit()
    print(f" Darbotojas {trinamas} istrintas sekmingai")

while True:
    print("*** Darbotuoju duomenu base ***")
    print(" Ka darom ?: ")
    print(" 0 - iseiti ")
    print(" 1 - rodyti visus darbotuojus")
    print(" 2 - ivesti nauja darbotuoja")
    print(" 3 - pakeisti darbotuoja ")
    print(" 4 - trinti darbotuoja")
    pasirinkimas = input("Pasirinkite: ") #.casefold()
    if pasirinkimas == "0":
        print("viso gero!")
        break
    if pasirinkimas == "1":
        print_employee()
    if pasirinkimas == "2":
        new_employee()
    if pasirinkimas == "3":
        update_employee()
    if pasirinkimas == "4":
        delete_employee()
    else:
        print(" - dar karta - ")

