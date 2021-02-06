__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

import tkinter as tk

from ui.pages.create_customer_page import CreateCustomerPage
from ui.pages.customer_administration_page import CustomerAdministrationPage
from ui.pages.plan_administration_page import PlanAdministrationPage
from ui.pages.room_administration_page import RoomAdministrationPage


class StartPage(tk.Frame):
    """
    This class creates the Page where all the other pages are called from.
    """

    def __init__(self, *args, **kwargs):
        """
        This method creates the page.
        """
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

    def btn2(self):
        """
        A callback for the button btn2.
        """
        self.p2.refresh()
        self.p2.lift()

    def btn3(self):
        """
        A callback for the button btn3.
        """
        self.p3.refresh()
        self.p3.lift()
