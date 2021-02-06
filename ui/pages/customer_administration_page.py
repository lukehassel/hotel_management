__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

import tkinter as tk

from domain.usecase.reception_usecase import ReceptionUseCase
from ui.pages.page import Page


class CustomerAdministrationPage(Page):

    """
    This class creates the Page where the reception can view a customer overview.
    """

    def __init__(self, *args, **kwargs):
        """
                This method creates the page.
        """
        Page.__init__(self, *args, **kwargs)

        self.create_list()

        title = tk.Label(self,
                         text="Kunden\nVerwaltung")
        title.config(font=("Courier", 44))
        title.place(x=20, y=35)

    def refresh(self):
        """
        This method will refresh the page.
        """
        self.list_widget.delete(0,'end')
        self.create_list()

    def create_list(self):
        """
        This method will create the ListBox of the page.
        """
        self.list_widget = tk.Listbox(self)

        for i, customer in enumerate(ReceptionUseCase().reservations):
            self.list_widget.insert(i, "Id: "+
                                    str(
                                        customer.getCustomerId()) + "    Name: " + customer.getName() + "    Noch nicht bezahlt.")

        self.list_widget.place(x=20, y=200, width=400)
