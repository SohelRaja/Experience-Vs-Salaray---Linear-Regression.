from tkinter import *
import os

from Intro import info
import display_csv as dc
import display_df as dd
import cnv_csv_to_xls as ccx
import model_training as MT
import predict as pred
from plot import scatter
from scatter_plot import scatterPlot
from model_report import ModelReport

class Main:
    # Constructor
    def __init__(self, root):
        self.root = root
        #info
        info(self.root)
        #calling the train function
        self.train = MT.train()
        # Create menubar
        self.menubar=Menu(root)
        root.config(menu=self.menubar)            # attach the menubar to root
        # Now create Single menubar operation menu
        self.menu=Menu(root, tearoff=0)

        self.menubar.add_cascade(label='Data Conversion', menu=self.menu)
        # Now create menu items under menubar 
        self.menu.add_command(label='Build CSV', command=self.create_csv)
        self.menu.add_command(label='Build DataFrame', command=self.create_df)
        self.menu.add_command(label='Convert to Excel', command=self.csv_to_xls)
         
        # Now add a separator
        self.menu.add_separator()
        # Now create a Exit menu
        self.menu.add_command(label='Exit', command=root.destroy)

        # Now create Data Maintenance operation menu
        self.data_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Reports', menu=self.data_menu)
        self.data_menu.add_command(label='Model Report', command=self.modelReport)
        self.data_menu.add_command(label='Scatter Plot', command=self.scatterPlot)
        self.data_menu.add_separator()
        self.data_menu.add_command(label='Plot', command=self.train_Plot)
        
        # Prediction Menu
        self.predict_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Prediction', menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict', command=self.predict)

    def create_df(self):
        dd.create_df(self.root)
    def create_csv(self):
        dc.create_csv(self.root)
    def csv_to_xls(self):
        ccx.csv_to_excel_class(self.root)
    
    def scatterPlot(self):
        scatterPlot()
    def train_Plot(self):
        scatter(self.train[0])
    def modelReport(self):    
        ModelReport(self.root,self.train[1],self.train[2],self.train[3])
        
    def predict(self):
        pred.prediction(self.root,self.train[0])   
#=====================================================================================================
  
root=Tk()
root.title('Project 4: Experience VS Salary in Linear Regression')

obj=Main(root)
root.geometry('800x600')
root.mainloop()



  
        
        
        
        
                 
