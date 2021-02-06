__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

import tkinter as tk

from domain.usecase.reception_usecase import ReceptionUseCase
from ui.pages.page import Page


class RoomAdministrationPage(Page):

    """
    This class creates the Page where the reception can create the new customers.
    """

    def __init__(self, *args, **kwargs):
        """
        This method creates the page.
        """
        Page.__init__(self, *args, **kwargs)

        self.create_list()

        title = tk.Label(self,
                         text="Zimmer\nVerwaltung")
        title.config(font=("Courier", 44))
        title.place(x=20, y=35)

    def refresh(self):
        """
        This method will refresh the page.
        """
        self.create_list()

    def create_list(self):
        """
        This method will create the ListBox of the page.
        """
        list_widget = tk.Listbox(self)

        list_widget.delete(0, 'end')

        for i, customer in enumerate(ReceptionUseCase().reservations):

            if not customer.getRoom().getKey():
                key = "Schlüssel im Hotel"
            else:
                key = "Schlüssel beim besitzer"

            list_widget.insert(i,"Id: "+ str(customer.getCustomerId()) + "   " + key + "   " + "Raum " + str(
                customer.getRoom().getRoomNumber()))

        list_widget.place(x=20, y=200, width=430)
