from tkinter import (Tk, Frame, Label, StringVar, OptionMenu, Entry, Button,
                     IntVar, Checkbutton)
from tkinter import ttk
from scrape_for_gui import get_data
from make_invoice import *
from num2words import num2words
from datetime import date


window = Tk()
window.title('Sąskaitų generatorius')

frame = Frame(window)
frame.pack()

user_name_label = Label(frame, text="Kieno vardu išrašoma sąskaita?")
user_name_label.grid(row=0, column=0)
user_name = StringVar(frame)
pick_user = OptionMenu(frame, user_name, *TEMPLATES.keys())
pick_user.grid(row=0, column=1)

invoice_date_label = Label(frame, text='Sąskaitos data (mmmm-mm-dd):')
invoice_date_label.grid(row=1, column=0)
invoice_date = Entry(frame)
invoice_date.grid(row=1, column=1)
checkbox_var = IntVar(frame)
checkbox = Checkbutton(frame, text="Naudoti šiandienos datą",
                       variable=checkbox_var)
checkbox.grid(row=1, column=2)

# Scrape zona, kur bus galima įvesti nuorodą ir scrapins duomenis ir
# pateiks juos lentelėje

scrape_link_label = Label(
    frame, text="Nukopijuokite nuorodą duomenų scrapinimui:")
scrape_link_label.grid(row=2, column=0)


def scrape_action():
    scrape_url = scrape_link.get()
    global scraped_info
    scraped_info = get_data(scrape_url)
    return scraped_info


def fill_table():
    table.insert('', 0, values=scrape_action())


scrape_button = Button(frame, text='Scrape', command=fill_table)
scrape_button.grid(row=3, column=1)

scrape_link = Entry(frame, width=50)
scrape_link.grid(row=2, column=1, columnspan=2)

columns = ('name', 'code', 'address', 'boss', 'info')
columns_names = (
    'Pavadinimas',
    'Kodas',
    'Adresas',
    'Vadovas',
    'Papildoma informacija')
table = ttk.Treeview(frame, columns=columns, show='headings', height=2)
table.grid(row=4, column=0, columnspan=5)
for i in range(len(columns)):
    table.heading(columns[i], text=columns_names[i])

# Sukuriam po įvesties langelį įmonės info pakeitimui

name = Entry(frame, width=25)
name.grid(row=5, column=0)
code = Entry(frame, width=25)
code.grid(row=5, column=1)
address = Entry(frame, width=25)
address.grid(row=5, column=2)
boss = Entry(frame, width=25)
boss.grid(row=5, column=3)
extra_info = Entry(frame, width=25)
extra_info.grid(row=5, column=4)

add_info_label = Label(
    frame,
    text="Norėdami įvesti įmonės duomenis arba pakeisti duomenis gautus iš rekvizitai.lt įveskite duomenis į langelius viršuje")
add_info_label.grid(row=6, column=1, columnspan=3)

services_name_label = Label(frame, text="Paslaugos pavadinimas")
services_name_label.grid(row=7, column=0)
services_amount_label = Label(frame, text="Paslaugų kiekis")
services_amount_label.grid(row=7, column=1)
unit_price_label = Label(frame, text="Vieneto kaina")
unit_price_label.grid(row=7, column=2)
total_price_label = Label(frame, text="Bendra suma")
total_price_label.grid(row=7, column=3)

services_name = Entry(frame, width=25)
services_name.grid(row=8, column=0)
services_amount = Entry(frame, width=25)
services_amount.grid(row=8, column=1)
unit_price = Entry(frame, width=25)
unit_price.grid(row=8, column=2)


def count_total_price():
    return round((int(services_amount.get()) * float(unit_price.get())), 2)


def show_total_price():
    total_price = Label(frame, text=count_total_price())
    total_price.grid(row=8, column=3)


total_price_button = Button(
    frame,
    text="Skaičiuoti bendrą sumą",
    command=show_total_price)
total_price_button.grid(row=8, column=4)


def generate():
    added_info = [name, code, address, boss, extra_info]
    company_info = {
        'name': '',
        'code': '',
        'address': '',
        'boss': '',
        'extra_info': ''}
    try:
        scraped_info
        for scraped, added, key in zip(scraped_info, added_info, company_info):
            company_info[key] = added.get() if added.get() else scraped
    except NameError:
        for added, key in zip(added_info, company_info):
            company_info[key] = added.get()

    total_price_data = "{:.2f}".format(count_total_price())
    invoice_date_data = str(date.today()) if checkbox_var.get() == 1\
                        else invoice_date.get()
    invoice_info = {'invoice_date': invoice_date_data,
                    'invoice_number': f'{invoice_date_data}-01',
                    'services': services_name.get(),
                    'amount': services_amount.get(),
                    'unit_price': unit_price.get(),
                    'sum': total_price_data,
                    'total_LT': num2words(total_price_data, to="currency",
                                          lang="lt", currency='EUR'),
                    'total_EN': num2words(total_price_data, to="currency",
                                          lang="en", currency='EUR')
                    }
    make_invoice(invoice_info, company_info, user_name.get())


button = Button(frame, text="Generuoti sąskaitą", command=generate)
button.grid(row=10, column=2)


window.mainloop()
