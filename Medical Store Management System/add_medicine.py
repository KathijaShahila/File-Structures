from tkinter import *
import os

def med_verify():
    mname = mname_med.get()
    mcompany= mcompany_med.get()
    rack = rack_med.get()
    expiry = expiry_med.get()
    price = price_med.get()

    mname_med_entry.delete(0, END)
    mcompany_med_entry.delete(0, END)
    rack_med_entry.delete(0, END)
    expiry_med_entry.delete(0, END)
    price_med_entry.delete(0,END)

    for line in open("medicine.txt", "r").readlines():
        login_info = line.split()
        if mcompany == login_info:
            med_exist()
            return TRUE
    insert_med(mname,mcompany,rack,expiry,price)

def med_exist():
    global med_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Medical Store Management System')
    password_not_recog_screen.geometry('350x100')
    password_not_recog_screen.configure( bg='#000000')
    Label(password_not_recog_screen, text="MEDICAL STORE MANAGEMENT SYSTEM",  bg='#000000', fg='white', font='verdana',width="512", height="2").pack()
    Label(text='', bg='#000000').pack()
    Label(password_not_recog_screen, text='ID Already Exist!', font='arial',fg='white', bg='#000000').pack()
    Label(text='', bg='#000000').pack()
    Button(password_not_recog_screen, text='Try Again',fg='white', bg='#000000',font='garamond', command=main_page,borderwidth='5px').pack()

def insert_med(mnamee,mcompanyy,rackk,expiryy,pricee):
    global book_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Medicine Added')
    password_not_recog_screen.geometry('320x150')
    password_not_recog_screen.configure( bg='#000000')
    Label(password_not_recog_screen, text="MEDICAL STORE MANAGEMENT SYSTEM",  bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, bg='#000000').pack()
    Label(password_not_recog_screen, text='Medicine Added Succesfully!', font='Garamond',fg='white', bg='#000000').pack()
    file=open('medicine.txt','a')
    file.write(mnamee)
    file.write(" ")
    file.write(mcompanyy)
    file.write(" ")
    file.write(rackk)
    file.write(" ")
    file.write(expiryy)
    file.write(" ")
    file.write(pricee)
    file.write(" ")
    file.write("\n")



def main_page():
    global main_screen
    global mname_med
    global mname_med_entry
    global mcompany_med
    global mcompany_med_entry
    global rack_med
    global rack_med_entry
    global expiry_med
    global expiry_med_entry
    global price_med
    global price_med_entry
    main_screen = Tk()
    main_screen.configure( bg='#000000')
    main_screen.geometry("320x370")
    main_screen.title('Add Medicine')
    Label(text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times', width="512", height="2").pack()
    Label(main_screen,text="Enter the Medicine Details:",font='Times',fg='white', bg='#000000',height='2').pack()
    mname_med = StringVar()
    mcompany_med = StringVar()
    rack_med = StringVar()
    expiry_med = StringVar()
    price_med=StringVar()

    Label(main_screen, text='Name:', font='garamond', fg='white', bg='#000000').pack()
    mname_med_entry = Entry(main_screen, textvariable=mname_med)
    mname_med_entry.pack()
    Label(main_screen, text='Manufacturer:', font='garamond', fg='white', bg='#000000').pack()
    mcompany_med_entry = Entry(main_screen, textvariable=mcompany_med)
    mcompany_med_entry.pack()
    Label(main_screen, text='Rack No:', font='garamond', fg='white', bg='#000000').pack()
    rack_med_entry = Entry(main_screen, textvariable=rack_med)
    rack_med_entry.pack()
    Label(main_screen, text='Expiry:', font='garamond', fg='white', bg='#000000').pack()
    expiry_med_entry = Entry(main_screen, textvariable=expiry_med)
    expiry_med_entry.pack()
    Label(main_screen, text='Price:', font='garamond', fg='white', bg='#000000').pack()
    price_med_entry = Entry(main_screen, textvariable=price_med)
    price_med_entry.pack()
    Label( bg='#000000').pack()
    Button(main_screen, text='Add Medicine', width=20, height=1, font='Times', fg='white', bg='#d90166',borderwidth=5, command=med_verify).pack()
    main_screen.mainloop()
main_page()