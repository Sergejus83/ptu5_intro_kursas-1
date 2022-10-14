import sqlite3

connector = sqlite3.connect("data_20221013/zmones.db")
cursor = connector.cursor()

with connector:
    while True:
        vardas = input("Iveskite Varda arba '!' kad iseiti arba '.' kas ivesti nauja: ")
        if vardas == "!":
            break
        elif vardas == ".":
            print("----------NAUJAS draugas---------")
            naujas_vardas = input("Vardas: ")
            nauja_pavarde = input("Pavarde: ")
            naujas_email = input("email: ")
            cursor.execute('INSERT INTO draugai (first_name, last_name, email) VALUES (?, ?, ?)', 
            (naujas_vardas, nauja_pavarde, naujas_email, ))
            connector.commit()
        else:
            # select_query = f'SELECT * FROM draugai WHERE first_name LIKE "%{vardas}%"' 
            # print(f'...vykdome {select_query}...')
            # cursor.execute(f'SELECT * FROM draugai WHERE first_name LIKE "%{vardas}%"') # %- if nepilnai varda

            select_query = 'SELECT * FROM draugai WHERE first_name LIKE ?'
            cursor.execute(select_query, (f'%{vardas}%', )) # %- if nepilnai varda
            rezultatas = cursor.fetchall()
            if rezultatas:
                print('Radau tokius dragus: ')
                for draugas in rezultatas:
                    print(f" - {draugas[0]} {draugas[1]} ({draugas[2]})")
            else:
                print("Tokio draugo varda nera")
    print("Bye!")




