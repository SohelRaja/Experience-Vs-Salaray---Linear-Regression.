# Conversion from CSV data to Microsoft Excel (xls) file
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msg
 
from pandastable import Table
from tkintertable import TableCanvas

import transferFile

class csv_to_excel_class:

    def __init__(self, root):

        self.root = root
        self.file_name = ''
        self.f = Frame(self.root, height=200, width=300)
        self.f.pack()    # Place the frame on root window
        
        # Creating label widgets
        self.message_label = Label(self.f,text='Conversion of CSV to Excel file',font=('Arial', 14,'underline'),fg='Red')

        # Buttons
        self.convert_button = Button(self.f,text='Convert', font=('Arial', 14), bg='Orange',
                                fg='Black', command=self.conv_to_xls)
        self.display_button = Button(self.f,text='Display', font=('Arial', 14), bg='Green',
                                fg='Black', command=self.display_xls_file)
        self.exit_button = Button(self.f,text='Back', font=('Arial', 14), bg='Red',
                                fg='Black', command=self.exit)

        # Placing the widgets using grid manager
        self.message_label.grid(row=1, column=1)
        self.convert_button.grid(row=2,column=0, padx=0, pady=15)
        self.display_button.grid(row=2,column=1, padx=10, pady=15)
        self.exit_button.grid(row=2,column=2, padx=10, pady=15)

    def conv_to_xls(self):         
        try:
            self.f.fileName = self.file_name = filedialog.askopenfilename(initialdir='/Desktop',title='Select a file',filetypes=(('csv file','*.csv'),('csv file','*.csv')))
            
            empsal_df = pd.read_csv(self.file_name)
            empsal_df = empsal_df.set_index('empno')

            # Next - Pandas DF to Excel file on disk
            if(len(empsal_df) == 0):      
                msg.showinfo('No Rows Selected', 'CSV has no rows')
            else:
                with pd.ExcelWriter('Dataset/empsal.xls') as writer:     # saves in the current directory
                        empsal_df.to_excel(writer,'EmpsalSheet')
                        writer.save()
                        msg.showinfo('Excel file ceated', 'Excel File created')                   
            
        except FileNotFoundError as e:
                msg.showerror('Error in opening file', e)

    def display_xls_file(self):
        try:
            empsal_df = pd.read_excel("Dataset/empsal.xls")
            if (len(empsal_df)== 0):
                msg.showinfo('No records', 'No records')
            else:
                pass   # To print in IDLE shell
             
            #Now display the DF in 'Table' object under'pandastable' module
            self.f2 = Frame(self.root, height=200, width=300) 
            self.f2.pack(fill=BOTH,expand=1)
            self.table = Table(self.f2, dataframe=empsal_df,read_only=True)
            self.table.show()
        except FileNotFoundError as e:
            print(e)
            msg.showerror('Error in opening file',e)
    def exit(self):
        self.f.destroy()
        self.f2.destroy()
        self.table.destroy()

   
