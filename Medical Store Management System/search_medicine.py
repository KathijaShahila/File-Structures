from tkinter import *
import os

def login_verify_med():
    password1 = med_mname.get()

    for line in open("medicine.txt", "r").readlines():
        login_info = line.split()
        if password1 == login_info[0]:
            login_success_med(password1)
            return TRUE
    password_not_recognised()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Confirmation')
    password_not_recog_screen.configure(bg='#000000')
    password_not_recog_screen.geometry('320x150')
    Label(password_not_recog_screen,text="MEDICAL STORE MANAGEMENT SYSTEM", bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(password_not_recog_screen, text='Medicine is not Available',font='Times',bg='#000000', fg='white').pack()
    Label(password_not_recog_screen,bg='#000000').pack()
    Button(password_not_recog_screen, text='Try Again',width=10, height=1, font='Times', fg='white', bg='#d90166',borderwidth=5, command=main_pagee).pack()
   
def main_pagee():
    password_not_recog_screen.destroy()   

def login_success_med(pas):
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title('Medicines')
    login_success_screen.geometry('600x200')  
    login_success_screen.configure(bg="black")    
    frame = Frame(login_success_screen)
    grid=Frame(frame)
    Label(login_success_screen, text='                         ',bg='#000000').grid(row=0)
    Label(login_success_screen, text="Medicine Details",font='Times',bg='black',fg='white',width=18).grid(row=1, column=1, columnspan=7)
    Label(login_success_screen, text='  ',bg='#000000').grid(row=2)
    Label(login_success_screen, text='    Name   ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=1)
    Label(login_success_screen, text='                 ',bg='#000000').grid(row=3)
    Label(login_success_screen, text='   Company ID       ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=3)
    Label(login_success_screen, text='               ',bg='#000000').grid(row=3)
    Label(login_success_screen, text='     Rack No      ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=5)
    Label(login_success_screen, text='                   ',bg='#000000').grid(row=3)
    Label(login_success_screen, text='      Expiry    ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=7)
    Label(login_success_screen,text="              ",bg="black").grid(row=3)
    Label(login_success_screen, text='      Price    ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=9)
    Label(login_success_screen,text="              ",bg="black").grid(row=6)
    
    i=5
    for line in open("medicine.txt","r").readlines():
        cus = line.split()
        if pas == cus[0]:
            Label(login_success_screen, text=cus[0],font='Garamond',fg='white',bg='#000000').grid(row=i, column=1)
            Label(login_success_screen, text=cus[1],font='Garamond',fg='white',bg='#000000').grid(row=i, column=3)
            Label(login_success_screen, text=cus[2],font='Garamond',fg='white',bg='#000000').grid(row=i, column=5)
            Label(login_success_screen, text=cus[3],font='Garamond',fg='white',bg='#000000').grid(row=i, column=7)
            Label(login_success_screen, text=cus[4],font='Garamond',fg='white',bg='#000000').grid(row=i, column=9)
        else:
            continue
    Button(login_success_screen, text='OK', width=5, height=1,font='Garamond',borderwidth=2,bg='#d90166',fg="white", command=delete_login_success).grid(row=i+2,column=1,columnspan=7)

def delete_login_success():
    login_success_screen.destroy()


def main_page():
    global main_screen
    global med_mname
    global med_mname_entry
    main_screen = Tk() 
    main_screen.configure(bg="#000000")
    main_screen.geometry("320x220")
    main_screen.title('Search Medicine')
    Label(text="MEDICAL STORE MANAGEMENT SYSTEM",bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(text='',bg='#000000').pack()
    Label(main_screen,text="Enter Name of Medicine:",font='Times',bg='#000000',fg="white").pack()
    Label(text='',bg='#000000').pack()
    med_mname=StringVar()
    med_mname_entry= Entry(main_screen, textvariable=med_mname)
    med_mname_entry.pack()
    Label(text='',bg='#000000').pack()
    Button(text='Search', width='15',height=1,font='garamond',borderwidth=5,bg='#d90166',fg="white",command=login_verify_med).pack()
    Label(text='',bg='#000000').pack()
    main_screen.mainloop()

main_page()