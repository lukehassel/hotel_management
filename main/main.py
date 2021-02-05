import tkinter as tk

from ui.pages.create_customer_page import CreateCustomerPage
from ui.pages.customer_administration_page import CustomerAdministrationPage
from ui.pages.room_administration_page import RoomAdministrationPage

if __name__ == "__main__":
    root = tk.Tk()
    root.title("HI")
    main = CustomerAdministrationPage(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()


