import sqlite3

connector = sqlite3.connect('data_auto/auto.db')
cursor = connector.cursor()


search_query = '''SELECT * FROM auto \
WHERE auto_marke LIKE ?\
AND modelis LIKE ?\
AND spalva LIKE ?\
AND metai BETWEEN ? AND ?\
AND kaina BETWEEN ? AND ?'''

def insert():
    n_auto_marke = input("-- marke: ")
    n_modelis = input("-- modelis: ")
    n_spalva = input("-- spalva: ")
    n_metai = input("-- pag. metai: ")
    n_kaina = input("-- kaina: ")
    with connector:
        cursor.execute('INSERT INTO auto (auto_marke, modelis, spalva, metai, kaina) VALUES (?, ?, ?, ?, ?)',\
             (n_auto_marke, n_modelis, n_spalva, n_metai, n_kaina))
    print(f'{n_auto_marke} {n_modelis} ({n_metai}) successfully created!')


def search():
    auto_marke = input('-- Auto: ')
    modelis = input('-- Model: ')
    spalva = input('-- Color: ')
    metai_nuo = input('-- Year from: ')
    metai_iki = input('-- Year to: ')
    kaina_nuo = input('-- Price from: ')
    kaina_iki = input('-- Price to: ')
    search_tuple = (
        auto_marke + '%' if auto_marke else '%',
        modelis +'%' if modelis else '%',
        spalva + '%' if spalva else '%',
        int(metai_nuo) if metai_nuo else 1900,
        int(metai_iki) if metai_iki else 2022,
        int(kaina_nuo) if kaina_nuo else 0,
        int(kaina_iki) if kaina_iki else 1000000 )

    with connector:
        cursor.execute(search_query, search_tuple)
        rezultatas = cursor.fetchall()

    for i in rezultatas:
        print("paeskos rezultatas: ", i)
    print(f'Is viso rado: {len(rezultatas)}')


while True:
    pasirinkimas = input("Iveskite: \n 's' - ieskoti auto info! \n 'exit' - iseiti \n 'ok' - ivesti naujo auto duomenis:\n Ivesti cia: ")
    if pasirinkimas == "exit":
        print("---------Programa UZDARYTA!---------")
        break
    elif pasirinkimas == "ok":
        print("----------NAUJAS auto---------")
        insert()
    elif pasirinkimas == "s":
        print("----------auto paeska---------")
        search()



























# with connector:
#     while True:
#         auto = input("Iveskite: \n 's' - ieskoti auto info! \n 'exit' - iseiti \n 'ok' - ivesti naujo auto duomenis:\n_: ")
#         if auto == "exit":
#             break
#         elif auto == "ok":
#             print("----------NAUJAS auto---------")
#             n_auto_marke = input("-- marke: ")
#             n_modelis = input("-- modelis: ")
#             n_spalva = input("-- spalva: ")
#             n_metai = input("-- pag. metai: ")
#             n_kaina = input("-- kaina: ")
#             cursor.execute('INSERT INTO auto (auto_marke, modelis, spalva, metai, kaina) VALUES (?, ?, ?, ?, ?)', 
#             (n_auto_marke, n_modelis, n_spalva, n_metai, n_kaina, ))
#             connector.commit()
#         elif auto == "s":
#             select_query = 'SELECT * FROM auto \
#             WHERE auto_marke LIKE ? \
#             AND  modelis LIKE ?,\
#             AND spalva LIKE?,\
#             AND metai LIKE ?,\
#             AND kaina LIKE ?'

#             marke = input('-- Auto: ')
#             modelis = input('-- Model: ')
#             spalva = input('-- Color: ')
#             metai_nuo = input('-- Year from: ')
#             metai_iki = input('-- Year to: ')
#             kaina_nuo = input('-- Price from: ')
#             kaina_iki = input('-- Price to: ')
#             select_tuple = (
#                 marke + '%' if marke else '%',
#                 modelis + '%' if modelis else '%',
#                 spalva + '%' if spalva else '%',
#                 int(metai_nuo) if metai_nuo else 1900,
#                 int(metai_iki) if metai_iki else 2022,
#                 int(kaina_nuo) if kaina_nuo else 0,
#                 int(kaina_iki) if kaina_iki else 1000000
#             )


#             # select_query = 'SELECT * FROM auto WHERE auto_marke LIKE ?'
#             cursor.execute(select_query, select_tuple) # % %- if nepilnai varda
#             rezultatas = cursor.fetchall()
#             if rezultatas:
#                 print('-- auto yra sarase: ')
#                 for info in rezultatas:
#                     print(f" -- {info[0]} ---- {info[1]} ---- spalva: {info[2]} ----  {info[3]} metu ---- {info[4]} eur")
#             else:
#                 print("-- tokios auto nera, patikrinkite ivedima, Please!!!--")
#     print("-- Laukiam sugriztant!--")









































#     import sqlite3

# connector = sqlite3.connect('data_auto/auto.db')
# cursor = connector.cursor()



# with connector:
#     while True:
#         auto = input("Iveskite auto info! 'exit' kad iseiti arba 'ok' kad ivesti auto duomenis: ")
#         if auto == "exit":
#             break
#         elif auto == "ok":
#             print("----------NAUJAS auto---------")
#             n_auto_marke = input("-- marke: ")
#             n_modelis = input("-- modelis: ")
#             n_spalva = input("-- spalva: ")
#             n_metai = input("-- pag. metai: ")
#             n_kaina = input("-- kaina: ")
#             cursor.execute('INSERT INTO auto (auto_marke, modelis, spalva, metai, kaina) VALUES (?, ?, ?, ?, ?)', 
#             (n_auto_marke, n_modelis, n_spalva, n_metai, n_kaina, ))
#             connector.commit()
#         else:
#             select_query = 'SELECT * FROM auto WHERE auto_marke LIKE ?'
#             cursor.execute(select_query, (f'%{auto}%', )) # % %- if nepilnai varda
#             rezultatas = cursor.fetchall()
#             if rezultatas:
#                 print('-- auto yra sarase: ')
#                 for info in rezultatas:
#                     print(f" -- {info[0]} ---- {info[1]} ---- spalva: {info[2]} ----  {info[3]} metu ---- {info[4]} eur")
#             else:
#                 print("-- tokios auto nera, patikrinkite ivedima, Please!!!--")
#     print("-- Laukiam sugriztant!--")