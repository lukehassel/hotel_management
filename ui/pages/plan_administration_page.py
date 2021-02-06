__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

import tkinter as tk

from domain.usecase.plan_usecase import get_duty_roster, set_duty_roster
from ui.pages.page import Page


class PlanAdministrationPage(Page):

    """
    This class creates the Page where the reception can create the new plans.
    """

    def __init__(self, *args, **kwargs):
        """
        This class creates the Page.
        """
        Page.__init__(self, *args, **kwargs)

        self.create_input_fields()
        self.create_btn()

        title = tk.Label(self,
                         text="Plan Verwaltung")
        title.config(font=("Courier", 44))
        title.place(x=20, y=35)

    def create_input_fields(self):
        """
        This method creates the input fields of the page.
        """
        inputFrame = tk.Frame(self)

        tk.Label(inputFrame,
                 text="Clicke Um zu\n bearbeiten:").grid(sticky="W", column=1, row=0)
        self.text = tk.Text(inputFrame, width=30, height=10)
        # Loads the contents of the duty_roster text file into the field
        self.text.insert(tk.INSERT, get_duty_roster())
        self.text.grid(sticky="W", column=2, row=0)

        inputFrame.place(x=20, y=150)

    def create_btn(self):
        """
        This method creates the buttons of the page.
        """
        btnFrame = tk.Frame(self, borderwidth=20)
        tk.Button(btnFrame,
                  text='Save', command=self.save).grid(column=1, row=0)
        btnFrame.pack(side="bottom")

    def save(self):
        """
        This method saves the plan.
        """
        content = self.text.get("1.0", 'end-1c')
        set_duty_roster(content)
