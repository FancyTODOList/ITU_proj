from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from tkinter import Tk, Toplevel
from tkcalendar import Calendar
import sys
import json

root = Tk()
root['bg'] = '#DDBEAA'
root.title('ToDo List!')
root.geometry("500x500")
root.resizable(width=False, height=False)

my_font = Font(family="Regular", size=30, weight="bold")

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame, font=my_font, width=25, height=5, bg="#DDBEAA", bd=0,
                  fg="#000000", highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    with open("tasks.json", "w") as file:
        tasks = []
        json.dump(tasks, file)

for task in tasks:
    if (task["completed"] == False):
        my_list.insert(END, task["text"])
    else:
        my_list.insert(END, f"✅ {task['text']}")


def delete_item():
    selected_indices = my_list.curselection()

    for index in reversed(selected_indices):
        task = tasks.pop(index)
        my_list.delete(index)

    save_tasks(tasks)


def add_item():
    task_text = my_entry.get()
    task = {"text": task_text, "completed": False}
    my_list.insert(END, task_text)
    my_entry.delete(0, END)
    tasks.append(task)
    save_tasks(tasks)


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def open_calendar():
    calendar_window = Toplevel(root)
    calendar_window.title("Calendar")
    calendar_window.configure(background='#469597')
    calendar_window.geometry("350x250")
    calendar_window.resizable(width=False, height=False)

    window_width = calendar_window.winfo_reqwidth()
    window_height = calendar_window.winfo_reqheight()

    x = (root.winfo_reqwidth() - window_width) // 2 + root.winfo_x()
    y = (root.winfo_reqheight() - window_height) // 2 + root.winfo_y()

    calendar_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    cal = Calendar(calendar_window, selectmode="day",
                   year=2023, month=11, day=2)
    cal.pack(padx=20, pady=20)


def open_translator():
    translator_window = Toplevel(root)
    translator_window.title("Translator")

    window_width = translator_window.winfo_reqwidth()
    window_height = translator_window.winfo_reqheight()

    x = (root.winfo_reqwidth() - window_width) // 2 + root.winfo_x()
    y = (root.winfo_reqheight() - window_height) // 2 + root.winfo_y()

    translator_window.geometry(f"{window_width}x{window_height}+{x}+{y}")


def complete_item():
    selected_indices = my_list.curselection()
    for index in selected_indices:
        task = tasks[index]
        if not task["completed"]:
            task["completed"] = True
            my_list.delete(index)
            my_list.insert(index, f"✅ {task['text']}")
            save_tasks(tasks)
        else:
            task["completed"] = False
            my_list.delete(index)
            my_list.insert(index, f"{task['text']}")
            save_tasks(tasks)


delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
complete_button = Button(button_frame, text="Complete", command=complete_item)
calendar_button = Button(button_frame, text="Calendar", command=open_calendar)
translator_button = Button(
    button_frame, text="Translator", command=open_translator)

calendar_button.grid(row=0, column=0, sticky='ew', pady=10, ipadx=10)
complete_button.grid(row=0, column=1, sticky='ew', pady=10, ipadx=10)
delete_button.grid(row=0, column=2, sticky='ew', pady=10, ipadx=10)
translator_button.grid(row=0, column=3, sticky='ew', pady=10, ipadx=10)
add_button.grid(row=1, column=0, columnspan=4, sticky='ew', pady=10)


root.mainloop()
