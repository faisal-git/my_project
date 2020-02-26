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
import numpy as np
from matplotlib import pyplot as plt


#--------------------------------for tkinter windows -------------------------------------------------
root=Tk()

root.geometry("1350x750+0+0")
root.title("dATA vISUALISATION")
root.configure(background = "black")

#------------------------------frame creation--------------------------------------------------------
top=Frame(root,width = 1350, height = 100, bd = 15,bg="LightSkyBlue1",relief="raise",padx=10,pady=10)
top.pack(side=TOP,fill=X,pady=20)

f1=Frame(root,bg='DeepSkyBlue3',bd=10,relief=RIDGE)
f2=Frame(root,bg='gray63',bd=20,relief=RIDGE)
f1.pack(side="left",fill=BOTH,expand=True,padx=35,pady=30)
f2.pack(side='right',fill=BOTH,expand=True,padx=35,pady=30)
#---------------------f3 and f4 is division of f2 in two halves-------------------------------------------------
f3=Frame(f2,bg='gray63')
f3.pack(side=TOP)
f4=Frame(f2,bg='gray63')
f4.pack()
f5=Frame(f2,bg='gray63',bd=10,relief=RIDGE)
f5.pack(fill=BOTH)
f6=Frame(f2,bg='gray63',bd=10,relief=RIDGE)
f6.pack(fill=BOTH)





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
    
#----------------------------------------------------------

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
#-----------------------------------------------------------
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
#---------------------------------------------------------
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
        
#----------------------------------------------------------------    


def data_wrangling():
    pass



def to_reset():
    global file_name
    file_name=""
    recreate()
#-----------------------------------------------------------------
def drop_col():
    global df
    if(file_name):
        val=col_entry.get()
        if(val):
            if val in df.columns:
                option=messagebox.askyesno("drop_column","Do you want to the  "+val+"  column ?")
                
                if(option):
                    
                    df.drop(val,axis=1,inplace=True)
                    info()
                else:
                    pass
            else:
                msgbx.showwarning("ABORT","No such column")
        
        else:
            msgbx.showwarning("ABORT","Enter a valid column_name")
            
        
    else:
        msgbx.showwarning("ABORT","No file is selected")
        
#-------------------------------------------------------------------
def nan_values():
    if(file_name):
        val=col_entry.get()
        if(val):
            if val in df.columns:
                    print(df[val].isna().sum(),df.shape[0])
                    per=(df[val].isna().sum()/df.shape[0])*100
                    print(per)
                    msgbx.showinfo("NaN_values",str(round(per,4))+"% data is NaN")
                
               
                    
                    
               
            else:
                msgbx.showwarning("ABORT","No such column")
        
        else:
            msgbx.showwarning("ABORT","Enter a valid column_name")
            
        
    else:
        msgbx.showwarning("ABORT","No file is selected")

#--------------------------------------------------------------------------------
def drop_row():
    if(file_name):
        #to give info of how many will be drop
        global df
        df=df.dropna(axis=0,how='any')
        info()
        
            
        
    else:
        msgbx.showwarning("ABORT","No file is selected")


#--------------------------------------------------------------------------------
def normalize():
    recreate()
    global df
    #-------------------checking shoud be done -----------------------------------
    #--------------------------survived vs ~survived------------------------------
    s=df['Survived'].value_counts()
    s_label=Label(f1,text="No. of passenger who didn't survived:    "+str(s[0]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    s_label.pack(padx=10,pady=10)
    t_label=Label(f1,text="Survived Passenger:  "+str(s[1]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    t_label.pack(padx=10,pady=10)
    s=df['Survived'].value_counts(normalize=True)
    u_label=Label(f1,text="% of passenger who did't survived:   "+str(round(s[0]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    u_label.pack(padx=10,pady=10)
    v_label=Label(f1,text="% of Survived Passenger:     "+str(round(s[1]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    v_label.pack(padx=10,pady=10)
    # -------------------------males(survived vs ~survived)------------------------------   
    s=df['Survived'][df['Sex']=='male'].value_counts()
    s_label=Label(f1,text="No. of male passenger who didn't survived:    "+str(s[0]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    s_label.pack(padx=10,pady=5)
    t_label=Label(f1,text="No. male passenger who survived  "+str(s[1]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    t_label.pack(padx=10,pady=5)
    s=df['Survived'][df['Sex']=='male'].value_counts(normalize=True)
    u_label=Label(f1,text="% of male passenger who did't survived:   "+str(round(s[0]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    u_label.pack(padx=10,pady=5)
    v_label=Label(f1,text="% of male passenger who survived :     "+str(round(s[1]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    v_label.pack(padx=10,pady=5) 
    #-------------------------- females(survived vs ~survived)---------------------------------------    
    s=df['Survived'][df['Sex']=='female'].value_counts()
    s_label=Label(f1,text="No. of female passenger who didn't survived:    "+str(s[0]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    s_label.pack(padx=10,pady=5)
    t_label=Label(f1,text="No. female passenger who survived  "+str(s[1]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    t_label.pack(padx=10,pady=5)
    s=df['Survived'][df['Sex']=='female'].value_counts(normalize=True)
    u_label=Label(f1,text="% of female passenger who did't survived:   "+str(round(s[0]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    u_label.pack(padx=10,pady=5)
    v_label=Label(f1,text="% of female passenger who survived :     "+str(round(s[1]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
    v_label.pack(padx=10,pady=5)     
        
        
        
        
        

#Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Latte, state = DISABLED)
        
        
#---------------------label-------------------------------------------------
data=Label(f5,text="DaTa WranGling's tooLs")
data.pack(pady=10)
Nan=Label(f5,text="")   
#-----------------------entry_point--------------------------------------------------------------
file_entry=Entry(f3,font=('arial', 12, 'bold'))
file_entry.pack(side=TOP,pady=10)
col_entry=Entry(f5,font=('arial', 12, 'bold'))
col_entry.pack(pady=10)
NaN_entry=Entry(f5,font=('arial', 12, 'bold'))
file_entry.pack(side=TOP,pady=10)

#--------------------------codes for Buttons ----------------------------------------------
button1=Button(f3,text='Open_csv',command=for_csv)
button2=Button(f3,text='Open_xls',command=for_xls)
button1.pack(side=LEFT,pady=10)
button2.pack(side=RIGHT,pady=10)
#----------------buttons for display and info-------------------------------------------------

button3=Button(f4,text='Display_Table_Canvas',command=display)
button3.grid(row=0,pady=10,padx=10)
button4=Button(f4,text='display_info',command=info)
button4.grid(row=0,column=4,pady=10,padx=10)
#-----------------------buttons for data wrangling---------------------------------------------
button5=Button(f5,text='Drop_column',command=drop_col)
button5.pack(side=RIGHT,padx=10,pady=10)

button6=Button(f5,text='% of_NaN_values',command=nan_values)
button6.pack(side=RIGHT,padx=10,pady=10)

button7=Button(f5,text="drop_row_with_NaN",command=drop_row)
button7.pack(side=RIGHT,padx=10,pady=10)

button8=Button(f5,text="Normalize",command=normalize)
button8.pack(side=RIGHT,padx=10,pady=10)









# button for clear all imported file 


#----------------Buttons ends--------------------------------------------------------------














root.mainloop()