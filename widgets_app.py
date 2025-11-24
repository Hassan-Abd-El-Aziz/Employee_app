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

        self.master = master
        self.master.geometry("1200x900+350+40")#ابعاد الشاشه
        self.master.resizable(width=False ,height=False)
        self.master.title("نظام إدارة شئون الموظفين")
        self.master.iconbitmap("images\\title_app.ico")
# ====================================================== #
# تشغيل الدوال  الخاصة  إدخال البحث
        self.add_frame_title()
        self.add_search_frame()


        self.add_entry_search()
        self.get_search()
# ====================================================== #

        self.add_delete_frame()
        self.add_entry_delete()
        self.get_delete()
# ====================================================== #
        self.add_frame_info()
# ====================================================== #

        self.add_email()
# ====================================================== #
        self.add_section()

# الدالة الخاصة بالعنوان
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
        self.search_frame=Frame(self.master,width=1165,height=80,
                                background="#d9ddf7",relief=SUNKEN,border=2)
        self.search_frame.place(x=18,y=88)


        self.search_label=Label(self.master,
                                background="#d9ddf7",text="أدخل الرقم الوظيفي للموظف أو البريد الإلكتروني للبحث عنه",font=('Bold Oblique',18))
        self.search_label.place(x=600,y=113)
#    دالة مربع الادخال للبحث
    def add_entry_search(self):
        '''add entry search for employee'''
        self.search_employee=Entry(
            self.master,width=33,background="#E6F2FC",
            font=('Bold Oblique',18)
            ,relief=RIDGE,border=1,justify=CENTER)
        self.search_employee.place(x=200, y=113)

# دالة زرار البحث بالصورة
    def get_search(self):
        '''function for call buttom get data'''
        self.image_search=Image.open("images\\search_data.png")
        self.image_search=self.image_search.resize((35,35))
        self.show_image_search_data=ImageTk.PhotoImage(self.image_search)

        self.button_search_data=Button(
            self.master,width=90,height=30,text="بحث",font=('Bold Oblique',18),
            background="#E6F2FC",padx=20,relief=FLAT,
            border=1,bd=1,image=self.show_image_search_data,
            compound="left",)
        self.button_search_data.place(x=40,y=106)

#دالة زرار الحذف
    def add_delete_frame(self):
        '''add search frame employee'''
        self.delete_frame=Frame(self.master,width=1165,height=80,
                                background="#FFF0F0",relief=SUNKEN,border=2)
        self.delete_frame.place(x=18,y=170)

        self.delete_label=Label(self.master,
                                background="#FFF0F0",
                                text="ادخل الرقم الوظيفي لحذف الموظف",
                                font=('Bold Oblique',18))
        self.delete_label.place(x=800,y=190)

        #    دالة مربع الادخال للحذف
    def add_entry_delete(self):
        '''add entry delete for employee'''
        self.delete_employee=Entry(
            self.master,width=40,background="#E6F2FC",
            font=('Bold Oblique',18)
            ,relief=RIDGE,border=1,justify=CENTER)
        self.delete_employee.place(x=200, y=190)


    # دالة زرار الحذف بالصورة
    def get_delete(self):
        '''function for call buttom delete data'''
        self.image_delete=Image.open("images\\delete_employee.png")
        self.image_delete=self.image_delete.resize((35,35))
        self.show_image_delete_employee=ImageTk.PhotoImage(self.image_delete)

        self.button_delete_data=Button(
            self.master,width=90,height=30,text="بحث",font=('Bold Oblique',18),
            background="#E6F2FC",padx=20,relief=FLAT,
            border=2,bd=2,image=self.show_image_delete_employee,
            compound="left",)
        self.button_delete_data.place(x=40,y=190)

# الاطار الخاص بمعلومات الموظف
    def add_frame_info(self):
        self.frame_info=Frame(self.master,
                              width=1165,height=350,bg="#AEDEFC",
                              padx=10,pady=3,relief=RIDGE,border=2)
        self.frame_info.place(x=18,y=250)


    def add_email(self):
        '''add employee email'''
        self.label_email=Label(self.master,
                               text="البريد الإلكتروني ",
                               font=('Bold Oblique',18),
                               background="#AEDEFC",)
        self.label_email.place(x=820,y=291)

        self.entry_email=Entry(self.master,
                         width=22,font=('Bold Oblique',18),
                         relief=RAISED,border=1,background="#EDFFF0")
        self.entry_email.place(x=520,y=292)
    
    def add_section(self):
        self.label_section=Label(self.master,text="القسم",font=('Bold Oblique',18),
                                 background="#AEDEFC", )
        self.label_section.place(x=420,y=291)

        self.entry_section=Entry(self.master,width=20,font=('Bold Oblique',18),
                                 relief=RAISED,border=1,background="#EDFFF0")
        self.entry_section.place(x=120,y=292)