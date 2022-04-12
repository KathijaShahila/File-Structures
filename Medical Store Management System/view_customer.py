from tkinter import *
import os


def main_page():
    global main_screen
    main_screen = Tk()
    main_screen.configure(bg="#000000")
    main_screen.title('View Customers')
    main_screen.geometry('450x400')
    frame = Frame(main_screen)
    grid=Frame(frame)
    Label(main_screen, text='                         ',bg='#000000').grid(row=0)
    Label(main_screen, text="Customer Details",font='Times',bg='#000000',fg='white',width=18).grid(row=1, column=1, columnspan=7)
    Label(main_screen, text='               ',bg='#000000').grid(row=2)
    Label(main_screen, text='       Name      ',font='Garamond',bg='#d90166',fg='white').grid(row=3, column=1)
    Label(main_screen, text='               ',bg='#000000').grid(row=3)
    Label(main_screen, text='   Address ',font='Garamond',bg='#d90166',fg='white').grid(row=3, column=3)
    Label(main_screen, text='               ',bg='#000000').grid(row=4)
    Label(main_screen, text='     Phone Number   ',font='Garamond',bg='#d90166',fg='white').grid(row=3, column=5)
    Label(main_screen, text='                   ',bg='#000000').grid(row=3)
   
    i=8
    for line in open("customer.txt","r").readlines():
        cus = line.split()
        Label(main_screen, text=cus[1],font='Garamond',fg='white',bg='#000000').grid(row=i, column=1)
        Label(main_screen, text=cus[2],font='Garamond',fg='white',bg='#000000').grid(row=i, column=3)
        Label(main_screen, text=cus[0],font='Garamond',fg='white',bg='#000000').grid(row=i, column=5)
       
        i = i + 1
    
    main_screen.mainloop()
    
    
main_page()    