
from tkinter import *
import os

def med_verify():
    mname = pas
    mcompany = mcompany_med.get()
    rack = rack_med.get()
    expiry = expiry_med.get()
    price=price_med.get()

    mname_med_entry.delete(0, END)
    mcompany_med_entry.delete(0,END)
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
    password_not_recog_screen.title('Update Medicine')
    password_not_recog_screen.geometry('350x150')
    Label(password_not_recog_screen, text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#000000', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, text='ID Already Exists',font='Times',bg='#000000', fg='white').pack()
    Label(password_not_recog_screen,bg='#000000').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#d90166',borderwidth=5).pack()
    #, command=main_page

def insert_med(mnamee,mcompanyy,rackk,expiryy,pricee):
    global med_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Medicine Updated')
    password_not_recog_screen.geometry('350x100')
    password_not_recog_screen.configure( bg='#000000')
    Label(password_not_recog_screen, text="MEDICAL STORE MANAGEMENT SYSTEM", fg='white', font='Times',width="512", bg='#d90166', height="2").pack()
    Label(text='').pack()
    Label(password_not_recog_screen, text='Medicine Updated Succesfully', font='Garamond', bg='#000000',fg='white').pack()
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

def delete_existing(pas):
    temp = list()
    fhand = open("medicine.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(pas):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("medicine.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')



def login_verify_med():
    password1 = med_id.get()

    for line in open("medicine.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_med(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Invalid')
    password_not_recog_screen.configure(bg='#000000')
    password_not_recog_screen.geometry('350x150')
    Label(password_not_recog_screen,text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, text='Medicine does not Exist',font='Times',bg='#000000', fg='white').pack()
    Label(password_not_recog_screen,bg='#000000').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#d90166',borderwidth=5,command=main_pagee).pack()
    
def main_pagee():
    password_not_recog_screen.destroy()    

def login_success_med(upas):
    global login_success_screen
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
    global pas
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('Update Medicines')
    login_success_screen.geometry('350x370')  
    login_success_screen.configure(bg="black")
    Label(login_success_screen,text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(bg="black").pack()
    Label(login_success_screen, text='Medicine Details Are:',font='Times',fg='white', bg='#000000').pack()
    Label(bg="black").pack()
    for line in open("medicine.txt","r").readlines():
        login_info = line.split()
        if upas == login_info[0]:
            pas = upas
            delete_existing(pas)
            Label(bg="black").pack()
            Label(login_success_screen, text='Medicine Name:',font='Times',fg='white', bg='#000000').pack()
            Label(bg="black").pack()
            Label(bg="black").pack()
            Label(login_success_screen, text=login_info[0],font='Times',fg='white', bg='#000000').pack()
            Label(login_success_screen, text='Medicine Company:',font='Times',fg='white', bg='#000000').pack()
            Label(bg="black").pack()
            Label(text='').pack()
            mcompany_med_entry = Entry(login_success_screen, textvariable=mcompany_med)
            mcompany_med_entry.pack()
            Label(text='').pack()
            Label(text='').pack()
            Label(login_success_screen, text='Rack:',font='Times',fg='white', bg='#000000').pack()
            Label(text='').pack()
            Label(text='').pack()
            rack_med_entry = Entry(login_success_screen, textvariable=rack_med)
            rack_med_entry.pack()
            Label(login_success_screen, text='Expiry:',font='Times',fg='white', bg='#000000').pack()
            Label(text='').pack()
            Label(text='').pack()
            expiry_med_entry = Entry(login_success_screen, textvariable=expiry_med)
            expiry_med_entry.pack()
            Label(login_success_screen, text='Price:',font='Times',fg='white', bg='#000000').pack()
            Label(text='').pack()
            Label(text='').pack()
            price_med_entry = Entry(login_success_screen, textvariable=price_med)
            price_med_entry.pack()
        else:
            continue
        Label(login_success_screen,bg='black').pack()
    Button(login_success_screen, text='Update Medicine', width=20, font='Times', fg='white', bg='#d90166',borderwidth=5,command=med_verify).pack()

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global med_id
    global mname_med_entry
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
    main_screen.geometry("320x210")
    main_screen.configure(bg="#000000")
    main_screen.title('Update Medicine')
    Label(text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times',width="512", height="2").pack()    
    Label(bg='#000000').pack()
    Label(main_screen,text="Enter the Medicine Name:", font='Times',fg='white', bg='#000000').pack()
    Label(bg='#000000').pack()
    med_id=StringVar()
    mname_med_entry= Entry(main_screen, textvariable=med_id)
    mname_med_entry.pack()
    Label(bg='#000000').pack()
    Button(text='Update',width=20, font='Times', fg='white', bg='#d90166',borderwidth=5,command=login_verify_med).pack()
    mname_med = StringVar()
    mcompany_med = StringVar()
    rack_med = StringVar()
    expiry_med = StringVar()
    price_med=StringVar()
    main_screen.mainloop()


main_page()