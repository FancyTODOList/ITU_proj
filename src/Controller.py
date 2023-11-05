from tkinter import Toplevel, Text, Button, END

from Model import TaskModel
from View import TaskView, CalendarView, TranslatorView
from googletrans import Translator


class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.delete_button.config(command=self.delete_item)
        self.view.add_button.config(command=self.add_item)
        self.view.complete_button.config(command=self.complete_item)
        self.view.calendar_button.config(command=self.open_calendar)  
        self.view.translator_button.config(command=self.open_translator)

    def delete_item(self):
        selected_indices = self.view.my_list.curselection()

        for index in reversed(selected_indices):
            self.model.delete_task(index)
            self.view.my_list.delete(index)

    def add_item(self):
        task_text = self.view.my_entry.get()
        self.model.add_task(task_text)
        self.view.my_list.insert(END, task_text)
        self.view.my_entry.delete(0, END)

    def complete_item(self):
        selected_indices = self.view.my_list.curselection()
        for index in selected_indices:
            self.model.complete_task(index)
            task_text = self.model.tasks[index]["text"]
            completed = self.model.tasks[index]["completed"]
            if completed:
                self.view.my_list.delete(index)
                self.view.my_list.insert(index, f"✅ {task_text}")
            else:
                self.view.my_list.delete(index)
                self.view.my_list.insert(index, task_text)

    def open_calendar(self):
        CalendarView(Toplevel(self.view.root))

    def open_translator(self):
        TranslatorView(Toplevel(self.view.root))


class TranslatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def translate(self):
        translator = Translator()
        text = self.view.input.get("1.0", 'end-1c')
        translation = translator.translate(text, dest='cs')
        self.view.output.delete("1.0", END)
        self.view.output.insert(END, translation.text)

class CalendarController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view
        