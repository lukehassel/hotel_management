__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

import tkinter as tk

from ui.pages.start_page import StartPage

"""
    This module starts the program and sets up the window of the ui.
"""

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Trash Hotel Administration System")
    main = StartPage(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x450")
    root.mainloop()


