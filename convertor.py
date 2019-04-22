from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import matplotlib
import datetime
import parser


def click():
    label['text'] = str(par.getValue(combo1.get()) / par.getNominal(combo1.get()) * float(txt.get()) /
                        par.getValue(combo2.get()) * par.getNominal(combo2.get()))


def gClick():
    start_day = dates[combo4.current()]
    last_day = 1
    print(str(start_day.month))
    if str(start_day.month) in ["1", "3", "5", "7", "8", "10", "12"]:
        last_day = datetime.datetime(int(start_day.year), int(start_day.month), int(start_day.day) + 30)
    if str(start_day.month) in ["4", "6", "9", "11"]:
        last_day = datetime.datetime(int(start_day.year), int(start_day.month), int(start_day.day) + 29)
    if str(start_day.month) == "2":
        if int(start_day.year) % 4 == 0:
            last_day = datetime.datetime(int(start_day.year), int(start_day.month), int(start_day.day) + 28)
        else:
            last_day = datetime.datetime(int(start_day.year), int(start_day.month), int(start_day.day) + 27)

    x = []
    y = []
    for i in range(int(start_day.day), int(last_day.day) + 1):
        d = datetime.datetime(start_day.year, start_day.month, i)
        x.append(i)
        y.append(parser.getValue(d, combo3.get()))
    fig.clear()
    plt.plot(x, y)
    plt.grid()
    canvas.draw()


window = Tk()
window.title("Converter. ИКБО-10-18. Грачев А.А.")
window.geometry("1280x720")

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
combo2["values"] = combo1["values"]
combo2.grid(column=1, row=0)

txt = Entry(tab1)
txt.grid(column=0, row=1)
label = Label(tab1, text="")
label.grid(column=1, row=1)
btn = Button(tab1, text="Рассчитать!", command=click)
btn.grid(column=2, row=0)

combo3 = ttk.Combobox(tab2)
combo3["values"] = combo1["values"]
combo3.grid(column=0, row=2)

dates = [datetime.datetime(int(datetime.datetime.today().year) - 1, m, 1) for m in range(1, 13)]

combo4 = ttk.Combobox(tab2)
combo4["values"] = [d.strftime('%B %Y') for d in dates]
combo4.grid(column=0, row=1)

btn1 = Button(tab2, text="Построить!", command=gClick)
btn1.grid(column=0, row=3)

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  # import не вверху а после matplotlib.use('TkAgg'), так как иначе не работает в mac OS

fig = plt.figure()
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab2)
plot_widget = canvas.get_tk_widget()
fig.clear()
# plt.plot([0], [0])
plt.grid()
plot_widget.grid(column=1, row=4)

tabs.pack(expand=1, fill='both')
window.mainloop()
