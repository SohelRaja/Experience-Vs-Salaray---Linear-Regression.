from   tkinter import *
import numpy as np
class ModelReport:
    def __init__(self,root,acc,intercept,coef):
        self.root = root
        self.f = Frame(root, height=350, width=500)
        self.f.pack() 
        self.acc = acc
        self.intercept = intercept
        self.coef = coef
        self.acc = self.acc * 100
        self.coef = str(self.coef)
        self.coef = self.coef[1:-1]
        label0 = Label(self.f,text='Model Report', font=('Arial', 14, 'underline'),fg='Red')
        label1 = Label(self.f,text='Accuracy of the Model is : '+str(self.acc), font=('Arial', 12),fg='Blue')
        label2 = Label(self.f,text='Intercept of the Model is : '+str(self.intercept), font=('Arial', 12),fg='Black')
        label3 = Label(self.f,text='Coefficient of the Model is : '+self.coef, font=('Arial', 12),fg='Blue')
        exit_button = Button(self.f,text='Back', font=('Arial', 14), bg='Yellow',
                                    fg='Black', command=self.exit)
        label0.grid(row=1, column=0)
        label1.grid(row=2, column=0)
        label2.grid(row=3, column=0)
        label3.grid(row=4, column=0)
        exit_button.grid(row=5,column=0,padx=20, pady=10)
    def exit(self):
        self.f.destroy()