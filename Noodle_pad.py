"""
Name of application: Noodle pad
Developed by: Corne Calitz
Start date: 29/08/2022
End date: TBD
Version 1.1
"""

from tkinter import *
import sys

def donothing():
    print("Nothing")

def close_program():
    msg = "Have a nice day ;)"
    sys.exit(msg)


root = Tk()

menubar = Menu(root)    # Set a menubar at the top of the gui
# File cascade
filemenu = Menu(menubar, tearoff=0) # Create an item on the menu
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="New Window", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Open...", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_separator()        # Separates the line within a menu cascade
filemenu.add_command(label="Page setup", command=donothing)
filemenu.add_command(label="Print...", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=close_program)
menubar.add_cascade(label="File", menu=filemenu)    # Adds the menu item and all the commands underneath into a cascade

# Edit cascade
editmenu = Menu(menubar, tearoff=0)
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
editmenu.add_command(label="Time/Date", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

# Format cascade
formatmenu = Menu(menubar, tearoff=0)
formatmenu.add_command(label="Word wrap", command=donothing)
formatmenu.add_command(label="Font...", command=donothing)
menubar.add_cascade(label="Format", menu=formatmenu)

# View cascade
viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Zoom", command=donothing)
viewmenu.add_command(label="Status Bar", command=donothing)
menubar.add_cascade(label="View", menu=viewmenu)

# Help cascade
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="View Help", command=donothing)
helpmenu.add_command(label="Send Feedback", command=donothing)
helpmenu.add_separator()
helpmenu.add_command(label="About NoodlePad", command=donothing)
menubar.add_cascade(label="Help", menu=viewmenu)

notepad = Text(root)
notepad.grid(row=0, column=0)

root.config(menu=menubar)
root.mainloop()
