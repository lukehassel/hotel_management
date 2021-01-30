import tkinter as tk

from ui.pages.create_customer_page import CreateCustomerPage
from ui.pages.start_page import StartPage

if __name__ == "__main__":
    root = tk.Tk()
    root.title("HI")
    main = StartPage(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()


