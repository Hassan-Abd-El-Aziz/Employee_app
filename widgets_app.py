from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import os,sys,shutil
from tkcalendar import Calendar, DateEntry
from threading import Thread

class WidgetsApp:
    def __init__(self,master):
        self.master=master
        self.master.geometry("1200x900+350+40")#ابعاد الشاشه
        self.master.resizable(width=False ,height=False)
        self.master.title("نظام إدارة شئون الموظفين")
        self.master.iconbitmap("images\\title_app.ico")

# تشغيل الدالة الخاصة بإضافة العنوان
        self.call_function_add_title_frame=Thread(target=self.add_frame_title,args=())
        self.call_function_add_title_frame.start()

# تشغيل الدالة الخاصة بإضافة مكان البحث
        self.call_function_add_search_frame=Thread(target=self.add_search_frame,args=(),)
        self.call_function_add_search_frame.start()

# الداخلة الخاصة بالعنوان
    def add_frame_title(self):
        """Add frame title and add title label"""
        self.title_frame=Frame(self.master,
                                   width=1165,height=80,background="#E8E4FA")
        self.title_frame.place(x=18,y=4)
        self.title_label=Label(self.title_frame,width=30,height=1,background="#E8E4FA",font=("Libra Baskerville, serif;" ,26)
                               ,text="إضافة موظف")
        self.title_label.place(x=300,y=20)
        # دالة تصميم البحث عن موظف 
    def add_search_frame(self):
        '''add search frame employee'''
        self.search_frame=Frame(self.master,width=1165,height=80,background="#d9ddf7",relief=SUNKEN,border=2)
        self.search_frame.place(x=18,y=88)