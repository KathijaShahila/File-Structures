from tkinter import *
import os

def cus_verify():
    phone=phone_cus.get()
    user = name_cus.get()
    id = id_cus.get()
    address = address_cus.get()
    
    phone_cus_entry.delete(0, END)
    name_cus_entry.delete(0, END)
    #id_cus_entry.delete(0, END)
    address_cus_entry.delete(0, END)
    

    for line in open("customer.txt", "r").readlines():
        login_info = line.split()
        if id  == login_info:
            user_exist()
            return TRUE
    insert_cus(phone,user,id,address)

rec=len(open("customer.txt", "r").readlines())+1
def autoincrement():
    global rec
    rec+=1
    id_cus_entry.configure(text=rec)

    
def user_exist():
    global user_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Medical Store Management System')
    password_not_recog_screen.geometry('350x350')
    Label(password_not_recog_screen, text="MEDICAL STORE MANAGEMENT SYSTEM",bg='#d90166', fg='white', font='Times',width="512", height="2").pack()
    Label(text='', bg='#000000').pack()
    Label(password_not_recog_screen, text='ID Already Exist!', font='arial',fg='red').pack()
    Label(text='', bg='#000000').pack()
    Button(password_not_recog_screen, text='Try Again',fg='white',font='garamond', command=main_page,borderwidth='5px').pack()

def insert_cus(phonee,userr,idd,address):
    global userr_exist_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title('Medical Store Management System')
    password_not_recog_screen.geometry('350x120')
    password_not_recog_screen.configure( bg='#000000')
    Label(password_not_recog_screen, text="MEDICAL STORE MANAGEMENT SYSTEM", fg='white', font='Times',width="512", bg='#d90166', height="2").pack()
    Label(password_not_recog_screen,bg='black').pack()
    Label(password_not_recog_screen, text='Customer Added Succesfully', font='Garamond', bg='#000000',fg='white').pack()
    file=open('customer.txt','a')
    file.write(phonee)
    file.write(" ")
    file.write(userr)
    file.write(" ")
    file.write(idd)
    file.write(" ")
    file.write(address)
    file.write(" ")
    
    file.write("\n")
    autoincrement()
    #Button(password_not_recog_screen, text='OK', width=5, font='Times', fg='white', bg='#d90166',borderwidth=5,command=main_page).pack()


def main_page():
    global main_screen
    global name_cus
    global name_cus_entry
    global id_cus
    global id_cus_entry
    global address_cus
    global address_cus_entry
    global phone_cus
    global phone_cus_entry
    main_screen = Tk()
    main_screen.configure( bg='#000000')
    main_screen.geometry("350x350")
    main_screen.title('Add Customer')
    Label(text="MEDICAL STORE MANAGEMENT SYSTEM",  bg='#d90166', fg='white', font='Times', width="512", height="2").pack()
    Label(main_screen,text="Enter Customer Details:",font='Times',fg='white', bg='#000000').pack()
    phone_cus=StringVar()
    name_cus = StringVar()
    id_cus = StringVar()
    address_cus = StringVar()
    

    Label(main_screen, text='Phone No:', font='garamond', fg='white', bg='#000000').pack()
    phone_cus_entry = Entry(main_screen, textvariable=phone_cus)
    phone_cus_entry.pack()

    Label(main_screen, text='Name:', font='garamond', fg='white',bg='#000000').pack()
    name_cus_entry = Entry(main_screen, textvariable=name_cus)
    name_cus_entry.pack()

    Label(main_screen, text='Customer ID:', font='garamond', fg='white', bg='#000000').pack()
    id_cus_entry = Label(main_screen,text=rec,font='garamond', fg='white', bg='#000000')
    id_cus_entry.pack()

    Label(main_screen, text='Address:', font='garamond', fg='white', bg='#000000').pack()
    address_cus_entry = Entry(main_screen, textvariable=address_cus)
    address_cus_entry.pack()

    

    Label(main_screen,text='', bg='#000000').pack()

    Button(main_screen, text='Add Customer', width=20, font='Times', fg='white', bg='#d90166',borderwidth=5,command=cus_verify).pack()
    main_screen.mainloop()

main_page()