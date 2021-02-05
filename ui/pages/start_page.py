import tkinter as tk

from ui.pages.create_customer_page import CreateCustomerPage
from ui.pages.customer_administration_page import CustomerAdministrationPage
from ui.pages.page import Page
from ui.pages.room_administration_page import RoomAdministrationPage


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)


class StartPage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = CreateCustomerPage(self)
        self.p2 = CustomerAdministrationPage(self)
        self.p3 = RoomAdministrationPage(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=self.btn2)
        b3 = tk.Button(buttonframe, text="Page 3", command=self.btn3)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

    def btn1(self):
        pass
    def btn2(self):
        self.p2.refresh()
        self.p2.lift()

    def btn3(self):
        self.p3.refresh()
        self.p3.lift()