#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:53:27 2020

@author: faisal
"""
""" """
from tkinter import *
from tkintertable import TableCanvas, TableModel
from tkinter import messagebox as msgbx
from tkinter import filedialog
import pandas as pd
import re


#--------------------------------for tkinter windows -------------------------------------------------
root=Tk()

root.geometry("1350x750+0+0")
root.title("dATA vISUALISATION")
root.configure(background = "black")

#------------------------------frame creation--------------------------------------------------------
top=Frame(root,width = 1350, height = 100, bd = 15,bg="LightSkyBlue1",relief="raise",padx=10,pady=10)
top.pack(side=TOP,fill=X,pady=20)

f1=Frame(root,bg='DeepSkyBlue3',bd=20,relief=RIDGE)
f2=Frame(root,bg='gray63',bd=20,relief=RIDGE)
f1.pack(side="left",fill=BOTH,expand=True,padx=35,pady=30)
f2.pack(side='right',fill=BOTH,expand=True,padx=35,pady=30)
#---------------------f3 and f4 is division of f2 in two halves-------------------------------------------------
f3=Frame(f2,bg='gray63')
f3.pack(side=TOP)
f4=Frame(f2,bg='gray63')
f4.pack()
f5=Frame(f2,bg='gray63')
f5.pack(side=BOTTOM,fill=BOTH)





#-----------label for heading--------------------------------------------------------------------
heading = Label(top, font  = ('Arial', 70, 'bold'), text = "datA visualisatioN", bg="LightSkyBlue1",bd = 10)

heading.pack()
#-------------heading ends here-------------------------------------------------------------------
#------data wranggling-------------














#-----global variable----------------

file_name=""


#------------funtion for buttons event---------------------------------
def recreate():
    global f1
    f1.destroy()
    f1=Frame(root,bg='DeepSkyBlue3',bd=20,relief=RIDGE)
    f1.pack(side="left",fill=BOTH,expand=True,padx=35,pady=30)
    

#-----------------------------------------------

def for_xls(event=None):
    print("xls")
    global file_name
    file_name=filedialog.askopenfilename()
    match=re.search(r'.xls',file_name)
    if match ==None:
        msgbx.showwarning("error","Required .xls file")
        file_name=""
    else:
        file_entry.insert(0,file_name)
        global df
        df=pd.read_excel(file_name)
        #data_wrangling(data_frame)
    


def for_csv(event=None):
    print('csv')
    global file_name
    file_name=filedialog.askopenfilename()
    print(file_name)
    match=re.search(r'.csv',file_name)
    if match==None:
        msgbx.showwarning("error","Required .xls file")
        file_name=""
    else:
        file_entry.insert(0,file_name)
        global df
        df=pd.read_csv(file_name)
        print(df.columns)
        #data_wrangling(data_frame)

def display(event=None):
    print("file",file_name)
    if(file_name!=""):
        recreate()
        table = TableCanvas(f1, read_only=True)
        #for csv and xls file------------------------------
        table.importCSV(file_name)
            #print (self.table.model.columnNames)
        table.show()
    else:
        
        msgbx.showwarning("error","No File is selected")

def info(event=None):
    if(file_name):
        
        recreate()
       
        naN_series=df.isna().sum()
        field="  cloumn_Name:\t  No_of_Null_values:\tdata_type:"
        Column=""
        No_of_null=""
        data_type=""
        for i in range(len(naN_series)):
            Column=Column+"\n"+df.columns[i]
            No_of_null=No_of_null+"\n"+str(naN_series[i])
            data_type=data_type+"\n"+str(df[df.columns[i]].dtype)
        f_label=Label(f1,text=field,fg='white',font  = ('Arial', 15, 'bold'),bg='DeepSkyBlue3')    
        c_label=Label(f1,text=Column,fg='black',font  = ('Arial', 14, 'bold'),bg='DeepSkyBlue3')
        n_label=Label(f1,text=No_of_null,fg='black', font  = ('Arial', 14, 'bold'),bg='DeepSkyBlue3')
        d_label=Label(f1,text=data_type,fg='black',font  = ('Arial', 14, 'bold'),bg='DeepSkyBlue3')
        # f_label.pack(side=TOP)
        # c_label.pack(side=LEFT)
       #  n_label.pack(side=LEFT)
       # d_label.pack(side=LEFT)
        f_label.grid(row=0,columnspan=4)
        c_label.grid(row=1,rowspan=3,column=0)
        n_label.grid(row=1,rowspan=3,column=2)
        d_label.grid(row=1,rowspan=3,column=3)
        
        shape="Total_No_of_Rows_in_the_dataSet:\t"+str(df.shape[0])+"\nTotal_No_of_columns_in_the_dataSet:\t"+str(df.shape[1])
        s_label=Label(f1,text=shape,fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
        s_label.grid(row=5,columnspan=3)
        
    else:
        msgbx.showwarning("ABORT","No file is selected")
        
    


def data_wrangling():
    pass



def to_reset():
    global file_name
    file_name=""
    recreate()
    

#Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Latte, state = DISABLED)
    

file_entry=Entry(f3,font=('arial', 12, 'bold'))
file_entry.pack(side=TOP,pady=10)

#--------------------------codes for Buttons ----------------------------------------------
button1=Button(f3,text='Open_csv',command=for_csv)
button2=Button(f3,text='Open_xls',command=for_xls)
file_entry.pack(side=TOP,pady=10)
button1.pack(side=LEFT,pady=10)
button2.pack(side=RIGHT,pady=10)
button3=Button(f4,text='Display_Table_Canvas',command=display)
button3.grid(row=0)
button4=Button(f4,text='display_info',command=info)
button4.grid(row=0,column=4)

# button for clear all imported file 


#----------------Buttons ends--------------------------------------------------------------














root.mainloop()