from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import datetime
import parser


def click():
    label['text'] = str(par.getValue(combo1.get()) / par.getNominal(combo1.get()) * float(txt.get()) /
                        par.getValue(combo2.get()) * par.getNominal(combo2.get()))


window = Tk()
window.title("Converter. ИКБО-10-18. Грачев А.А.")
window.geometry("640x480")

tabs = ttk.Notebook(window)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tabs.add(tab1, text="Конвертер")
tabs.add(tab2, text="График")

url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={}".format(datetime.datetime.now().strftime("%d/%m/%Y"))
response = urllib.request.urlopen(url)
par = parser.Parser(response)

combo1 = ttk.Combobox(tab1)
combo1["values"] = par.getCorrectValutes()
combo1.grid(column=0, row=0)

combo2 = ttk.Combobox(tab1)
combo2["values"] = par.getCorrectValutes()
combo2.grid(column=1, row=0)

txt = Entry(tab1)
txt.grid(column=0, row=1)
label = Label(tab1, text="")
label.grid(column=1, row=1)
btn = Button(tab1, text="Рассчитать!", command=click)
btn.grid(column=2, row=0)

tabs.pack(expand=1, fill='both')
window.mainloop()
