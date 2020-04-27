from   tkinter import *
import numpy as np

class prediction:
    def __init__(self, root, pred):
        self.root = root
        self.pred = pred
        self.f = Frame(self.root, height=350, width=500)
        self.f.pack()    # Place the frame on root window

        # Creating label widgets
        self.message_label1 = Label(self.f,text='SALARY PREDICTION',font=('Arial', 16,'underline'),fg='Red')
        self.message_label2 = Label(self.f,text='Experience(years) : ',font=('Arial', 14))
        
        # Buttons
        self.confirm_button = Button(self.f,text='Predict', font=('Arial', 14), bg='Orange',
                                fg='Black', command=self.predict)
        self.exit_button = Button(self.f,text='Back', font=('Arial', 14), bg='Yellow',
                                fg='Black', command=self.exit)

        #input field
        self.exp_years = Entry(self.f, font=('Arial', 14), width=10)
        self.exp_years.focus()

        #New Frame
        self.f2 = Frame(self.root, height=350, width=500)
        self.f2.pack()
        self.output_label = Label(self.f2,text='', font=('Arial', 14, 'bold'),fg='Red')
        
        # Placing the widgets using grid manager
        self.message_label1.grid(row=1, column=1)
        self.message_label2.grid(row=2, column=0,pady=10)
        self.exp_years.grid(row=2, column=1,pady=10)
        self.confirm_button.grid(row=2,column=2,pady=10)
        self.exit_button.grid(row=2,column=3,padx=20,pady=10)
        
        self.output_label.grid(row=5, column=0,pady=10)
    
    def exit(self):
        self.f.destroy()
        self.f2.destroy()
        
    def predict(self):
        self.value = self.exp_years.get()
        self.salary = str(self.pred.predict([[np.int64(self.value)]]))
        self.salary = self.salary[1:-1]
        print(self.salary)
        self.output_label.config(text = 'The Expected Salary for '+str(self.value) +' years of Experience is : ' + self.salary)
        self.exp_years.delete(0,END)