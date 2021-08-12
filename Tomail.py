from tkinter import *
from tkinter import font 
import smtplib, requests

App = Tk()
class Application():
    def __init__(self):
        self.App = App
        self.confWindow()
        self.createFrame()
        self.confFrame()
        self.confWidgets()
        App.mainloop()

    def confWindow(self):
        self.App.title("To Mail XML - 2S")
        self.App.geometry("450x150")
        self.App.configure(background="#ffffff")
    
    def createFrame(self):
        self.TextLocalFile = Frame(self.App, background="#f0eee9")
        self.LocalFile = Frame(self.App, background="#f0eee9")
        self.Separator = Frame(self.App, background="#000")
        self.PanelAction = Frame(self.App, background="#f0eee9")
        self.TextFile = Frame(self.App, background="#f0eee9")
        self.FileSend = Frame(self.App, background="#f0eee9")
        self.InitSend = Frame(self.App, background="#f0eee9")
        
    def confFrame(self):
        self.TextLocalFile.place(relx=0.01, rely=0.01, relwidth=0.20, relheight=0.19)
        self.LocalFile.place(relx=0.22, rely=0.01, relwidth=0.77, relheight=0.19)
        self.Separator.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.01)
        self.PanelAction.place(relx=0.30, rely=0.30, relwidth=0.40, relheight=0.20)
        self.TextFile.place(relx=0.01, rely=0.57, relwidth=0.10, relheight=0.13)
        self.FileSend.place(relx=0.12, rely=0.57, relwidth=0.87, relheight=0.13)
        self.InitSend.place(relx=0.74, rely=0.73, relwidth=0.25, relheight=0.20)
    
    def confWidgets(self):
        self.Tlf = Label(self.TextLocalFile, text="Local File:", foreground="black", relief=SOLID, borderwidth=1)
        self.Tlf.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.Inputt = Entry(self.LocalFile, foreground="black", background="#f0eee9" ,font="Arial 12", relief=SOLID)
        self.Inputt.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.PanelText = Label(self.PanelAction, text="Wait Process", foreground="black", relief=SOLID, borderwidth=1)
        self.PanelText.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.TextFileSend = Label(self.TextFile, text="File", foreground="black", relief=SOLID, borderwidth=1)
        self.TextFileSend.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.AreaFileSend = Label(self.FileSend, foreground="black", relief=SOLID, borderwidth=1)
        self.AreaFileSend.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.ButtonInit = Button(self.InitSend, text="Init", foreground="black", relief=SOLID, borderwidth=1)
        self.ButtonInit.place(relx=0, rely=0, relwidth=1, relheight=1)

Application()