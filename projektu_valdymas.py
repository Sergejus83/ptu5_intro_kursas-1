from projekto_modelis import Projektas, engine
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)()

def print_projects():
    print("----PROJEKTAI----")
    print("(#, pavadinimas, kaina, sukurta)")
    projects = session.query(Projektas).all()
    for project in projects:
        print(project)

def new_project():
    print("---Naujas projektas---")
    try:
        name = input("pavadinimas: ")
        price = float(input("kaina: "))
    except ValueError:
        print("Klaida: kaina ne skaicius!")
        return
    else:
        project = Projektas(name, price)
        session.add(project)
        session.commit()
        print(f"Projektas {project} sukurtas sekmingai!")

def input_project():
    print_projects()
    try:
        project_id = int(input("iveskite trinama projekto ID: "))
    except ValueError:
        print("Klaida: kaina trinamas projekto ID ne skaicius!")
        return None
    else:
        if project_id:
            project = session.query(Projektas).get(project_id)
            if project:
                return project
            else:
                print(f"Projektas su ID: {project_id} neegzistuoja")
                return None

def update_project():
    project = input_project()
    if project:
        try:
            name = input(f"pavadinimas ({project.name}): ")
            price = float(input(f"kaina ({project.price}): ")  or 0)
        except ValueError:
            print("KLAIDA: kaina turi buti skaicius")
        else:
            if len(name) > 0:
                project.name = name
            if price > 0:
                project.price = price
            session.commit()
            print(f"Projektas {project} atnaujintas sekmingai")
        # end of updating

def delete_project():
   trinamas = input_project()
   if trinamas:
    trinamas = session.query(Projektas).get(trinamas)
    session.delete(trinamas)
    session.commit()
    print(f" Projektas {trinamas} istrintas sekmingai")

while True:
    print("===Projektu valdymo duomenu base===")
    print("Pasirinkita: ")
    print("- q: iseiti ")
    print("- r: rodyti visus projektus: ")
    print("- n: naujas projektas ")
    print("- u: pakeisti projekta ")
    print("- d: istrinti projekta ")
    pasirinkimas = input("Pasirinkite: ").casefold()
    if pasirinkimas == "q":
        print("viso gero!")
        break
    if pasirinkimas == "r":
        print_projects()
    if pasirinkimas == "n":
        new_project()
    if pasirinkimas == "u":
        update_project()
    if pasirinkimas == "d":
        delete_project()
    else:
        print("KLaida: Blogas pasirinkimas, rinkites is naujo!")


