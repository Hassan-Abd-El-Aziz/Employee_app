from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import os,sys,shutil
from tkcalendar import Calendar, DateEntry
from threading import Thread

class TreeviewApp:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1200x900+350+40')
        self.table_data=ttk.Treeview(self.root,columns=("Age", "Submission_date","City",
                                                       "Section","Salary","Name",
                                                        "ID","Email","Image"))
        self.table_data["show"]="headings"
        self.table_data.heading("Image",text="الصورة")
        self.table_data.heading("Age",text="السن")
        self.table_data.heading("Submission_date",text="تاريخ التعيين")
        self.table_data.heading("City",text="العنوان")
        self.table_data.heading("Section",text="القسم")
        self.table_data.heading("Salary",text="الراتب")
        self.table_data.heading("Name",text="الإسم")
        self.table_data.heading("ID",text="الرقم الوظيفي")
        self.table_data.heading("Email",text="البريدالإلكتروني")

    def show_treeview(self):
        self.scroll_x=Scrollbar(self.root,orient=HORIZONTAL,command=self.table_data.xview)
        self.scroll_y=Scrollbar(self.root,orient=VERTICAL,command=self.table_data.yview)

        self.table_data.place(x=19,y=708,width=1164,height=170)

        self.table_data.configure(xscrollcommand=self.scroll_x)
        self.scroll_x.pack(side=BOTTOM,fill=X)

        self.table_data.configure(yscrollcommand=self.scroll_y)
        self.scroll_y.pack(side=LEFT,fill=X)