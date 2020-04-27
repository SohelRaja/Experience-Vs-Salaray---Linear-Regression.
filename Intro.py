from tkinter import *
def info(root):
    info_f = Frame(root, height=100, width=800)
    info_f.pack()
    main_lbl=Label(info_f, text='(Experience VS Salary) Linear Regression and Predict Salary based on Experience', fg='blue', font=('Arial', -15, 'bold underline'))
    main_lbl.place(x=110, y=25)
    lb1=Label(info_f, text='Name: Sohel Raja Molla, Roll No: 22, Department: CSE, Year: 3rd', fg='Green', font=('Arial', 10, 'bold'))
    lb1.place(x=110, y=55)
