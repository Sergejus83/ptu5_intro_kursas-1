# from darbotuoju_modelis import*
# from darbotuoju_valdimas import *
from dbcon import *
from tkinter import Tk, Frame, Label, Button, Entry, Listbox, SINGLE, END, RIGHT, LEFT, Y, PhotoImage

def perziureti():
    vardas=laukas_vardas.get()
    pavarde=laukas_pavarde.get()
    gim_data=laukas_gim_data.get()
    pareigos=laukas_pareigos.get()
    atlyginimas=laukas_atlyginimas.get()
    dirba_nuo=laukas_dirba_nuo.get()
    employee = f"Vardas: {vardas}, Pavarde: {pavarde}, gimimo data: {gim_data}, Pareigoas: {pareigos}, \
Atlyginomas: {atlyginimas} eur, Dirba nuo: {dirba_nuo}"
    if employee:
        print(employee)
    else:
        print("nieko niera")

def ivesti():
    pass
def redaguoti():
    pass
def istrinti():
    laukas_vardas.delete(0, END)
    laukas_pavarde.delete(0, END)
    laukas_gim_data.delete(0, END)
    laukas_atlyginimas.delete(0, END)
    laukas_pareigos.delete(0, END)
    laukas_dirba_nuo.delete(0, END)

pagr_langas = Tk()
pagr_langas.title("Darbotuoju katalogas")
pagr_langas.geometry("500x300")
pagr_langas.iconbitmap(r"data_20221013/pyicon.png")



virs_frame=Frame(pagr_langas)
virs_frame.pack()
apat_frame=Frame(pagr_langas)
apat_frame.pack()
migtukas_frame= Frame(pagr_langas)
boksas = Listbox(apat_frame, selectmode=SINGLE)

laukas_vardas = Entry(virs_frame)
laukas_pavarde = Entry(virs_frame)
laukas_gim_data = Entry(virs_frame)
laukas_pareigos = Entry(virs_frame)
laukas_atlyginimas = Entry(virs_frame)
laukas_dirba_nuo = Entry(virs_frame)

uzrasas1 = Label(virs_frame, text= "Iveskite darbotuoja: ", width= 50)
uzrasas_vardas=Label(virs_frame, text="Vardas: ")
uzrasas_pavarde=Label(virs_frame, text="Pavarde: ")
uzrasas_gim_data=Label(virs_frame, text="Gimimo data: ")
uzrasas_pareigos=Label(virs_frame, text="Pareigos: ")
uzrasas_atlyginimas=Label(virs_frame, text="Atlyginimas: ")
uzrasas_dirba_nuo=Label(virs_frame, text="Dirba nuo: ")
uzrasas_tuscias=Label(virs_frame, text="         ")


mig_ivesti=Button(virs_frame, text="Ivesti", command=ivesti).grid(row=1, column=3, sticky= "W")
mig_redaguoti=Button(virs_frame, text="Redaguoti", command=redaguoti) #com
mig_istrinti=Button(virs_frame, text="Istrinti", command=istrinti) #com
mig_perziureti=Button(virs_frame, text="Perziureti", command=perziureti) #com

uzrasas1.grid(row=0, columnspan=2, sticky= "E")
laukas_vardas.grid(row=1, column=1)
laukas_pavarde.grid(row=2, column=1)
laukas_gim_data.grid(row=3, column=1)
laukas_pareigos.grid(row=4, column=1)
laukas_atlyginimas.grid(row=5, column=1)
laukas_dirba_nuo.grid(row=6, column=1)

uzrasas_vardas.grid(row=1, column=0, sticky= "E")
uzrasas_pavarde.grid(row=2, column=0, sticky= "E")
uzrasas_gim_data.grid(row=3, column=0, sticky= "E")
uzrasas_pareigos.grid(row=4, column=0, sticky= "E")
uzrasas_atlyginimas.grid(row=5, column=0, sticky= "E")
uzrasas_dirba_nuo.grid(row=6, column=0, sticky= "E")
uzrasas_tuscias.grid(row=1, column=2)

mig_redaguoti.grid(row=2, column=3, sticky= "W")
mig_istrinti.grid(row=3, column=3, sticky= "W")
mig_perziureti.grid(row=4, column=3, sticky= "W")


# laukas1.bind("<Return>")
# migtukas1.bind("<Button-1>")
# migtukas2.bind
# migtukas2.bind


pagr_langas.mainloop()

