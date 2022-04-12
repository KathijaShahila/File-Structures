from tkinter import *
import os

def login_verify_cus():
    password1 = cus_name.get()


    for line in open("customer.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_cus(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global deleted_success
    deleted_success = Toplevel(main_screen)
    deleted_success.title('Confirmation')
    deleted_success.configure(bg='#000000')
    deleted_success.geometry('350x150')
    Label(deleted_success,text="MEDICAL STORE MANAGEMENT SYSTEM",bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(deleted_success, text='Customer does not Exist',font='garamond',bg='#000000',fg='white').pack()
    Label(deleted_success,bg='#000000').pack()
    Button(deleted_success, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#d90166',borderwidth=5,command=main_pagee).pack()
    
def main_pagee():
    deleted_success.destroy()

def login_success_cus(pas):
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Medical Store Management System')
    password_not_recog_screen.geometry('350x150')
    password_not_recog_screen.configure(bg='#000000')
    Label(password_not_recog_screen, text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen,bg='#000000').pack()
    Label(password_not_recog_screen, text='Customer deleted Succesfully!',font='Garamond',fg='white',bg='#000000').pack()
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


def main_page():
    global main_screen
    global cus_name
    global name_emp_entry
    main_screen = Tk()
    main_screen.configure( bg='#000000')
    main_screen.geometry("350x250")
    main_screen.title('Delete Customer')
    Label(text="MEDICAL STORE MANAGEMENT SYSTEM",  bg='#d90166', fg='white', font='Times', width="512", height="2").pack()
    Label(text='', bg='#000000').pack()
    Label(main_screen,text="Enter the Mobile Number:",font='Times',fg='white', bg='#000000').pack()
    Label(text='', bg='#000000').pack()
    cus_name=StringVar()
    cus_name_entry = Entry(main_screen, textvariable=cus_name)
    cus_name_entry.pack()
    Label(text='', bg='#000000').pack()
    Button(text='Delete',width=20, height=1, font='Times', fg='white', bg='#d90166',borderwidth=3,command=login_verify_cus).pack()
    Label(text='', bg='#000000').pack()

    main_screen.mainloop()


main_page()