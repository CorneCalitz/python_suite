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

Problems I ran into:
    - Launching Microsoft feedback hub seems impossible
    - Scaling using zoom is different from changing the font, yet it still requires a font change to scale
    - Certain binds do not work (Example: KP_Add, KP_0, KP_Subtract and etc.)
    - Page Setup menu command removed since it seems pointless
"""

from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import sys
import webbrowser
from datetime import datetime


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
        filemenu.add_command(label="Page Setup", command=donothing)
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
        editmenu.add_command(label="Undo", command=notepad.edit_undo, state=DISABLED)
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
        self.check = BooleanVar()

        formatmenu = Menu(self.menu, tearoff=0)
        formatmenu.add_checkbutton(label="Word wrap", onvalue=1, offvalue=0, variable=self.check,
                                   command=self.word_wrap)
        formatmenu.add_command(label="Font...", command=self.font_change)
        self.menu.add_cascade(label="Format", menu=formatmenu)

    def word_wrap(self):
        if self.check.get():
            notepad.config(wrap=WORD)
        else:
            notepad.config(wrap=NONE)

    @staticmethod
    def font_change():

        font_window = Toplevel(gui)
        font_window.geometry("420x440")
        font_window.resizable(False, False)
        font_window.grab_set()  # Locks window parent window and all its widgets

        # Labels
        Label(font_window, text="Font:").grid(row=1, column=1, pady=(20, 0), padx=(20, 10), sticky="W")
        Label(font_window, text="Font Style:").grid(row=1, column=2, pady=(20, 0), padx=14, sticky="W")
        Label(font_window, text="Size:").grid(row=1, column=3, pady=(20, 0), padx=14, sticky="W")

        # Entries
        entry_font = Entry(font_window, width=28)
        entry_font.grid(row=2, column=1, pady=(0, 1), padx=(20, 0), sticky="W")
        entry_font_style = Entry(font_window)
        entry_font_style.grid(row=2, column=2, pady=(0, 1), padx=(14, 0), sticky="W")
        entry_font_size = Entry(font_window, width=8)
        entry_font_size.grid(row=2, column=3, pady=(0, 1), padx=(14, 0), sticky="W")

        # Text boxes
        txt_font = Text(font_window, width=21, height=10)
        txt_font.grid(row=3, column=1, padx=(20, 0), sticky="NW")
        txt_font_style = Text(font_window, width=15, height=10)
        txt_font_style.grid(row=3, column=2, padx=(14, 0), sticky="NW")
        txt_font_size = Text(font_window, width=6, height=10)
        txt_font_size.grid(row=3, column=3, padx=(14, 0), sticky="NW")

        # Labelframe
        frame_sample = LabelFrame(font_window, text="Sample", relief=GROOVE)
        frame_sample.grid(row=4, column=2, columnspan=2, pady=25, sticky="W")
        lbl_sample = Label(frame_sample, text="Shit", width=28, height=6)
        lbl_sample.pack()

        font_window.mainloop()


# Almost complete
class View:
    def __init__(self, menu):

        self.menu = menu
        self.zoom_size = 0
        self.status = BooleanVar()

        if not self.status.get():
            status_bar.forget()

        # View cascade
        viewmenu = Menu(self.menu, tearoff=0)
        # Zoom cascade existing within view cascade
        zoommenu = Menu(viewmenu, tearoff=0)
        zoommenu.add_command(label="Zoom in                                    Ctrl+Right", command=self.zoom_in)
        zoommenu.add_command(label="Zoom out                                    Ctrl+Left", command=self.zoom_out)
        zoommenu.add_command(label="Restore default zoom              Ctrl+Down",
                             command=self.zoom_defualt)
        viewmenu.add_cascade(label="Zoom", menu=zoommenu)
        viewmenu.add_checkbutton(label="Status Bar", onvalue=1, offvalue=0, variable=self.status,
                                 command=self.sbar_show)
        self.menu.add_cascade(label="View", menu=viewmenu)

        gui.bind('<Control-Left>', self.zoom_out_bind)
        gui.bind('<Control-Right>', self.zoom_in_bind)
        gui.bind('<Control-Down>', self.zoom_default_bind)

    @staticmethod
    def zoom(size):
        font.configure(size=size)

    def zoom_out_bind(self, event):
        if zoom_scale.get() != zoom_scale.cget("from"):  # The min value is called
            zoom_scale.set(zoom_scale.get() - 1)
            self.zoom(zoom_scale.get())

    def zoom_in_bind(self, event):
        if zoom_scale.get() != zoom_scale.cget("to"):  # The max value is called
            zoom_scale.set(zoom_scale.get() + 1)
            self.zoom(zoom_scale.get())

    def zoom_out(self):
        self.zoom_out_bind(self)

    def zoom_in(self):
        self.zoom_in_bind(self)

    def zoom_default_bind(self, event):
        zoom_scale.set(14)
        self.zoom(zoom_scale.get())

    def zoom_defualt(self):
        self.zoom_default_bind(self)

    def sbar_show(self):
        if self.status.get():
            status_bar.pack(fill=X, side=BOTTOM, before=scrolly)
        else:
            status_bar.forget()


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

    @staticmethod
    def view_help():
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    @staticmethod
    def send_feedback():
        webbrowser.open("https://aka.ms")  # Consider creating a run command to launch microsoft feedback
        # For now, it takes you to the site that feedback uses

    @staticmethod
    def about_noodlepad():
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


# --------------------- Classless methods ---------------------
def sbar_details(ev=None):
    row, col = notepad.index('insert').split('.')
    zoom_percent = int(100 / 13 * zoom_scale.get()-7)
    status_bar['text'] = f'             |  Ln {row}, Col {col}  |  Zoom {zoom_percent}%  |'


if __name__ == "__main__":
    # GUI creation
    gui = Tk()
    gui.title("NoodlePad")
    gui.geometry("700x500")
    menubar = Menu(gui)  # Set a menubar at the top of the gui

    # Create status bar
    status_bar = Label(gui)
    status_bar.pack(fill=BOTH, side=BOTTOM)

    # Create scale
    zoom_scale = Scale(gui, from_=1, to=72)
    zoom_scale.set(14)
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

    # Event creation for line and col fetch
    notepad.event_add('<<REACT>>', *('<Motion>', '<ButtonRelease>', '<KeyPress>', '<KeyRelease>'))
    x = notepad.bind('<<REACT>>', sbar_details)
    sbar_details()
    notepad.focus()

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
    # ========================== Experimental code =============================================


