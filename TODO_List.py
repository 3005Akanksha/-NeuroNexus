
import customtkinter
from tkinter import *
from tkinter import messagebox

app=customtkinter.CTk()
app.title('MY TO_DO LIST')
app.geometry('450x600')
app.config(bg='#e4c6dd')

font1=('Times New Roman',35,'bold','italic')
font2=('Times New Roman',20,'bold')
font3=('Times New Roman',15,'bold')

def add_task():
    task=task_entry.get()
    if task:
        tasks_list.insert(0,task)
        task_entry.delete(0,END)
        save_tasks()
    else:
        messagebox.showerror('Entry Not Found','Enter a Task')
        
def remove_task():
    selected=tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('Error', 'Choose a task to delete')
        
def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks=tasks_list.get(0,END)
        for task in tasks:
            f.write(task +"\n")
            
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks=f.readlines()
            for task in tasks:
                tasks_list.insert(0,task.strip())
    except FileNotFoundError:
        pass
    
   
    

title_label=customtkinter.CTkLabel(app,font=font1,text='My TO-DO LIST',text_color='#FFFFFF',bg_color='#382133',width=300)
title_label.place(x=80,y=20)

add_button=customtkinter.CTkButton(app,command=add_task,font=font2,text='New Task',text_color='#382133',border_color='#382133',fg_color='#fff',hover_color=' #e48897',cursor='hand2',corner_radius=8,width=120)
add_button.place(x=85,y=80)

remove_button=customtkinter.CTkButton(app,command=remove_task,font=font2,text='Remove',text_color='#382133',border_color='#382133',fg_color='#fff',hover_color=' #e48897',cursor='hand2',corner_radius=8,width=120)
remove_button.place(x=240,y=80)

task_entry=customtkinter.CTkEntry(app,font=font3,fg_color='#fff',text_color='#382133',border_color='#382133',width=300)
task_entry.place(x=70,y=120)

tasks_list=Listbox(app,width=39,height=20,font=font3)
tasks_list.place(x=80,y=200)

load_tasks()




app.mainloop()

