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
# ====================================================== #
        self.add_frame_info()

# ====================================================== #
        self.add_email()

        self.add_section()
        self.add_id()
        self.add_city()
        self.add_name()
        self.add_date()

        self.add_Image_employee()

        self.add_salary()
        self.add_age()
# ====================================================== #
# ====================================================== #
        self.add_frame_buttons()
        self.func_insert()
        self.func_update()
        self.func_delete()
        self.func_show()
        self.func_empty()
# ====================================================== #
# ====================================================== #



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
                                 relief=RAISED,border=1,background="#EDFFF0",justify=RIGHT)
        self.entry_section.place(x=120,y=292)
    

    def add_id(self):
        '''add employee id'''
        self.label_id=Label(self.master,font=('Bold Oblique',18),
                            background="#AEDEFC",text="الرقم الوظيفي")
        self.label_id.place(x=850,y=360)
        self.employee_id=Entry(
            self.master,width=22,background="#EDFFF0",
            font=('Bold Oblique',18)
            ,relief=RAISED,border=1,justify=CENTER)
        self.employee_id.place(x=520, y=360)
    
    def add_city(self):
        '''add adress'''
        self.label_city=Label(self.master,font=('Bold Oblique',18),
                              bg="#AEDEFC",text="المدينة")
        self.label_city.place(x=410,y=360)

        self.entry_city=Entry(self.master,width=20,
                              font=('Bold Oblique',18),
                                 relief=RAISED,border=1,
                                 background="#EDFFF0",justify=RIGHT)
        self.entry_city.place(x=120,y=360)
    
    def add_name(self):
        '''add name'''
        self.label_name=Label(self.master,
                              text="إسم الموظف",font=('Bold Oblique',18),
                              bg="#AEDEFC",)
        self.label_name.place(x=853,y=433)
        self.entry_name=Entry(self.master,width=22,
                              font=('Bold Oblique',18),
                                 relief=RAISED,border=1,
                                 background="#EDFFF0",justify=RIGHT)
        self.entry_name.place(x=520,y=433)

# إضافة التاريخ
    def add_date(self):
        '''add date'''
        self.label_date=Label(self.master,
                              font=('Bold Oblique',18), 
                              bg="#AEDEFC",
                              text="تاريخ التعيين")
        self.label_date.place(x=390,y=433)

        self.entry_date=DateEntry(self.master,
                                  selectmode="day",
                                  year=datetime.now().year,
                                  month=datetime.now().month,
                                  day=datetime.now().day,
                                  font=('Bold Oblique',18),
                                  justify='center',
                                  date_pattern="yyyy-mm-dd",
                                  foreground="black",
                                  headersforground="black",
                                  selectbackground="black",
                                  width=18,
                                  )
        self.entry_date.place(x=110,y=433)
# إضافة الصورة والزرار 
    def add_Image_employee(self):
        '''add image for employee'''
        self.image=Image.open("images\\image_empoyee.jpg")
        self.image=self.image.resize((170,160))

        self.insert_image_employee=ImageTk.PhotoImage(self.image)
        self.label_insert_image=Label(self.master,
                                      image=self.insert_image_employee).place(x=995,y=300)
     
     
        self.image_open=Image.open("images\\open_file.png")
        self.image_open=self.image_open.resize((30,30))

        self.insert_image_open=ImageTk.PhotoImage(self.image_open)
        self.button_choice=Button(self.master,text="إختيار صورة",relief=GROOVE
                                  ,width=130,height=30,border=2,
                                  background="#EDFFF0"
                                  ,font=('Bold Oblique',18), compound='left',
                                  padx=20,image=self.insert_image_open)
        self.button_choice.place(x=995,y=470)
        
# اضافة الراتب
    def add_salary(self):
        self.label_salary=Label(self.master,text="الراتب",
                                font=('Bold Oblique',18),
                                background="#AEDEFC").place(x=890,y=510)
        self.entry_salary=Entry(self.master,width=22,
                            font=('Bold Oblique',18),
                            relief=RAISED,border=1,
                            background="#EDFFF0",justify=CENTER)
        self.entry_salary.place(x=520,y=510)
    
# إضافة العمر
    def add_age(self):
        self.label_age=Label(self.master,text="السن",font=('Bold Oblique',18),
                             background="#AEDEFC",).place(x=420,y=510)
        self.entry_age=Entry(self.master,width=16,
                            font=('Bold Oblique',18),
                            relief=RAISED,border=1,
                            background="#EDFFF0",justify=CENTER).place(x=150,y=510)
# اضافة قسم الزراير 
    def add_frame_buttons(self):
        self.frame_buttons=Frame(self.master,width=1165,height=106,background="#AEDEFC",
                                 padx=10,pady=3
                                 ,relief=RIDGE,border=2).place(x=18,y=600)
        # زرار اضافة البيانات
    def func_insert(self):
        self.image_insert=Image.open("images\\insert_data.png")
        self.image_insert= self.image_insert.resize((30,30))

        self.show_image_insert=ImageTk.PhotoImage(self.image_insert)
        self.button_insert=Button(self.master,
                                  text="إضافة الموظف",width=145,height=40,
                                  relief=FLAT,border=2,
                                  image=self.show_image_insert,
                                  font=('Bold Oblique',18),padx=20,compound="left")
        self.button_insert.place(x=976,y=630)

                                  
        # زرار تحديث البيانات
    def func_update(self):
        self.image_update=Image.open("images\\update_data.png")
        self.image_update= self.image_update.resize((30,30))

        self.show_image_update=ImageTk.PhotoImage(self.image_update)
        self.button_update=Button(self.master,
                                  text="تحديث البيانات",width=145,height=40,
                                  relief=FLAT,border=2,
                                  image=self.show_image_update,
                                  font=('Bold Oblique',18),padx=20,compound="left")
        self.button_update.place(x=740,y=630)


          # زرار حذف البيانات
    def func_delete(self):
        self.image_delete=Image.open("images\\delete_data.png")
        self.image_delete= self.image_delete.resize((30,30))

        self.show_image_delete=ImageTk.PhotoImage(self.image_delete)
        self.button_delete=Button(self.master,
                                  text="حذف البيانات",width=145,height=40,
                                  relief=FLAT,border=2,
                                  image=self.show_image_delete,
                                  font=('Bold Oblique',18),padx=20,compound="left")
        self.button_delete.place(x=500,y=630)
    

         # زرار افراغ الحقول   
    def func_empty(self):
        self.image_empty=Image.open("images\\empty_data.png")
        self.image_empty= self.image_empty.resize((30,30))

        self.show_image_empty=ImageTk.PhotoImage(self.image_empty)
        self.button_empty=Button(self.master,
                                  text="إفراغ الحقول",width=145,height=40,
                                  relief=FLAT,border=2,
                                  image=self.show_image_empty,
                                 font=('Bold Oblique',18),padx=20,compound="left")
        self.button_empty.place(x=260,y=630)



         # زرار عرض البيانات  
    def func_show(self):
        self.image_show=Image.open("images\\show_data.png")
        self.image_show= self.image_show.resize((30,30))

        self.show_image_show=ImageTk.PhotoImage(self.image_show)
        self.button_show=Button(self.master,
                                  text="عرض البيانات",width=145,height=40,
                                  relief=FLAT,border=2,
                                  image=self.show_image_show,
                                  font=('Bold Oblique',18),padx=20,compound="left")
        self.button_show.place(x=35,y=630)