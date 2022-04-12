from tkinter import *
from tkinter import messagebox
import os

def add_medicine():
    os.system('python add_medicine.py')

def view_medicine():
    os.system('python view_medicine.py')

def search_medicine():
    os.system('python search_medicine.py')

def update_medicine():
    os.system('python update_medicine.py')

def delete_medicine():
    os.system('python delete_medicine.py')



def add_customer():
    os.system('python add_customer.py')

def view_customer():
    os.system('python view_customer.py')

def search_customer():
    os.system('python search_customer.py')

def update_customer():
    os.system('python update_customer.py')

def delete_customer():
    os.system('python delete_customer.py')




def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    login_screen = Toplevel(main_screen)
    login_screen.title('Admin Login')
    login_screen.geometry('275x275')
    login_screen.configure(bg="#000000")
    Label(login_screen,bg="#000000").pack()
    Label(login_screen, text='Enter Admin Credentials', fg='black',bg='#d90166', font='Times',height=2,width=512).pack()
    Label(login_screen, bg="#000000").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text='Username',font='Garamond',bg="#000000",fg="white").pack()
    Label(bg="#000000").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text='',bg="#000000").pack()
    Label(login_screen, text='Password',font='Garamond',bg="#000000",fg="white").pack()
    Label(bg="#000000").pack()
    Label(bg="#000000").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text='',bg="#000000").pack()
    Button(login_screen, text='LOGIN', width=10, height=0,font='Garamond',borderwidth=5,bg='#d90166',fg='white' ,command=login_verify).pack()




def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    for line in open("login.txt", "r").readlines():
        login_info = line.split()
        if username1 == login_info[0] and password1 == login_info[1]:
            login_success()
            return TRUE
    password_not_recognised()


def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title('Login Success')
    login_success_screen.geometry('200x200')
    login_success_screen.configure(bg="#000000")
    Label(login_success_screen,bg="#000000").pack()
    Label(login_success_screen, text='Login Success',bg="#d90166",height=1,fg='white',font="Times",width=512).pack()
    Label(login_success_screen,bg="#000000").pack()
    Label(command=admin_button()).pack()



def admin_button():
    login_success_screen.geometry('400x700')
    Button(login_success_screen, text='Add Medicine', font='Times', height=1, width=30, fg='white', bg='#000000',command=add_medicine).pack()
    Label(login_success_screen,bg="#000000").pack()
    Button(login_success_screen, text='View Medicine', font='Times', height=1, width=30, fg='white', bg='#000000',command=view_medicine).pack()
    Label(login_success_screen,bg="#000000").pack()
    Button(login_success_screen, text='Search Medicines', font='Times', height=1, width=30, fg='white', bg='#000000',command=search_medicine).pack()
    Label(login_success_screen,bg="#000000").pack()
    Button(login_success_screen, text='Delete Medicine', font='Times', height=1, width=30, fg='white',bg='#000000',command=delete_medicine).pack()
    Label(login_success_screen,bg="#000000").pack()
    Button(login_success_screen, text='Update Medicine Details', font='Times', height=1, width=30, fg='white',bg='#000000',command=update_medicine).pack()
    Label(login_success_screen,bg="#000000").pack()
    


    Label(login_success_screen,bg="#000000").pack()
    Button(login_success_screen, text='Add New Customer', font='Times', height=1, width=30, fg='white', bg='#000000',command=add_customer).pack()
    Label(login_success_screen,bg="#000000").pack()
    Button(login_success_screen, text='View Customers', font='Times', height=1, width=30, fg='white', bg='#000000',command=view_customer).pack()
    Label(login_success_screen,bg="#000000").pack()
    Button(login_success_screen, text='Search Customer', font='Times', height=1, width=30, fg='white', bg='#000000',command=search_customer).pack()
    Label(login_success_screen,bg="#000000").pack()
    Button(login_success_screen, text='Delete Customer', font='Times', height=1, width=30, fg='white', bg='#000000',command=delete_customer).pack()
    Label(login_success_screen,bg="#000000").pack()
    Button(login_success_screen, text='Update Customer Details',font='Times', height=1, width=30, fg='white',bg='#000000',command=update_customer).pack()
    Label(login_success_screen,bg="#000000").pack()
    
    Button(login_success_screen,text='LOGOUT', height='1', width='20',font='garamond',borderwidth=5,bg='#d90166',fg="white",command=view_success).pack() 

    
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title('Confirmation')
    password_not_recog_screen.geometry('250x250')    
    password_not_recog_screen.configure(bg="#000000")
    Label(password_not_recog_screen,bg="#000000").pack()
    Label(password_not_recog_screen, text='Invalid Credentials',font="Times",bg="#000000",width=20,fg="white").pack()
    Label(password_not_recog_screen,bg="#000000").pack()
    Label(password_not_recog_screen,bg="#000000").pack()
    Button(password_not_recog_screen, text='OK',height='1', width='15',font='garamond', borderwidth=5,bg='#d90166',fg='white', command=delete_password_not_recognised).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title('User not found')
    user_not_found_screen.geometry('212x212')
    Label(user_not_found_screen, text='User not found').pack()
    Button(user_not_found_screen, text='OK', command=delete_user_not_found).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found():
    user_not_found_screen.destroy()

def view_success():
    main_screen.destroy()    

def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg="#000000")
    main_screen.geometry("320x200")
    main_screen.title('Home')
    Label(text="MEDICAL STORE MANAGEMENT SYSTEM",bg='#d90166', fg='black', font='Times',width="512", height="2").pack()
    Label(bg='#000000').pack()
    Label(text='Login Here', height='1',font='Times',bg='#000000',fg="white").pack()
    Label(bg='#000000').pack() 
    Button(text='ADMIN', height='1', width='20',font='garamond', command=login,borderwidth=5,bg='#d90166',fg="white").pack() 

    main_screen.mainloop()


main_page()

