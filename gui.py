import tkinter
from tkinter import *
from tkinter import ttk
from scrape_gui import get_data_gui

window = Tk()
window.title('Sąskaitų generatorius')

frame = Frame(window)
frame.pack()

#Pasirikti kieno vardu išrašoma sąskaita
user_name_label = Label(frame, text = "Kieno vardu išrašoma sąskaita?")
user_name_label.grid(row = 0, column = 0)
user_var = StringVar(frame)
pick_user = OptionMenu(frame,user_var,"Tado","Pamelos")
pick_user.grid(row = 0, column = 1)
#user_var.get() reik įtraukti į "Generuoti sąskaitą" mygtuką

#Sąskaitos datos zona
invoice_date_label = Label(frame, text='Sąskaitos data:')
invoice_date_label.grid(row = 1, column = 0)
invoice_date = Entry(frame)
invoice_date.grid(row=1,column=1)

#Scrape zona, kur bus galima įvesti nuorodą ir scrapins duomenis ir pateiks juos lentelėje
scrape_link_label = Label(frame, text="Nukopijuokite nuorodą duomenų scrapinimui:")
scrape_link_label.grid(row=2,column=0)

#Padarom mygtuką scrapinimui
def scrape_action():
    scrape_url = scrape_link.get()
    scraped_data = get_data_gui(scrape_url)
    table.insert('',0,values=scraped_data)

scrape_button = Button(frame,text='Scrape',command=scrape_action)
scrape_button.grid(row=3,column=1)

scrape_link = Entry(frame)
scrape_link.grid(row=2,column=1)

#Atiduodam nuskaitytus duomenis į lentelę
columns = ('name','code','address','boss','info')
columns_names = ('Pavadinimas','Kodas','Adresas','Vadovas','Papildoma informacija')
table = ttk.Treeview(frame,columns=columns,show='headings')
table.grid(row=4,column=0,columnspan=5)
for i in range(len(columns)):
    table.heading(columns[i],text=columns_names[i])

#Sukuriam po įvesties langelį įmonės info pakeitimui ir mygtuką su kuriuo galima papildyti info
name_add = Entry(frame)
name_add.grid(row=5,column=0)
code_add = Entry(frame)
code_add.grid(row=5,column=1)
address_add = Entry(frame)
address_add.grid(row=5,column=2)
boss_add = Entry(frame)
boss_add.grid(row=5,column=3)
info_add = Entry(frame)
info_add.grid(row=5,column=4)


#test button function
def ok():
    print("user is ",user_var.get())
#test button
button = Button(frame, text="OK", command=ok)
button.grid(row=15,column=0)


window.mainloop()