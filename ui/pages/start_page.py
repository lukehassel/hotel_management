import tkinter as tk

from ui.pages.create_customer_page import CreateCustomerPage
from ui.pages.room_administration_page import RoomAdministrationPage
from ui.pages.customer_administration_page import CustomerAdministrationPage

class StartPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #p1 = CreateCustomerPage(self)
        p2 = RoomAdministrationPage(self)
        w = tk.Label(self, text="Trash-Hotel Bearbeitungs_Zentrum", bg = "red")
        w.pack()

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        b1 = tk.Button(buttonframe, text="CustomerPage")
        b2 = tk.Button(buttonframe, text="RoomAdministration")
        b3 = tk.Button(buttonframe, text="CustomerAdministrationPage")

        b1.grid(row=0, column=2, padx='10', pady='30', sticky='ew')
        b2.grid(row=1, column=2, padx='10', pady='30', sticky='ew')
        b3.grid(row=2, column=2, padx='10', pady='30', sticky='ew')

