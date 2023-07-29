#to-do list in pyhton
from tkinter import *
from tkinter import messagebox

#initialize root widget
root = Tk()

#empty list to enter tasks
task_list = []

# create task function
def CreateTask():
    task = entry.get()
    if task != "":
        lb.insert(END, task)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("*WARNING*" , "Please enter the task." )
    return

#delete task function
def DeleteTask():
    lb.delete(ANCHOR)
    return

#edit task function
def EditTask():
     
     #fetching value of selected task with curselection()
     selected_tsk = lb.curselection()
     if selected_tsk:
         selected_tsk_index =selected_tsk[0]
         edited_task = entry.get()
         if edited_task != "":
             
             #remove the selected task
             lb.delete(selected_tsk_index)

             #insert the edites task at same position
             lb.insert(selected_tsk_index , edited_task)
            
            #clear the entry widget
             entry.delete(0, "end")

         else:
             messagebox.showwarning("*WARNING" , "Please enter the task")

     else:
         messagebox.showwarning("*WARNING*" , "Please enter the task")
     return

#task exit function
def exitf():
    exit()
    return

#setting the window size
root.geometry("800x650") 
root.title("To-Do List")

#background color
root.config(bg="#CBFFA9", pady=50)
root.resizable(width=False, height=False)

#create frame widget
frame = Frame(root)
frame.pack()

#heading
heading = Label(frame, text= "To - Do List", font=("Times New Roman" , "25"), pady="18" ) 
heading.pack()

#litsbox 
lb = Listbox(frame, width="40", height="11", font=("Times New Roman", "12"), fg="black", bd=2)
lb.pack(fill=BOTH)

for task in task_list:
    lb.insert(END,task)

sb=Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#creating entry box
entry = Entry(root, font=("Times New Roman","20"))
entry.pack(pady=20)

#creating button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

credit_label = Label(root, text=" By Anushka Bhasme ",font=("Times New Roman", "10"), fg="black")
credit_label.pack()

#button-add task
AddTask = Button(button_frame, text="Add Task", font=("Times New Roman", "15"), bg="#ED2B2A", padx=20, pady=10, command=CreateTask)
AddTask.pack(fill=BOTH, expand=True, side=LEFT)

#button-edit task
EditTask = Button(button_frame, text="Edit Task", font=("Times New Roman", "15"), bg="#E80F88", padx=20, pady=10, command=EditTask)
EditTask.pack(fill=BOTH, expand=True, side=LEFT)

#button-delete task
DelTask = Button(button_frame, text="Delete Task", font=("Times New Roman", "15"), bg="#FEC260", padx=20, pady=10, command=DeleteTask)
DelTask.pack(fill=BOTH, expand=True, side=LEFT)

#button-exit
Exit = Button(button_frame, text="Exit", font=("Times New Roman", "15"), bg="azure4", padx=20, pady=10, command=exitf)
Exit.pack(fill=BOTH, expand=True, side=LEFT)

root.mainloop()
