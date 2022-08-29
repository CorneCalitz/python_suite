"""
Name of application: Noodle pad
Developed by: Corne Calitz
Start date: 29/08/2022
End date: TBD
Version 1.0
"""

from tkinter import *

class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Noodle Pad")
        master.geometry("600x800")

        self.notepad = Text(master)
        self.menu = Menu(master)

        self.SetLayout()
    def SetLayout(self):
        self.menu.grid(row=1, column=0)
        self.notepad.grid(row=1,column=0)

if __name__ == "__main__":
    root = Tk()
    run = Notepad(root)
    root.mainloop()
