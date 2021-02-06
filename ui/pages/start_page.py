import tkinter as tk

from ui.pages.create_customer_page import CreateCustomerPage
from ui.pages.customer_administration_page import CustomerAdministrationPage
from ui.pages.plan_administration_page import PlanAdministrationPage
from ui.pages.room_administration_page import RoomAdministrationPage


class StartPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = CreateCustomerPage(self)
        self.p2 = CustomerAdministrationPage(self)
        self.p3 = RoomAdministrationPage(self)
        self.p4 = PlanAdministrationPage(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Neuer Kunde", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Kunden Verwaltung", command=self.btn2)
        b3 = tk.Button(buttonframe, text="Zimmer Verwaltung", command=self.btn3)
        b4 = tk.Button(buttonframe, text="Plan Verwaltung", command=self.p4.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        p1.show()

    def btn1(self):
        pass
    def btn2(self):
        self.p2.refresh()
        self.p2.lift()

    def btn3(self):
        self.p3.refresh()
        self.p3.lift()