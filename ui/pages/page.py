__author__ = "6668734, Just, 7340644, Hassel"
__email__ = "s6668734@stud.uni-frankfurt.de, s7340644@rz.uni-frankfurt.de"

import tkinter as tk


class Page(tk.Frame):

    """
    Represents a Page of the ui.
    """

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        """
        Lifts the page to the top of the pages stack.
        """
        self.lift()
