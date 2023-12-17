"""
Controller.py

Authors:
    - Ivan Onufriienko xonufr00
    - Oleksii Shelest xshele02
    - Václav Zapletal xzaple40

This file contains the TaskController and CalendarController classes, which are used to control the interaction between the model and the view in the ToDo List application.
"""
from tkinter import *
from Model import TaskModel
from View import TaskView
import datetime
from pocketsphinx import LiveSpeech


# Todo list controller


class TaskController:
    """
    @brief Class representing the controller for tasks.
    @author Ivan Onufriienko xonufr00
    This class provides the interface for controlling the interaction between the model and the view for tasks.
    """
    def __init__(self, model, view):
        """
        @brief Constructor for TaskController.
        @author Oleksii Shelest xshele02
        @param model The model containing the tasks.
        @param view The view for displaying and interacting with tasks.
        """                                  
        self.model = model
        self.view = view

        self.selected_date = datetime.date.today().strftime("%d. %m. %Y")
        # load tasks from JSON file
        self.load_tasks()

        self.view.delete_button.config(command=self.delete_item)
        self.view.add_button.config(command=self.add_item)
        self.view.complete_button.config(command=self.complete_item)
        self.view.speech_button.config(command=self.speech_to_text)
        


    # delete one task function
    def delete_item(self):
        """
        @brief Deletes the selected task.
        @author Oleksii Shelest xshele02
        This method is called when the "Delete Task" button is clicked.
        """
        # Get selected indices from the Listbox
        selected_indices = self.view.my_list.curselection()

        # Get the selected date (you need to have this attribute set somewhere in your code)
        selected_date = self.selected_date

        # If there are selected indices
        if selected_indices:
            filtered_tasks = [
                task for task in self.model.tasks if task["date"] == selected_date]

            for index in reversed(selected_indices):
                # Check if the index is within the bounds of the filtered tasks list
                if 0 <= index < len(filtered_tasks):
                    # Get the index of the task within the entire tasks list
                    global_index = self.model.tasks.index(
                        filtered_tasks[index])

                    # Delete the task from the model and the view (Listbox)
                    self.model.delete_task(global_index)
                    self.view.my_list.delete(global_index)
        self.view.display_tasks(self.model.tasks)

    def add_item(self):                                         # add one task function
        """
        @brief Adds a new task.
        @author Oleksii Shelest xshele02
        This method is called when the "Add Task" button is clicked.
        """
        if (self.view.my_entry.get() == ""):                    # if entry is empty, do nothing
            return
        task_text = self.view.my_entry.get()
        task_date = self.selected_date
        self.model.add_task(task_text, task_date)
        # add task to listbox and json file and clear entry
        self.view.my_list.insert(END, task_text)
        self.view.my_entry.delete(0, END)

    def complete_item(self):
        """
        @brief Marks the selected task as completed or uncompleted and increments points counter.
        @author Oleksii Shelest xshele02
        @author Zapletal Václav xzaple40 (Added only increment for points)
        This method is called when the "Complete" button is clicked.
        """
        selected_indices = self.view.my_list.curselection()

        # Iterate through selected tasks
        for index in selected_indices:
            task_info = self.view.my_list.get(
                index)  # Get task info from the view
            # Remove completion indicator from task text
            task_text = task_info.lstrip('✅ ')

            # Find the task index in the model based on text and the selected date
            task_index = None
            for i, task in enumerate(self.model.tasks):
                if task['text'] == task_text and task['date'] == self.selected_date:
                    task_index = i
                    break

            # Check if the task exists for the selected date
            if task_index is not None:
                # If the task exists, update its completion status in the model
                self.model.complete_task(task_index)

                # Update the view based on the completion status
                task_text = self.model.tasks[task_index]["text"]
                completed = self.model.tasks[task_index]["completed"]

                if completed:
                    self.view.my_list.delete(index)
                    self.view.my_list.insert(index, f"✅ {task_text}")
                    
                    # Increment points_value only if the task is completed
                    points_value = int(self.view.points_var.get())
                    points_value += 1
                    self.view.points_var.set(str(points_value))

                else:
                    self.view.my_list.delete(index)
                    self.view.my_list.insert(index, task_text)
            else:
                # If the task doesn't exist for the selected date, add it to the model
                self.model.add_task(task_text, self.selected_date)

                # Update the view with the newly added task
                self.view.my_list.delete(index)
                self.view.my_list.insert(index, f"✅ {task_text}")
            
                points_value = int(self.view.points_var.get())
                points_value += 1
                self.view.points_var.set(str(points_value))
            
    def load_tasks(self):
        """
        @brief Loads the tasks for the selected date.
        @author Ivan Onufriienko xonufr00
        This method is called when the selected date is changed.
        """
        tasks = self.model.load_tasks()
        self.view.display_tasks(tasks)

    def speech_to_text(self):
        """
        @brief Convert speech to text
        @author Václav Zapletal xzaple40
        """
        speech = LiveSpeech()

        for phrase in speech:
            task_text = str(phrase)
            # Extract the first word from the recognized speech
            first_word = task_text.split()[0]
    
            self.process_first_word(first_word)

            break  

    def process_first_word(self, first_word):
        """
        @brief Processing of the first spoken word
        @author Václav Zapletal xzaple40
        """
        self.view.my_entry.delete(0, END)
        self.view.my_entry.insert(END, first_word)