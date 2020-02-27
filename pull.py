#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 19:07:44 2020

@author: fasial
"""



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
f5.pack(side=RIGHT,fill=BOTH,padx=35,pady=30)
f6=Frame(f2,bg='gray63',bd=10,relief=RIDGE)
f6.pack(side=LEFT,fill=BOTH,padx=35,pady=30)





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
    global file_name
    if(file_name):
        recreate()
        file_name=""
        file_entry.delete(0,END)
        file_entry.insert(0,"import file")
    print("xls")
    
    file_name=filedialog.askopenfilename()
    match=re.search(r'.xls',file_name)
    if match ==None:
        msgbx.showwarning("error","Required .xls file")
        file_name=""
    else:
        file_entry.insert(0,file_name)
        global df
        #df=pd.read_excel(file_name)
        df_excel= pd.read_excel(file_name)
        #df.to_csv('new.csv', index=False)
        #df_excel.to_csv('/new.csv', encoding='utf-8')
        #df=pd.read_excel('new.csv')
        #data_wrangling(data_frame)
    
#----------------------------------------------------------

def for_csv(event=None):
    global file_name
    if(file_name):
        recreate()
        file_name=""
        file_entry.delete(0,END)
        file_entry.insert(0,"import file")
    print('csv')
  
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
    recreate()
    if(file_name):
        """recreate()
        typ=re.search(r'.csv',file_name)
        if(typ==None):"""
        table = TableCanvas(f1, read_only=True)
        #for csv and xls file------------------------------
        table.importCSV(file_name)
            #print (self.table.model.columnNames)
        table.show()
        """else:
            table = tktable.Table(root, rows=10, cols=4)
            table.pack(side="top", fill="both", expand=True)"""
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
                option=msgbx.askyesno("drop_column","Do you want to the  "+val+"  column ?")
                
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
    
    global df
    #-------------------checking shoud be done -----------------------------------
    if(file_name):
    #--------------------------survived vs ~survived------------------------------
        recreate()
        try:
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
        except:
            s=df['survived'].value_counts()
            s_label=Label(f1,text="No. of passenger who didn't survived:    "+str(s[0]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            s_label.pack(padx=10,pady=10)
            t_label=Label(f1,text="Survived Passenger:  "+str(s[1]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            t_label.pack(padx=10,pady=10)
            s=df['survived'].value_counts(normalize=True)
            u_label=Label(f1,text="% of passenger who did't survived:   "+str(round(s[0]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            u_label.pack(padx=10,pady=10)
            v_label=Label(f1,text="% of Survived Passenger:     "+str(round(s[1]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            v_label.pack(padx=10,pady=10)
        # -------------------------males(survived vs ~survived)------------------------------
        try:
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
        except:
            s=df['survived'][df['sex']=='male'].value_counts()
            s_label=Label(f1,text="No. of male passenger who didn't survived:    "+str(s[0]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            s_label.pack(padx=10,pady=5)
            t_label=Label(f1,text="No. male passenger who survived  "+str(s[1]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            t_label.pack(padx=10,pady=5)
            s=df['survived'][df['sex']=='male'].value_counts(normalize=True)
            u_label=Label(f1,text="% of male passenger who did't survived:   "+str(round(s[0]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            u_label.pack(padx=10,pady=5)
            v_label=Label(f1,text="% of male passenger who survived :     "+str(round(s[1]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            v_label.pack(padx=10,pady=5)
            
        #-------------------------- females(survived vs ~survived)---------------------------------------
        try:
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
        except:
            s=df['survived'][df['sex']=='female'].value_counts()
            s_label=Label(f1,text="No. of female passenger who didn't survived:    "+str(s[0]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            s_label.pack(padx=10,pady=5)
            t_label=Label(f1,text="No. female passenger who survived  "+str(s[1]),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            t_label.pack(padx=10,pady=5)
            s=df['survived'][df['sex']=='female'].value_counts(normalize=True)
            u_label=Label(f1,text="% of female passenger who did't survived:   "+str(round(s[0]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            u_label.pack(padx=10,pady=5)
            v_label=Label(f1,text="% of female passenger who survived :     "+str(round(s[1]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
            v_label.pack(padx=10,pady=5)     
            if("Child" in df.columns):  
    
                s=df['Survived'][df['Child']==1].value_counts(normalize=True)
                u_label=Label(f1,text="% of children died:   "+str(round(s[0]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
                u_label.pack(padx=10,pady=5)
                v_label=Label(f1,text="% of children survived :     "+str(round(s[1]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
                v_label.pack(padx=10,pady=5) 
                s=df['Survived'][df['Child']==0].value_counts(normalize=True)
                u_label=Label(f1,text="% of Adult died:   "+str(round(s[0]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
                u_label.pack(padx=10,pady=5)
                v_label=Label(f1,text="% of Adult survived :     "+str(round(s[1]*100,2)),fg='white',font  = ('Arial', 16, 'bold'),bg='DeepSkyBlue3')
                v_label.pack(padx=10,pady=5)    
    else:
        msgbx.showwarning("ABORT","No file is selected")
        
        
        
#--------------------------------------------------------
def get_Graph():
    print('inside graph')
    if(file_name):
        recreate()
        try:
            plt.clf()
        except: 
            print("No_Graph_is_open")
        if(variable.get()=="No_of_passenger vs class"):
            try:
                print('Class wise no. of passengers')
                print(df.groupby(['Pclass']).size())
                df.groupby(['Pclass']).size().plot(kind='bar')
                plt.title('No. of Passengers Class wise')
                plt.ylabel('Number of passengers')
                plt.xlabel('Class -->')
                plt.tight_layout()
                plt.show()
            except:
                print('Class wise no. of passengers')
                print(df.groupby(['pclass']).size())
                df.groupby(['pclass']).size().plot(kind='bar')
                plt.title('No. of Passengers Class wise')
                plt.ylabel('Number of passengers')
                plt.xlabel('Class -->')
                plt.tight_layout()
                plt.show()

          
        elif(variable.get()=="No_of_passenger vs Class & Gender"):
            try:
                print('No. of passengers class wise , gender wise')
                print(df.groupby(['Pclass','Sex']).size())
                df.groupby(['Pclass','Sex']).size().unstack().plot(kind='bar',stacked=True)
                plt.title('No. of Passengers Classwise, Genderwise')
                plt.ylabel('Number of passengers')
                plt.xlabel('Class -->')
                plt.tight_layout()
                plt.show()
            except:
                print('No. of passengers class wise , gender wise')
                print(df.groupby(['pclass','sex']).size())
                df.groupby(['pclass','sex']).size().unstack().plot(kind='bar',stacked=True)
                plt.title('No. of Passengers Classwise, Genderwise')
                plt.ylabel('Number of passengers')
                plt.xlabel('Class -->')
                plt.tight_layout()
                plt.show()
                
                
       
        elif(variable.get()=="class wise Survival vs. Non-Survival"):
            try:
                print('Classwise survival vs non-survival')
                print(df.groupby(['Pclass','Survived']).size())
                df.groupby(['Pclass','Survived']).size().unstack().plot(kind='bar',stacked=True)
                plt.title('Classwise survival vs non-survival')
                plt.ylabel('Number of passengers')
                plt.xlabel('Class -->')
                plt.legend('Died','Survived')
                plt.tight_layout()
                plt.show()
            except:
                print('Classwise survival vs non-survival')
                print(df.groupby(['pclass','survived']).size()) 
                df.groupby(['pclass','survived']).size().unstack().plot(kind='bar',stacked=True)
                plt.title('Classwise survival vs non-survival')
                plt.ylabel('Number of passengers')
                plt.xlabel('Class -->')
                plt.legend('Died','Survived')
                plt.tight_layout()
                plt.show()
                
        elif(variable.get()=="Total_Passengers in different age group"):
            try:
                #Pie Chart
                age_bin = [0,18,25,40,60,100]
                #create the bin
                df['AgeBin'] = pd.cut(df.Age, bins= age_bin)
                d_temp = df[np.isfinite(df['Age'])]
                #Number of survivors based on age bin
                survivors = d_temp.groupby('AgeBin')['Survived'].agg(sum)
                #Total passengers in each bin
                total_passengers = d_temp.groupby('AgeBin')['Survived'].agg('count')
                
                plt.pie(total_passengers, labels = total_passengers.index.values.tolist(),autopct='%1.1f%%',shadow=True , startangle=90)
                plt.title('Total passengers in different age group')
                plt.show()
            except:
                #Pie Chart
                age_bin = [0,18,25,40,60,100]
                #create the bin
                df['AgeBin'] = pd.cut(df.age, bins= age_bin)
                d_temp = df[np.isfinite(df['age'])]
                #Number of survivors based on age bin
                survivors = d_temp.groupby('AgeBin')['survived'].agg(sum)
                #Total passengers in each bin
                total_passengers = d_temp.groupby('AgeBin')['survived'].agg('count')
                
                plt.pie(total_passengers, labels = total_passengers.index.values.tolist(),autopct='%1.1f%%',shadow=True , startangle=90)
                plt.title('Total passengers in different age group')
                plt.show()
            
        elif(variable.get()=="survivors in different age group"):
            try:
                #Pie Chart
                age_bin = [0,18,25,40,60,100]
                #create the bin
                df['AgeBin'] = pd.cut(df.Age, bins= age_bin)
                d_temp = df[np.isfinite(df['Age'])]
                #Number of survivors based on age bin
                survivors = d_temp.groupby('AgeBin')['Survived'].agg(sum)
                #Total passengers in each bin
                total_passengers = d_temp.groupby('AgeBin')['Survived'].agg('count')
                plt.pie(survivors, labels = survivors.index.values.tolist(),autopct='%1.1f%%',shadow=True,startangle=90)
                plt.title('Survivors in different age group')
                plt.show()
            except:
                #Pie Chart
                age_bin = [0,18,25,40,60,100]
                #create the bin
                df['AgeBin'] = pd.cut(df.age, bins= age_bin)
                d_temp = df[np.isfinite(df['age'])]
                #Number of survivors based on age bin
                survivors = d_temp.groupby('AgeBin')['survived'].agg(sum)
                #Total passengers in each bin
                total_passengers = d_temp.groupby('AgeBin')['survived'].agg('count')
                plt.pie(survivors, labels = survivors.index.values.tolist(),autopct='%1.1f%%',shadow=True,startangle=90)
                plt.title('Survivors in different age group')
                plt.show()
                


















            
        elif(variable.get()=="Class wise Survival vs. Non-Survival of child passengers"):
            if("child" in df.columns):
                try:
                    print('Classwise survival vs non-survival of child passengers')
                    print(df[df.child==1].groupby(['Pclass','Survived']).size())
                    df[df.child==1].groupby(['Pclass','Survived']).size().unstack().plot(kind='bar',stacked=True)
                    plt.title('Classwise survival vs non-survival of child passengers')
                    plt.tight_layout()
                    plt.ylabel('Child passengers')
                    plt.xlabel('Class -->')
                    plt.legend('Died','Survived')
                    plt.tight_layout()
                    plt.show()
                except:
                    print('Classwise survival vs non-survival of child passengers')
                    print(df[df.child==1].groupby(['pclass','survived']).size())
                    df[df.child==1].groupby(['pclass','survived']).size().unstack().plot(kind='bar',stacked=True)
                    plt.title('Classwise survival vs non-survival of child passengers')
                    plt.tight_layout()
                    plt.ylabel('Child passengers')
                    plt.xlabel('Class -->')
                    plt.legend('Died','Survived')
                    plt.tight_layout()
                    plt.show()
                
            else:
                msgbx.showwarning("ABORT","No child  columns exists add dummy column ")
                
        else:
            msgbx.showwarning("ABORT","No file is selected")
#--------------------------------------------------------
def dummy():
    if(file_name):
       
        try:
            
            df['child']=float('NaN')
            df['child'][df['Age']<18]=1
            df['child'][df['Age']>=18]=1
        except:
            df['child']=float('NaN')
            df['child'][df['age']<18]=1
            df['child'][df['age']>=18]=1
        recreate()
        info()
    else:
        msgbx.showwarning("ABORT","No file is selected")
    
#Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Latte, state = DISABLED)
        
        
#---------------------label-------------------------------------------------
data=Label(f5,text="DaTa WranGling's tooLs")
data.pack(pady=10,padx=30)
ds=Label(f6,text="DaTa visualisaton")
ds.pack(pady=10,padx=30)
Nan=Label(f5,text="")   
#-----------------------entry_point--------------------------------------------------------------
file_entry=Entry(f3,font=('arial', 12, 'bold'))
file_entry.pack(side=TOP,pady=10)
file_entry.insert(0,"improt file")
col_entry=Entry(f5,font=('arial', 12, 'bold'))
col_entry.pack(pady=10,padx=30)
NaN_entry=Entry(f5,font=('arial', 12, 'bold'))
file_entry.pack(side=TOP,pady=10)
#---------------------optionmenu in f6-----------------------------------------------------------
variable = StringVar(f6)
variable.set("OptionS") 
OPTIONS=["No_of_passenger vs class","No_of_passenger vs Class & Gender",
         "class wise Survival vs. Non-Survival","Class wise Survival vs. Non-Survival of child passengers",
         "Total_Passengers in different age group","survivors in different age group"]


w = OptionMenu(f6, variable, *OPTIONS)
w.pack(padx=20)


#--------------------------codes for Buttons ----------------------------------------------
button1=Button(f3,text='Open_csv',bg="black",fg="white",command=for_csv)
button2=Button(f3,text='Open_xls',bg="black",fg="white",command=for_xls)
button1.pack(side=LEFT,pady=10)
button2.pack(side=RIGHT,pady=10)
#----------------buttons for display and info-------------------------------------------------

button3=Button(f4,text='Display_Table_Canvas',bg="black",fg="white",command=display)
button3.grid(row=0,pady=10,padx=10)
button4=Button(f4,text='display_info',bg="black",fg="white",command=info)
button4.grid(row=0,column=4,pady=10,padx=10)
#-----------------------buttons for data wrangling---------------------------------------------

button8=Button(f5,text="Normalize",bg="black",fg="white",command=normalize)
button8.pack(padx=30,pady=5)

button6=Button(f5,text='% of_NaN_values',bg="black",fg="white",command=nan_values)
button6.pack(padx=30,pady=5)

button7=Button(f5,text="drop_row_with_NaN",bg="black",fg="white",command=drop_row)
button7.pack(padx=30,pady=5)

button5=Button(f5,text='Drop_column',bg="black",fg="white",command=drop_col)
button5.pack(padx=30,pady=5)

button9=Button(f6,text="Add_dummy",bg="black",fg="white",command=dummy)
button9.pack(side=LEFT,padx=20,pady=10)

button10=Button(f6,text="get_Graph",bg="black",fg="white",command=get_Graph)
button10.pack(side=LEFT,padx=10,pady=10)

    







# button for clear all imported file 


#--------------------------Buttons ends--------------------------------------------------------------
#---------------------option menu for graphs-----------------------------------------------














root.mainloop()

   
