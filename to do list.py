from tkinter import * 
root=Tk()
root.title("TO-DO LIST")
root.geometry("300x450")
task_list=[]

def addtask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        task_list.append(task)
        listbox.insert(END,task)

def done():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        listbox.delete(ANCHOR)
        

label1=Label(root,text="TO-DO LIST",font="ariel,40,bold",fg="white",bg="black")
label1.place(x=80,y=20)

frame=Frame(root,width=400,height=40,bg="orange")
frame.place(x=0,y=100)

task=StringVar()
task_entry=Entry(frame,width=18,font="lucida,30",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="Add task",font="ariel,5,bold",bg="brown",fg="white",width=7,command=addtask)
button.place(x=210,y=0)

listframe=Frame(root,bd=3,width=700,height=280,bg="black")
listframe.pack(padx=0,pady=160)

listbox=Listbox(listframe,font="ariel,60",width=40,height=16,bg="grey",fg="white")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

btn2=Button(root,text="DONE",bd=0,bg="green",fg="white",command=done)
btn2.place(x=100,y=330) 
root.mainloop
