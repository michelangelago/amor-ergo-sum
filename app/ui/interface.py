import tkinter as tk

class Interface():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ergo-Sum")
        self.root.geometry("200x200")
        self.root.mainloop()

    def exit(self):
        print