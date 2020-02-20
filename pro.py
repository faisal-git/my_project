#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:03:51 2020

@author: fasial
"""





from tkinter import *
from tkinter import filedialog
import pandas as pd





root=Tk()






#drop down to show different kinds of information to display
def info():
    pass


#drop doem for graphs and plots
def graphs_plots():
    pass


def data_wrangling(df):
    #filename=filedialog.askopenfilename()
    
    print(df.head)
    label=Label(root,text=df.columns,fg="red")
    label.pack()
    #print('Slected: ',filename)



def for_xls(event=None):
    print("xls")
    
    file_name=filedialog.askopenfilename()
    data_frame=pd.read_excel(file_name)
    data_wrangling(data_frame)
    


def for_csv(event=None):
    print('csv')
    file_name=filedialog.askopenfilename()
    data_frame=pd.read_csv(file_name)
    data_wrangling(data_frame)
    






button1=Button(root,text='Open_csv',command=for_csv)
button2=Button(root,text='Open_xls',command=for_xls)
button1.pack()
button2.pack()
root.mainloop()