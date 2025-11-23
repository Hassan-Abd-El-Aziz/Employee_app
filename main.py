from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import os , sys , shutil
from tkcalendar import Calendar, DateEntry
from threading import Thread
from widgets_app import WidgetsApp
class MainApp:
    def __init__(self,root):
        self.root=root
        self.class_widgets=WidgetsApp(self.root)

if __name__=="__main__":
    app=Tk()
    class_main=MainApp(app)
    app.mainloop()