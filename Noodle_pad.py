"""
Name of application: Noodle pad
Developed by: Corne Calitz
Start date: 29/08/2022
End date: TBD
Version 1.2

Expectations:
    - Will learn how to create dynamic widgets
    - Learn how to work inactive and active text selection
    - File handling
    - Launching .txt using this application
    - Learn how to implement a menu bar
    - Learn how to implement binds using keyboard

Problems I ran into so far:
    - Launching Microsoft feedback hub seems impossible
    -
"""

from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import tkinter.messagebox as msgbox
import sys
import webbrowser
from datetime import datetime

import subprocess


def donothing():
    print("Nothing")


class File:
    def __init__(self, menu):
        self.menu = menu
        # File cascade
        filemenu = Menu(self.menu, tearoff=0)  # Create an item on the menu
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="New Window", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Open...", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_separator()  # Separates the line within a menu cascade
        filemenu.add_command(label="Page setup", command=donothing)
        filemenu.add_command(label="Print...", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit, background="Red")
        self.menu.add_cascade(label="File",
                              menu=filemenu)  # Adds the menu item and all the commands underneath into a cascade

    def exit(self):
        msg = "Have a nice day ;)"
        sys.exit(msg)


class Edit:
    def __init__(self, menu):
        self.menu = menu
        # Edit cascade
        editmenu = Menu(self.menu, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Search with Bing...", command=donothing)
        editmenu.add_command(label="Find...", command=donothing)
        editmenu.add_command(label="Find next", command=donothing)
        editmenu.add_command(label="Find previous", command=donothing)
        editmenu.add_command(label="Replace...", command=donothing)
        editmenu.add_command(label="Go To...", command=donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Select All", command=donothing)
        editmenu.add_command(label="Time/Date", command=self.time_date)
        self.menu.add_cascade(label="Edit", menu=editmenu)

    def time_date(self):
        time = datetime.now().time().strftime("%H:%M")
        date = datetime.now().date().strftime("%Y-%m-%d")
        notepad.insert("1.0", time + " " + date + "\n")


class Format:
    def __init__(self, menu):
        self.menu = menu
        # Format cascade
        # SET A BOOLEAN VAR THAT WILL CHANGE IF THE CHECKBUTTON CHANGES ONVALUE AND OFFVALUE PS. USE .get alongside the varaible
        self.check = BooleanVar()

        formatmenu = Menu(self.menu, tearoff=0)
        formatmenu.add_checkbutton(label="Word wrap", onvalue=1, offvalue=0, variable=self.check,
                                   command=self.word_wrap)
        formatmenu.add_command(label="Font...", command=donothing)
        self.menu.add_cascade(label="Format", menu=formatmenu)

    def word_wrap(self):
        if self.check.get():
            notepad.config(wrap=WORD)
        else:
            notepad.config(wrap=NONE)


# Completed
class View:
    def __init__(self, menu):
        self.menu = menu
        self.zoom_increment = 0  # ---------------------------> Save value
        # View cascade
        viewmenu = Menu(self.menu, tearoff=0)
        # Zoom cascade existing within view cascade
        zoommenu = Menu(viewmenu, tearoff=0)
        zoommenu.add_command(label="Zoom in", command=self.zoom_in)
        zoommenu.add_command(label="Zoom out", command=self.zoom_out)
        zoommenu.add_command(label="Restore default zoom", command=lambda: font.configure(size=14))

        viewmenu.add_cascade(label="Zoom", menu=zoommenu)
        viewmenu.add_command(label="Status Bar", command=donothing)
        self.menu.add_cascade(label="View", menu=viewmenu)

    def zoom_out(self):
        self.zoom_increment -= 1
        font.configure(size=14 + self.zoom_increment)

    def zoom_in(self):
        self.zoom_increment += 1
        font.configure(size=14 + self.zoom_increment)


# Completed
class Help:
    def __init__(self, menu):
        self.menu = menu
        # Help cascade
        helpmenu = Menu(self.menu, tearoff=0)
        helpmenu.add_command(label="View Help", command=self.view_help)
        helpmenu.add_command(label="Send Feedback", command=self.send_feedback)
        helpmenu.add_separator()
        helpmenu.add_command(label="About NoodlePad", command=self.about_noodlepad)
        self.menu.add_cascade(label="Help", menu=helpmenu)

    def view_help(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def send_feedback(self):
        webbrowser.open("https://aka.ms")  # Consider creating a run command to launch microsoft feedback
        # For now, it takes you to the site that feedback uses

    def about_noodlepad(self):
        about_page = Toplevel(gui)
        about_page.geometry("460x380")
        about_page.title("About NoodlePad")
        about_page.resizable(False, False)
        ttk.Separator(about_page, orient="horizontal").pack(fill="x", padx=20, pady=10)
        Label(about_page, text="NoodlePad", font=("Century Gothic", 20, "italic")).pack(pady=10, side=TOP)
        ttk.Separator(about_page, orient="horizontal").pack(fill="x", padx=20, pady=10)
        frame = LabelFrame(about_page, relief=GROOVE)
        frame.pack(fill="both", expand=YES, pady=10, padx=20)
        Label(frame, text="It's about drive, it's about power").pack()
        Label(frame, text="We stay hungry, we devour").pack()
        Label(frame, text="Put in the work, put in the hours and take what's ours (ahoo)").pack()
        Label(frame, text="Black and Samoan in my veins").pack()
        Label(frame, text="My culture bangin' with Strange").pack()
        Label(frame, text="I change the game, so what's my motherfuckin' name (Rock)").pack()
        Label(frame, text="(What they gonna get though?)").pack()
        Label(frame, text="Desecration, defamation, if you wanna bring it to the masses").pack()
        Label(frame, text="Face to face, now we escalatin', when I have to put boots to asses").pack()
        Label(frame, text="Mean on ya, like a dream when I'm rumblin', you're gonna scream mama").pack()
        Label(frame, text="So bring drama to the King Brahma (then what?)").pack()
        Label(frame, text="Comin' at you with extreme mana").pack()


if __name__ == "__main__":
    # GUI creation
    gui = Tk()
    gui.title("NoodlePad")
    gui.geometry("700x500")
    menubar = Menu(gui)  # Set a menubar at the top of the gui

    # Create font
    font = Font(family="Consolas", size=14)

    # Scrollbar creation
    scrolly = Scrollbar(gui)
    scrollx = Scrollbar(gui, orient=HORIZONTAL)
    scrolly.pack(side=RIGHT, fill=Y)
    scrollx.pack(side=BOTTOM, fill=X)

    # Create and set text input
    notepad = Text(gui, relief=SUNKEN, font=font, wrap=NONE, undo=True, yscrollcommand=scrolly.set,
                   xscrollcommand=scrollx.set)
    notepad.pack(expand=True, fill=BOTH)

    # Config scrollbars
    scrolly.config(command=notepad.yview)
    scrollx.config(command=notepad.xview)

    # Set items on menubar
    File(menubar)
    Edit(menubar)
    Format(menubar)
    View(menubar)
    Help(menubar)

    gui.config(menu=menubar)
    gui.mainloop()
