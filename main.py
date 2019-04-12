from tkinter import *
import tkinter as tk
import os
import pickle
import facere_enfi as fi

master = Tk()
master.geometry("650x650") # opning the dam window
n=0
f=0
prof = Entry(master)
prof.pack()
prof.focus_set()
prof.place(x=200,y=60,width=250)

proftext = tk.Label(master, text="Profesur name")
proftext.pack()
proftext.place(relx=.2, rely=.1, anchor="c")

salla=Entry(master)
salla.pack()
salla.focus_set()
salla.place(x=200,y=100,width=250)

sallatext = tk.Label(master, text="name of the classrome")
sallatext.pack()
sallatext.place(relx=.2, rely=.165, anchor="c")

IA= IntVar()
a = Checkbutton(master, text="IA", variable=IA)
a.pack()
a.place(relx=.139, rely=.3, anchor="c") #139

IA1_1= IntVar()
b= Checkbutton(master, text="IA1.1", variable=IA1_1)
b.pack()
b.place(relx=.25, rely=.37, anchor="c")

IA1_2= IntVar()
c= Checkbutton(master, text="IA1.2", variable=IA1_2)
c.pack()
c.place(relx=.25, rely=.45, anchor="c")

IA2_1= IntVar()
d= Checkbutton(master, text="IA2.1", variable=IA2_1)
d.pack()
d.place(relx=.4, rely=.37, anchor="c")

IA2_2= IntVar()
f= Checkbutton(master, text="IA2.2", variable=IA2_2)
f.pack()
f.place(relx=.4, rely=.45, anchor="c")

IA3_1= IntVar()
h= Checkbutton(master, text="IA3.1", variable=IA3_1)
h.pack()
h.place(relx=.55, rely=.37, anchor="c")

IA3_2= IntVar()
i= Checkbutton(master, text="IA3.2", variable=IA3_2)
i.pack()
i.place(relx=.55, rely=.45, anchor="c")


GTE= IntVar()
g = Checkbutton(master, text="GTE", variable=GTE)
g.pack()
g.place(relx=.139, rely=.55, anchor="c")

GTE1_1= IntVar()
b= Checkbutton(master, text="GTE1.1", variable=GTE1_1)
b.pack()
b.place(relx=.25, rely=.61, anchor="c")

GTE1_2= IntVar()
c= Checkbutton(master, text="GTE1.2", variable=GTE1_2)
c.pack()
c.place(relx=.25, rely=.70, anchor="c")

GTE2_1= IntVar()
d= Checkbutton(master, text="GTE2.1", variable=GTE2_1)
d.pack()
d.place(relx=.40, rely=0.61, anchor="c")

GTE2_2= IntVar()
f= Checkbutton(master, text="GTE2.2", variable=GTE2_2)
f.pack()
f.place(relx=.40, rely=.70, anchor="c")

GTE3_1= IntVar()
h= Checkbutton(master, text="GTE3.1", variable=GTE3_1)
h.pack()
h.place(relx=.56, rely=.61, anchor="c")

GTE3_2= IntVar()
i= Checkbutton(master, text="GTE3.2", variable=GTE3_2)
i.pack()
i.place(relx=.56, rely=.70, anchor="c")




def callback():
        database={}
        database_of_pickles={}
        list_of_dossies=[i for i in os.listdir("pickles")]
        isemprof=prof.get()
        salla_name=salla.get()
        n=IA.get()
        f=GTE.get()
        #print("n",n)
        #print("f",f)
                
        if(n==1 and f==1):
                for i in range(len(list_of_dossies)):
                        path="pickles"+"/"+list_of_dossies[i]
                        list_of_pickle_files=[i for i in os.listdir(path)]
                        #print(list_of_pickle_files)
                        for j in list_of_pickle_files:
                        	path1=path+"/"+j
                        	l=j.split("_")
                        	database_of_pickles[l[0]]=path1

                for i in database_of_pickles:
                	database[i]=[]
                	with open(database_of_pickles[i],'rb') as f:
                		li = pickle.load(f)
                		known_face_names=[i for i in li]
                		database[i].append(known_face_names)
                		known_face_encodings=[li[i] for i in li]
                		database[i].append(known_face_encodings)
               
        elif(n!=1 and f==1):
                path="pickles/GTE"
                list_of_pickle_files=[i for i in os.listdir(path)]
                for j in list_of_pickle_files:
                        path1=path+"/"+j
                        l=j.split("_")
                        database_of_pickles[l[0]]=path1
                for i in database_of_pickles:
                        database[i]=[]
                        with open(database_of_pickles[i],'rb') as f:
                                li = pickle.load(f)
                                known_face_names=[i for i in li]
                                database[i].append(known_face_names)
                                known_face_encodings=[li[i] for i in li]
                                database[i].append(known_face_encodings)
                
        elif(n==1 and f!=1):
                path="pickles/IA"
                list_of_pickle_files=[i for i in os.listdir(path)]
                for j in list_of_pickle_files:
                        path1=path+"/"+j
                        l=j.split("_")
                        database_of_pickles[l[0]]=path1
                for i in database_of_pickles:
                        database[i]=[]
                        with open(database_of_pickles[i],'rb') as f:
                                li = pickle.load(f)
                                known_face_names=[i for i in li]
                                database[i].append(known_face_names)
                                known_face_encodings=[li[i] for i in li]
                                database[i].append(known_face_encodings)
               
       
        fi.absance(database)

    
#fffffffffffff
b = Button(master, text="run", width=10, command=callback)
b.pack()
n=0
f=0
b.place(relx=.5, rely=.85, anchor="c")

mainloop()
e = Entry(master, width=50)
e.pack()

text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=RIGHT)
    return entry


user = makeentry(parent, "User name:", 10)
password = makeentry(parent, "Password:", 10, show="*")
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)

text = content.get()
content.set(text)


