from tkinter import Toplevel, Text, Button, END
from Model import TaskModel
from View import TaskView, CalendarView
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
        self.view.translator_button.config(command=self.translate) # set commands for buttons

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

    def translate(self):                     # translate function    
        selected_indices = self.view.my_list.curselection()
        from_language = self.view.from_language.get()
        to_language = self.view.to_language.get()
        translator = Translator()
        if (self.view.my_entry.get() != ""):
            task_text = self.view.my_entry.get() 
            translation = translator.translate(task_text, src=from_language, dest=to_language)
            self.view.my_entry.delete(0, END)  # Delete the current text
            self.view.my_entry.insert(0, translation.text)  # Insert the translated text
            return
        elif (len(selected_indices) != 0):
            for index in selected_indices:
                task_text = self.model.tasks[index]["text"]
                translation = translator.translate(task_text, src=from_language, dest=to_language)
                self.view.my_list.delete(index)
                self.view.my_list.insert(index, translation.text)   
                # Update the task text in the model
                self.model.tasks[index]["text"] = translation.text
            # Save the tasks
            self.model.save_tasks()

    def load_tasks(self):                                    # load tasks to listbox function      
        tasks = self.model.load_tasks()
        self.view.display_tasks(tasks)

# Calendar controller
class CalendarController:
    def __init__(self, model, view):    # initialization
        self.model = model
        self.view = view

    def get_date(self):
        today = datetime.date.today()   # get today's date
        return today
