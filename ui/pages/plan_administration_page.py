import tkinter as tk

from domain.entities.room.double_room import DoubleRoom
from domain.entities.room.single_room import SingleRoom
from domain.entities.room.suite import Suite
from domain.usecase.reception_usecase import ReceptionUseCase
from ui.pages.page import Page
from domain.usecase.plan_usecase import get_duty_roster, set_duty_roster


class PlanAdministrationPage(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        # label.pack(side="top", fill="both", expand=True)

        # self.frame = tk.Frame(self).pack()

        self.create_input_fields()
        self.create_btn()

        title = tk.Label(self,
                         text="Plan Verwaltung")
        title.config(font=("Courier", 44))
        # title.pack(side="top", fill="both", expand=True)
        title.place(x=20, y=35)

    def create_input_fields(self):
        inputFrame = tk.Frame(self)

        tk.Label(inputFrame,
                 text="Clicke Um zu\n bearbeiten:").grid(sticky="W", column=1, row=0)
        self.text = tk.Text(inputFrame, width=30, height=10)
        # Loads the contents of the duty_roster text file into the field
        self.text.insert(tk.INSERT, get_duty_roster())
        self.text.grid(sticky="W", column=2, row=0)

        inputFrame.place(x=20, y=150)

    def create_btn(self):
        btnFrame = tk.Frame(self, borderwidth=20)
        tk.Button(btnFrame,
                  text='Save', command=self.save).grid(column=1, row=0)
        btnFrame.pack(side="bottom")

    def save(self):
        content = self.text.get("1.0", 'end-1c')
        set_duty_roster(content)
