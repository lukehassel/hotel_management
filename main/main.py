import tkinter as tk

from ui.pages.create_customer_page import CreateCustomerPage
from ui.pages.customer_administration_page import CustomerAdministrationPage
from ui.pages.room_administration_page import RoomAdministrationPage
from ui.pages.start_page import StartPage

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Trash Hotel Administration System")
    main = StartPage(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x450")
    root.mainloop()


