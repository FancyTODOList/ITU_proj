from tkinter import Toplevel, Text, Button, END
from Model import TaskModel
from View import TaskView, CalendarView, TranslatorView
from googletrans import Translator
import datetime

# Todo list controller
class TaskController:
    def __init__(self, model, view):                                     # initialization
        self.model = model
        self.view = view
        
        self.load_tasks()                                                # load tasks from JSON file                                
        
        self.view.delete_button.config(command=self.delete_item)
        self.view.add_button.config(command=self.add_item)
        self.view.complete_button.config(command=self.complete_item)
        self.view.calendar_button.config(command=self.open_calendar)
        self.view.translator_button.config(command=self.open_translator) # set commands for buttons

    def delete_item(self):                                      # delete one task function
        selected_indices = self.view.my_list.curselection()     # get selected tasks        

        for index in reversed(selected_indices):               
            self.model.delete_task(index)
            self.view.my_list.delete(index)                     # delete tasks from listbox

    def add_item(self):                                         # add one task function                      
        if (self.view.my_entry.get() == ""):                    # if entry is empty, do nothing
            return
        task_text = self.view.my_entry.get()
        self.model.add_task(task_text)
        self.view.my_list.insert(END, task_text)                # add task to listbox and json file and clear entry
        self.view.my_entry.delete(0, END)

    def complete_item(self):                                    # complete/uncomplete one task function    
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

    def open_calendar(self):                                    # open calendar function            
        calendar_controller = CalendarController(None, None)
        # Get the date using the controller's get_date function
        today = calendar_controller.get_date()
        # Create a CalendarView instance with the controller and pass the date
        calendar_view = CalendarView(
            Toplevel(self.view.root), calendar_controller, today)
        # Set the controller on the view
        calendar_controller.view = calendar_view

    def open_translator(self):                                  # open translator function                
        # Create a TranslatorView instance first without a controller
        translator_view = TranslatorView(Toplevel(self.view.root), None)
        # Create a TranslatorController with the view
        translator_controller = TranslatorController(None, translator_view)
        # Set the controller on the view
        translator_view.controller = translator_controller

    def load_tasks(self):                                    # load tasks to listbox function      
        tasks = self.model.load_tasks()
        self.view.display_tasks(tasks)

# Translator controller
class TranslatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view                                    # initialization

    def translate(self, input, output):                     # translate function
        if (input.get("1.0", 'end-1c') == ""):
            return                                          # if input is empty, do nothing
        translator = Translator()
        text = input.get("1.0", 'end-1c')
        translation = translator.translate(text, dest='cs') # translate text from input in any language to output in Czech
        output.delete("1.0", END)
        output.insert(END, translation.text)

# Calendar controller
class CalendarController:
    def __init__(self, model, view):    # initialization
        self.model = model
        self.view = view

    def get_date(self):
        today = datetime.date.today()   # get today's date
        return today
