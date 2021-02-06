import tkinter as tk

from domain.entities.room.single_room import SingleRoom
from domain.usecase.reception_usecase import ReceptionUseCase
from ui.pages.page import Page


class RoomAdministrationPage(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        # label.pack(side="top", fill="both", expand=True)

        #self.frame = tk.Frame(self).pack()

        # ReceptionUseCase().createReservation("nasdf", 12, SingleRoom())
        # ReceptionUseCase().createReservation("nasdf", 12, SingleRoom())
        # ReceptionUseCase().createReservation("nasdf", 12, SingleRoom())

        print("HELLO")

        self.create_list()

        title = tk.Label(self,
                         text="Zimmer\nVerwaltung")
        title.config(font=("Courier", 44))
        title.place(x=20, y=35)

    def refresh(self):
        self.create_list()

    def create_list(self):
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
