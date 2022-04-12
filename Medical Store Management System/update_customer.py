from tkinter import *
import os

def cus_verify():
    user = name_cus.get()
    id = pas
    address = address_cus.get()
    ph = ph_cus.get()

    name_cus_entry.delete(0, END)
    address_cus_entry.delete(0, END)
    ph_cus_entry.delete(0, END)

    for line in open("customer.txt", "r").readlines():
        login_info = line.split()
        if id == login_info:
            cus_exist()
            return TRUE
    insert_cus(user,id,address,ph)

def insert_cus(userr,idd,addresss,phh):
    global user_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Customer Updated')
    password_not_recog_screen.geometry('320x120')
    password_not_recog_screen.configure( bg='#000000')
    Label(password_not_recog_screen,text="MEDICAL STORE MANAGEMENT SYSTEM", fg='white', font='Times',width="512", bg='#d90166', height="2").pack()
    Label(password_not_recog_screen,bg="black").pack()
    Label(password_not_recog_screen, text='Customer Updated Succesfully', font='Garamond', bg='#000000',fg='white').pack()
    file=open('customer.txt','a')
    file.write(idd)
    file.write(" ")
    file.write(userr)
    file.write(" ")
    file.write(addresss)
    file.write(" ")
    file.write(phh)
    file.write(" ")
    file.write("\n")

def cus_exist():
    global cus_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Update Customer')
    password_not_recog_screen.geometry('350x150')
    Label(password_not_recog_screen, text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#000000', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, text='ID Already Exists',font='Times',bg='#000000', fg='white').pack()
    Label(password_not_recog_screen,bg='#000000').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#d90166',borderwidth=5).pack()
    #, command=main_page

def delete_existing(pas):
    temp = list()
    fhand = open("customer.txt", "r")
    data = fhand.read()
    fhand.close()
    records = data.split('\n')
    for record in records:
        if record.startswith(pas):
            continue
        else:
            temp.append(record)
    del temp[-1]

    fhand = open("customer.txt", "w")
    for record in temp:
        fhand.write(record)
        fhand.write('\n')

def login_verify_cus():
    password1 = cus_id.get()


    for line in open("customer.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_cus(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Invalid')
    password_not_recog_screen.configure(bg='#000000')
    password_not_recog_screen.geometry('320x170')
    Label(password_not_recog_screen,text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen,bg='#000000').pack()
    Label(password_not_recog_screen, text='Customer does not Exist',font='Times',bg='#000000', fg='white').pack()
    Label(password_not_recog_screen,bg='#000000').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#d90166',borderwidth=5,command=main_pagee).pack()
     
def main_pagee():
    password_not_recog_screen.destroy()


def login_success_cus(upas):
    global login_success_screen
    global name_emp_entry
    global name_cus_entry
    global id_cus
    global id_cus_entry
    global address_cus
    global address_cus_entry
    global ph_cus
    global ph_cus_entry
    global pas
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('Update Medicines')
    login_success_screen.geometry('320x290')  
    login_success_screen.configure(bg="black")
    Label(login_success_screen,text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(bg="black").pack()
    Label(login_success_screen, text='Update Customer With:',font='Times',fg='white', bg='#000000').pack()
    Label(bg="black").pack()
    for line in open("customer.txt", "r").readlines():
        login_info = line.split()
        if upas == login_info[0]:
            pas = upas
            delete_existing(pas)
            Label(login_success_screen, text='Phone Number',font='Times',fg='white', bg='#000000').pack()
            Label(bg="black").pack()
            Label(bg="black").pack()
            Label(login_success_screen, text=login_info[0],font='Times',fg='white', bg='#000000').pack()
            Label(login_success_screen, text='Name:',font='Times',fg='white', bg='#000000').pack()
            Label(bg="black").pack()
            Label(bg="black").pack()
            address_cus_entry = Entry(login_success_screen, textvariable=name_cus)
            address_cus_entry.pack()
            Label(login_success_screen, text='Address',font='Times',fg='white', bg='#000000').pack()
            Label(bg="black").pack()
            Label(bg="black").pack()
            ph_cus_entry = Entry(login_success_screen,textvariable=address_cus)
            ph_cus_entry.pack()
        else:
            continue
        Label(login_success_screen, bg='#000000').pack()
    Button(login_success_screen, text='Update Customer', width=20, font='Times', fg='white', bg='#d90166',borderwidth=5,command=cus_verify).pack()

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global cus_id
    global name_emp_entry
    global name_cus
    global name_cus_entry
    global id_cus
    global id_cus_entry
    global address_cus
    global address_cus_entry
    global ph_cus
    global ph_cus_entry
    main_screen = Tk()
    main_screen.geometry("320x210")
    main_screen.configure(bg="#000000")
    main_screen.title('Update Customer')
    Label(text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times',width="512", height="2").pack() 
    Label(bg='#000000').pack()   
    Label(main_screen,text="Enter the Mobile Number:", font='Times',fg='white', bg='#000000').pack()
    Label(bg='#000000').pack()
    cus_id=StringVar()
    name_cus_entry = Entry(main_screen, textvariable=cus_id)
    name_cus_entry.pack()
    Label(bg='#000000').pack()
    Button(text='Update',width=20, font='Times', fg='white', bg='#d90166',borderwidth=5,command=login_verify_cus).pack()
    name_cus = StringVar()
    id_cus = StringVar()
    address_cus = StringVar()
    ph_cus= StringVar()

    main_screen.mainloop()


main_page()