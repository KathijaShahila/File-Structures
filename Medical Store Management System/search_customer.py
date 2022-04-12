from tkinter import *
import os

def login_verify_cus():
    password1 = phone_cus.get()


    for line in open("customer.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_cus(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Confirmation')
    password_not_recog_screen.configure(bg='#000000')
    password_not_recog_screen.geometry('350x200')
    Label(password_not_recog_screen,text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen,bg='#000000').pack()
    Label(password_not_recog_screen, text='Customer does not Exist',font='Times',bg='#000000', fg='white').pack()
    Label(password_not_recog_screen,bg='#000000').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#d90166',borderwidth=5, command=main_pagee).pack()
    
def main_pagee():
    password_not_recog_screen.destroy()

def login_success_cus(pas):
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.configure(bg="#000000")
    login_success_screen.geometry('450x250')
    frame = Frame(login_success_screen)
    grid=Frame(frame)
    Label(login_success_screen, text='                         ',bg='#000000').grid(row=0)
    Label(login_success_screen, text="Customer Detail",font='Times',bg='black',fg='white',width=18).grid(row=1, column=1, columnspan=7)
    Label(login_success_screen, text='  ',bg='#000000').grid(row=2)
    Label(login_success_screen, text='    Name   ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=1)
    Label(login_success_screen, text='                 ',bg='#000000').grid(row=3)
    Label(login_success_screen, text='     Address      ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=3)
    Label(login_success_screen, text='                   ',bg='#000000').grid(row=3)
    Label(login_success_screen, text='    Phone Number    ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=5)
    Label(login_success_screen,text="              ",bg="black").grid(row=5)
    
    i=4
    for line in open("customer.txt","r").readlines():
        cus = line.split()
        if pas == cus[0]:
            Label(login_success_screen, text=cus[1],font='Garamond',fg='white',bg='#000000').grid(row=i, column=1)
            Label(login_success_screen, text=cus[2],font='Garamond',fg='white',bg='#000000').grid(row=i, column=3)
            Label(login_success_screen, text=cus[0],font='Garamond',fg='white',bg='#000000').grid(row=i, column=5)
        else:
            continue
    Button(login_success_screen, text='OK', width=4, height=1,font='Garamond',borderwidth=3,bg='#d90166',fg="white", command=delete_login_success).grid(row=i+2,column=1,columnspan=7)

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global phone_cus
    global name_emp_entry
    main_screen = Tk()
    main_screen.configure(bg="#000000")
    main_screen.geometry("320x230")
    main_screen.title('Search Customer')
    Label(text="MEDICAL STORE MANAGEMENT SYSTEM",bg="#d90166",fg="white", font='Times',width="512", height="2").pack()
    Label(bg='#000000').pack()
    Label(main_screen,text="Enter Mobile Number:",font='Times',bg="#000000",fg="white").pack()
    Label(bg='#000000').pack()
    phone_cus=StringVar()
    phone_cus_entry = Entry(main_screen, textvariable=phone_cus)
    phone_cus_entry.pack()
    Label(bg='#000000').pack()
    Button(text='Search', width='15',font='garamond',borderwidth=5,bg="#d90166",fg="white",command=login_verify_cus).pack()
    Label(bg='#000000').pack()

    main_screen.mainloop()


main_page()
