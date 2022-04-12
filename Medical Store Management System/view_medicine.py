from tkinter import *
import os


def main_page():
    global main_screen
    main_screen1 = Tk()
    main_screen1.title('View Medicines')
    main_screen1.configure(bg="#000000")
    main_screen1.geometry('600x400')
    frame = Frame(main_screen1)
    grid=Frame(frame)
    Label(main_screen1, text='                         ',bg='#000000').grid(row=0)
    Label(main_screen1, text="Medicine Details",font='Times',bg='#000000',fg='white',width=18).grid(row=1, column=1, columnspan=7)
    Label(main_screen1, text='  ',bg='#000000').grid(row=2)
    Label(main_screen1, text='    Name   ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=1)
    Label(main_screen1, text='                 ',bg='#000000').grid(row=3)
    Label(main_screen1, text='   Manufacturer       ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=3)
    Label(main_screen1, text='               ',bg='#000000').grid(row=3)
    Label(main_screen1, text='     Rack No      ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=5)
    Label(main_screen1, text='                   ',bg='#000000').grid(row=3)
    Label(main_screen1, text='      Expiry    ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=7)
    Label(main_screen1, text='                   ',bg='#000000').grid(row=3)
    Label(main_screen1, text='      Price     ',font='Garamond',fg='white',bg='#d90166').grid(row=3, column=9)
    i=10
    for line in open("medicine.txt","r").readlines():
        cus = line.split()
        Label(main_screen1, text=cus[0],font='Garamond',fg='white',bg='#000000').grid(row=i, column=1)
        Label(main_screen1, text=cus[1],font='Garamond',fg='white',bg='#000000').grid(row=i, column=3)
        Label(main_screen1, text=cus[2],font='Garamond',fg='white',bg='#000000').grid(row=i, column=5)
        Label(main_screen1, text=cus[3],font='Garamond',fg='white',bg='#000000').grid(row=i, column=7)
        Label(main_screen1, text=cus[4],font='Garamond',fg='white',bg='#000000').grid(row=i, column=9)
        i = i + 1
   
    main_screen1.mainloop()
        
    
main_page() 