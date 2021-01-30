import tkinter as tk

from ui.pages.start_page import StartPage

if __name__ == "__main__":
    root = tk.Tk()
    main = StartPage(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()

