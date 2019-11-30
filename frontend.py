import tkinter as tk
from tkinter import *
import pymongo
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv('suicides.csv')

# importing module 
from pymongo import MongoClient 

# creation of MongoClient 
#client=MongoClient() 

# Connect with the portnumber and host 
client = MongoClient("localhost", 27017) 

# Access database 
mydatabase = client["mydb"] 

# Access collection of the database 
mycollection=mydatabase["sss"]

   
    
def Search():
    
    root2=tk.Tk()
    root2.geometry('800x800')
    root2.configure(background='#bdbdbd')
    root2.title('Search')
    
    
    
    def search():
        state=State.get()
        d=mycollection.find({"State":state}).limit(1000)
        

        
        eula.delete(0, 'end')#to clear listbox
        for i in d:
            eula.insert(END,str(i))#to insert text into listbox    
            
  
    q=tk.StringVar(root2)
    q.set('')
    f1=tk.Frame(root2,bg='#bdbdbd')
    at=tk.Label(f1,text="State",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='left')
    
    State=tk.Entry(f1,textvariable=q)
    State.pack(padx=5,pady=10,side='left')
    btu=tk.Button(f1,text="Search",fg='black',font="Helvetica 15 bold",command=search,width=8)
    btu.pack(padx=5,pady=10,side='left')
    f1.pack()
    xscrollbar = Scrollbar(root2, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    # Vertical (y) Scroll Bar
    yscrollbar = Scrollbar(root2,orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)

    # Text Widget
    eula = Listbox(root2, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set,height=90)
    eula.pack(fill=X)
        

    # Configure the scrollbars
    xscrollbar.config(command=eula.xview)
    yscrollbar.config(command=eula.yview)
    
    
    
    
    
    root2.mainloop()
    
def Delete():
    root3=tk.Tk()
    root3.geometry('1000x600')
    root3.configure(background='#bdbdbd')
    root3.title('Delete')
    def delete():
        State1=State.get()
        Year1=int(Year.get())
        query={"State":State1,"Year":Year1}
        mycollection.delete_many(query)
    q=tk.StringVar(root3)
    q.set('')
    u=tk.IntVar(root3)
    f1=tk.Frame(root3,bg='#bdbdbd')
    at=tk.Label(f1,text="State",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='left')
    
    State=tk.Entry(f1,textvariable=q)
    State.pack(padx=5,pady=10,side='left')
    at1=tk.Label(f1,text="Year",font='Helvetica 18 bold',width=7,height=1)
    at1.pack(padx=5,pady=10,side='left')
    Year=tk.Entry(f1,textvariable=u)
    Year.pack(padx=5,pady=10,side='left')
    btu=tk.Button(f1,text="Delete",fg='black',font="Helvetica 15 bold",command=delete,width=8)
    btu.pack(padx=5,pady=10,side='left')
    f1.pack()
    root3.mainloop()

def hdr():
    root4=tk.Tk()
    root4.geometry('1100x800')
    root4.configure(background='#bdbdbd')
    root4.title('Search')
    
    
    
    def search():
        state=State.get()
        d=mycollection.find({"State":state}).sort([("Total",pymongo.DESCENDING)]).limit(100)

        

        
        eula.delete(0, 'end')#to clear listbox
        for i in d:
            eula.insert(END,str(i))#to insert text into listbox    
            
  
    q=tk.StringVar(root4)
    q.set('')
    f1=tk.Frame(root4,bg='#bdbdbd')
    at=tk.Label(f1,text="State",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='left')
    
    State=tk.Entry(f1,textvariable=q)
    State.pack(padx=5,pady=10,side='left')
    btu=tk.Button(f1,text="Search",fg='black',font="Helvetica 15 bold",command=search,width=8)
    btu.pack(padx=5,pady=10,side='left')
    f1.pack()
    xscrollbar = Scrollbar(root4, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    # Vertical (y) Scroll Bar
    yscrollbar = Scrollbar(root4,orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)

    # Text Widget
    eula = Listbox(root4, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set,height=90)
    eula.pack(fill=X)
        

    # Configure the scrollbars
    xscrollbar.config(command=eula.xview)
    yscrollbar.config(command=eula.yview)
    
    
    
    
    
    root4.mainloop()

def hdrc():
    root5=tk.Tk()
    root5.geometry('800x800')
    root5.configure(background='#bdbdbd')
    root5.title('Search')
    xscrollbar = Scrollbar(root5, orient=HORIZONTAL)
    xscrollbar.pack(side=BOTTOM, fill=X)
    # Vertical (y) Scroll Bar
    yscrollbar = Scrollbar(root5,orient=VERTICAL)
    yscrollbar.pack(side=RIGHT, fill=Y)

    # Text Widget
    eula = Listbox(root5, xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set,height=90)
    eula.pack(fill=X)
        

    # Configure the scrollbars
    xscrollbar.config(command=eula.xview)
    yscrollbar.config(command=eula.yview)
    d=mycollection.find().sort([("Total",pymongo.DESCENDING)]).limit(100)
    for i in d:
        eula.insert(END,str(i))#to insert text into listbox

def Update():
    def Upd():
        
        state=State.get()
        year=Year.get()
        tc=TC.get()
        age=Age.get()
        gender=Gender.get()
        typ=Type.get()
        dic={"$inc":{"Total" : 1 }}
        x = mycollection.update_one({"State":state},dic)
       
    
    root1=tk.Tk()
    root1.geometry('800x600')
    root1.configure(background='#bdbdbd')
    
    q=tk.StringVar(root1)
    q.set('')
    f1=tk.Frame(root1,bg='#bdbdbd')
    State=tk.Entry(f1,textvariable=q)
    State.pack(padx=5,pady=10,side='right')
    at=tk.Label(f1,text="State",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='right')
    f1.pack()
    
    r=tk.IntVar(root1)
    r.set('')
    f2=tk.Frame(root1,bg='#bdbdbd')
    Year=tk.Entry(f2,textvariable=r)
    Year.pack(padx=5,pady=10,side='right')
    at=tk.Label(f2,text="Year",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='right')
    f2.pack()
    s=tk.StringVar(root1)
    s.set('')
    f3=tk.Frame(root1,bg='#bdbdbd')
    TC=tk.Entry(f3,textvariable=s)
    TC.pack(padx=5,pady=10,side='right')
    at=tk.Label(f3,text="Type Code",font='Helvetica 18 bold',width=10,height=1)
    at.pack(padx=5,pady=10,side='right')
    f3.pack()
    t=tk.StringVar(root1)
    t.set('')
    f4=tk.Frame(root1,bg='#bdbdbd')
    Type=tk.Entry(f4,textvariable=t)
    Type.pack(padx=5,pady=10,side='right')
    at=tk.Label(f4,text="Type",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='right')
    f4.pack()
    u=tk.StringVar(root1)
    u.set('')
    f5=tk.Frame(root1,bg='#bdbdbd')
    Gender=tk.Entry(f5,textvariable=u)
    Gender.pack(padx=5,pady=10,side='right')
    at=tk.Label(f5,text="Gender",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='right')
    f5.pack()
    v=tk.StringVar(root1)
    v.set('')
    f6=tk.Frame(root1,bg='#bdbdbd')
    Age=tk.Entry(f6,textvariable=v)
    Age.pack(padx=5,pady=10,side='right')
    at=tk.Label(f6,text="Age Group",font='Helvetica 18 bold',width=10,height=1)
    at.pack(padx=5,pady=10,side='right')
    f6.pack()
    w=tk.IntVar(root1)
    w.set('')
    f32=tk.Frame(root1,bg='#bdbdbd')
    but=tk.Button(f32,text="Update",command=Upd,font="Helvetica 18 bold",width=10,height=1)
    but.pack(side='right',padx=5,pady=10)
    f33=tk.Frame(root1,bg='#bdbdbd')
    but=tk.Button(f33,text="Back",command=root1.destroy,font="Helvetica 18 bold",width=10,height=1)
    but.pack(side='right',padx=5,pady=10)
    f32.pack()
    f33.pack()
    root1.mainloop()
    

def Insert():
    def Ins():
        state=State.get()
        year=Year.get()
        tc=TC.get()
        age=Age.get()
        gender=Gender.get()
        total=Total.get()
        typ=Type.get()
        dic={"State" : state, "Year" : year, "Type_code" : tc, "Type" : typ, "Gender" : gender, "Age_group" : age, "Total" : total }
        x = mycollection.insert_one(dic)

    root1=tk.Tk()
    root1.geometry('800x600')
    root1.configure(background='#bdbdbd')
    q=tk.StringVar(root1)
    q.set('')
    f1=tk.Frame(root1,bg='#bdbdbd')
    State=tk.Entry(f1,textvariable=q)
    State.pack(padx=5,pady=10,side='right')
    at=tk.Label(f1,text="State",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='right')
    f1.pack()
    r=tk.IntVar(root1)
    r.set('')
    f2=tk.Frame(root1,bg='#bdbdbd')
    Year=tk.Entry(f2,textvariable=r)
    Year.pack(padx=5,pady=10,side='right')
    at=tk.Label(f2,text="Year",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='right')
    f2.pack()
    s=tk.StringVar(root1)
    s.set('')
    f3=tk.Frame(root1,bg='#bdbdbd')
    TC=tk.Entry(f3,textvariable=s)
    TC.pack(padx=5,pady=10,side='right')
    at=tk.Label(f3,text="Type Code",font='Helvetica 18 bold',width=10,height=1)
    at.pack(padx=5,pady=10,side='right')
    f3.pack()
    t=tk.StringVar(root1)
    t.set('')
    f4=tk.Frame(root1,bg='#bdbdbd')
    Type=tk.Entry(f4,textvariable=t)
    Type.pack(padx=5,pady=10,side='right')
    at=tk.Label(f4,text="Type",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='right')
    f4.pack()
    u=tk.StringVar(root1)
    u.set('')
    f5=tk.Frame(root1,bg='#bdbdbd')
    Gender=tk.Entry(f5,textvariable=u)
    Gender.pack(padx=5,pady=10,side='right')
    at=tk.Label(f5,text="Gender",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='right')
    f5.pack()
    v=tk.StringVar(root1)
    v.set('')
    f6=tk.Frame(root1,bg='#bdbdbd')
    Age=tk.Entry(f6,textvariable=v)
    Age.pack(padx=5,pady=10,side='right')
    at=tk.Label(f6,text="Age Group",font='Helvetica 18 bold',width=10,height=1)
    at.pack(padx=5,pady=10,side='right')
    f6.pack()
    w=tk.IntVar(root1)
    w.set('')
    f7=tk.Frame(root1,bg='#bdbdbd')
    Total=tk.Entry(f7,textvariable=w)
    Total.pack(padx=5,pady=10,side='right')
    at=tk.Label(f7,text="Total",font='Helvetica 18 bold',width=7,height=1)
    at.pack(padx=5,pady=10,side='right')
    f7.pack()
    f32=tk.Frame(root1,bg='#bdbdbd')
    but=tk.Button(f32,text="Insert",command=Ins,font="Helvetica 18 bold",width=10,height=1)
    but.pack(side='right',padx=5,pady=10)
    f33=tk.Frame(root1,bg='#bdbdbd')
    but=tk.Button(f33,text="Back",command=root1.destroy,font="Helvetica 18 bold",width=10,height=1)
    but.pack(side='right',padx=5,pady=10)
    f32.pack()
    f33.pack()
    root1.mainloop()

def plot():

    df = pd.read_csv('suicides.csv')
    yearwise= df[['Year', 'Total']].groupby('Year').sum()
    yearwise.reset_index(inplace = True)
    plt.rcParams.update({'font.size': 13})
    plt.figure(figsize= (25,10)) # Make a plot size
    trace = sns.barplot(x = yearwise['Year'], y = yearwise['Total'], data = yearwise)
        # Adding values on the top of the bars
    for index, row in yearwise.iterrows():
        trace.text(x = row.name, y = row.Total, s = str(row.Total),color='black', ha="center")
    plt.title('Year wise Suicide count')    
    plt.show()

def plot2():
    gender_wise = df[['Year', 'Gender','Total']].groupby(['Year', 'Gender']).sum()
    gender_wise.reset_index(inplace = True)
    plt.rcParams.update({'font.size': 18})
    plt.figure(figsize= (20,10)) # Make a plot size
    plt.title('Yearly Males & Females Sucides rate')
    ax = sns.barplot(x = 'Year', y = 'Total', hue = 'Gender', data = gender_wise)
    plt.show()

def plot3():
    reasons_set = df[df['Type_code'] == 'Causes']
    reasons_set['Type'].value_counts()
    reasons_set['Type'].value_counts()
    set1 = reasons_set[['Type','Total']]
    set1 = set1.groupby('Type').sum()
    set1.reset_index(inplace = True)
    set1 = set1.sort_values('Total', ascending = False)
    set1 = set1.reset_index(drop=True)
    plt.rcParams.update({'font.size': 7})
    plt.figure(figsize= (20,15)) # Make a plot size
    trace = sns.barplot(x = set1['Type'], y = set1['Total'], data = set1, orient = 'v')
    # Adding values on the top of the bars
    for index, row in set1.iterrows():
        trace.text(x = row.name, y = row.Total+ 10000, s = str(row.Total),color='black', ha="center")
    plt.title('Reasons for Suicides')    
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.show()


def plot4():
    state_count = df[['State','Total']]
    state_count = state_count.groupby('State').sum()
    state_count = state_count.sort_values('Total', ascending = False)
    state_count = state_count.reset_index()
    plt.figure(figsize = (20,15))
    state_count.plot(kind = 'bar',x = 'State', figsize = (15,5), title = 'States and Suicide count')
    plt.show()

def plot5():
    reasons_set = df[df['Type_code'] == 'Causes']
    reasons_set['Type'].value_counts()
    reasons_set['Type'].value_counts()
    gender_set = reasons_set[['Type', 'Gender', 'Total']]
    male_set = gender_set[gender_set['Gender'] == 'Male']
    male_set = male_set.groupby('Type').sum().reset_index()
    male_set = male_set.sort_values('Total', ascending = False)
    male_set = male_set.reset_index(drop=True)
    female_set = gender_set[gender_set['Gender'] == 'Female']
    female_set = female_set.groupby('Type').sum().reset_index()
    female_set = female_set.sort_values('Total', ascending = False)
    female_set = female_set.reset_index(drop=True)
    plt.rcParams.update({'font.size': 6})
    gender_set = gender_set.sort_values('Total', ascending = False)
    gender_set = gender_set.reset_index(drop = True)
    plt.figure(figsize= (20,10)) # Make a plot size
    plt.title('India "Suicide Reasons" and "Gender" from Year 2001 to 2012')
    ax = sns.barplot(x = 'Type',y = 'Total', hue = 'Gender', data = gender_set)
    plt.xticks(rotation = 90)
    plt.show()

    
root0=tk.Tk()
root0.title('India suicides data analysis')
root0.geometry('1000x800')
root0.configure(background='LightYellow4')
bt=tk.Label(root0,text="Ending ones own life is a very daring act, but people who commit suicide are cowards.",font="Helvetica 15 bold italic",width='700',fg='#e0e0e0',bg='slate blue')
bt.pack()
btu=tk.Button(root0,text="Insert",fg='black',font="Helvetica 20 bold",command=Insert,width=8)
btu.pack(padx=5,pady=10)
btu1=tk.Button(root0,text="High Death Rate from each State",fg='black',font="Helvetica 10 bold",command=hdr,width=28)
btu1.pack(padx=5,pady=10)
btu1=tk.Button(root0,text="High Death Rate all over the country",fg='black',font="Helvetica 10 bold",command=hdrc,width=30)
btu1.pack(padx=5,pady=10)
btu2=tk.Button(root0,text="Delete",fg='black',font="Helvetica 20 bold",command=Delete,width=8)
btu2.pack(padx=5,pady=10)

btu2=tk.Button(root0,text="Update",fg='black',font="Helvetica 20 bold",command=Update,width=8)
btu2.pack(padx=5,pady=10)
btu3=tk.Button(root0,text="Search",fg='black',font="Helvetica 20 bold",command=Search,width=8)
btu3.pack(padx=5,pady=10)
w = tk.Label(root0,text="Data Analysis Graphs ")
w.pack(padx=5,pady=10,side=tk.LEFT)
btu4=tk.Button(root0,text="Year Wise Graph",fg='black',font="Helvetica 10 bold",command=plot,width=18)
btu4.pack(padx=5,pady=10,side=tk.LEFT)
btu5=tk.Button(root0,text="Gender Wise Graph",fg='black',font="Helvetica 10 bold",command=plot2,width=18)
btu5.pack(padx=5,pady=10,side=tk.LEFT)
btu5=tk.Button(root0,text="Sucied reason Graph",fg='black',font="Helvetica 10 bold",command=plot3,width=18)
btu5.pack(padx=5, pady=10,side=tk.LEFT)
btu6=tk.Button(root0,text="State wise Graph",fg='black',font="Helvetica 10 bold",command=plot4,width=18)
btu6.pack(padx=5, pady=10,side=tk.LEFT)
btu7=tk.Button(root0,text="Gender wise reason",fg='black',font="Helvetica 10 bold",command=plot5,width=18)
btu7.pack(padx=5, pady=10,side=tk.LEFT)

root0.mainloop()
