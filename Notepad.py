from distutils import command
from json.tool import main
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#=======Functions
def NewFile():
    global file
    root.title("Untitled")
    file=None
    TextArea.delete(1.0, END)

def OpenFile():
    global file
    file=askopenfilename(defaultextension= ".txt",filetypes=[("All files","*.*"),("Text documents",".txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "_Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read()) 


def SaveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", 
        defaultextension= ".txt",filetypes=[("All files","*.*"),("Text documents",".txt")])

def exit():
    pass

def Cut():
    TextArea.event_generate(("<<Cut>>"))


def Copy():
    TextArea.event_generate(("<<Copy>>"))


def Paste():
    TextArea.event_generate(("<<Paste>>"))

def About():
    pass

if __name__== '__main__':
    root= Tk()
    root.title("My notepad")
    root.geometry("644x788")

    #Menu Bar======================================
    MenuBar = Menu(root)
    
    #=======File menu starts
    FileMenu = Menu(MenuBar, tearoff=0)

    #To open new file
    FileMenu.add_command(label="New", command=NewFile)

    #To open existing file
    FileMenu.add_command(label="Open", command=OpenFile)

    #To save the current file
    FileMenu.add_command(label="Save", command=SaveFile)

    FileMenu.add_separator()

    #Exit command
    FileMenu.add_command(label="Exit", command=exit)

    MenuBar.add_cascade(label="File", menu=FileMenu)

    #========File menu ends

    #=======Edit menu starts
    EditMenu = Menu(MenuBar, tearoff=0)
    
    #Cut, copy and paste features
    EditMenu.add_command(label="Cut", command=Cut)

    EditMenu.add_command(label="Copy", command=Copy)

    EditMenu.add_command(label="Paste", command=Paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    #=======Edit menu ends

    #=======Help menu starts
    HelpMenu = Menu(MenuBar, tearoff=0)

    HelpMenu.add_command(label="About", command=About)

    MenuBar.add_cascade(label="Help", menu= HelpMenu)
    #=======Help menu ends
    
    root.config(menu=MenuBar)

    #Menu Bar end===================================

    #Text area======================================
    TextArea = Text(root, font="lucida 13")
    file= None
    TextArea.pack(fill=BOTH, expand=True)
    #Text area ends=================================


    #Scroll bar=====================================
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    #Scroll bar ends================================

    root.mainloop()
