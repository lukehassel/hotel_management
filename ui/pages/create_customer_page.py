import tkinter as tk

from ui.pages.page import Page


class CreateCustomerPage(Page):

    def show_entry_fields(self):
        print("Dein Name ist %s" % (self.e1.get()))

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        # label.pack(side="top", fill="both", expand=True)

        self.frame = tk.Frame(self).pack()

        self.create_input_fields()
        self.create_radios()
        self.create_btn()

        title = tk.Label(self.frame,
                 text="Neuer Kunde")
        title.config(font=("Courier", 44))
        title.place(x=20, y=35)

    def create_btn(self):
        btnFrame = tk.Frame(self, borderwidth=20)
        tk.Button(btnFrame,
                  text='Okay', command=self.show_entry_fields).grid(column=1, row=0)
        btnFrame.pack(side="bottom")

    def create_radios(self):
        radioFrame = tk.Frame(self.frame, borderwidth=40)

        var = tk.IntVar()
        rad1 = tk.Radiobutton(radioFrame, text='EinzelZimmer', value=1)

        rad2 = tk.Radiobutton(radioFrame, text='DoppelZimmer', value=2)

        rad3 = tk.Radiobutton(radioFrame, text='Suite', value=3)

        rad1.grid(sticky="W", column=0, row=0)
        rad2.grid(sticky="W", column=0, row=1)
        rad3.grid(sticky="W", column=0, row=2)

        radioFrame.place(x=200, y=175)

    def create_input_fields(self):
        inputFrame = tk.Frame(self.frame)

        tk.Label(inputFrame,
                 text="Name").grid(sticky="W", column=1, row=0)
        self.e1 = tk.Entry(inputFrame)
        self.e1.grid(sticky="W", column=2, row=0)

        tk.Label(inputFrame,
                 text="Wie Oft?").grid(sticky="W", column=1, row=1)
        self.e2 = tk.Entry(inputFrame)
        self.e2.grid(sticky="W", column=2, row=1)

        inputFrame.place(x=20, y=200)
