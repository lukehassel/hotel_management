import tkinter as tk

if __name__ == '__main__':
    gui = tk.Tk(className='Python Examples - Window Size')
    # set window size
    gui.geometry("500x200")
    label = tk.Label(
        text="Hotel Management",
        foreground="white",
        background="black"
    )
    label.pack()
    button = tk.Button(
        text="Click me!",
        width=25,
        height=5,
        bg="blue",
        fg="red",
    )
    button.pack()
    gui.mainloop()
