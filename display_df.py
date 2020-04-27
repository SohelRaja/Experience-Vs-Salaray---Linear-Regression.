from   tkinter import *
from   tkinter import messagebox as msg
import pandas as pd
from pandastable import Table

import transferFile

class create_df:

    def __init__(self, root):
        self.root = root
        self.f = Frame(self.root, height=350, width=500)
        self.f.pack()    # Place the frame on root window
        
        # Creating label widgets
        self.message_label = Label(self.f,text='Displaying the DataFrame',font=('Arial', 14, 'underline'),fg='Red')
        
        # Buttons
        self.confirm_button = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                fg='Black', command=self.conv_to_csv)
        self.exit_button = Button(self.f,text='Back', font=('Arial', 14), bg='Yellow',
                                fg='Black', command=self.exit)

        # Placing the widgets using grid manager
        self.message_label.grid(row=1, column=0)
        self.confirm_button.grid(row=2,column=0,padx=10, pady=5)
        self.exit_button.grid(row=3,column=0,padx=10, pady=5)
    
    def conv_to_csv(self):
        
        try:   
            # Now display the CSV in 'tkintertable' widget
            self.f2 = Frame(self.root, height=200, width=300) 
            self.f2.pack(fill=BOTH,expand=1)
            self.file_name = transferFile.file_import()
            self.df = pd.read_csv(self.file_name)
            self.df = self.df[['expyr','salary']]
            self.df = pd.DataFrame(self.df)
            self.table = Table(self.f2, dataframe=self.df)
            self.table.show()
    
        except FileNotFoundError as e:
            msg.showerror('Error in opening file', e.msg)
          

    def exit(self):
        self.f.destroy()
        self.f2.destroy()
        self.table.destroy()