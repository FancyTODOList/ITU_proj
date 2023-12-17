"""
Controller.py

Authors:
    - Ivan Onufriienko xonufr00
    - Oleksii Shelest xshele02
    
This file contains the TaskController and CalendarController classes, which are used to control the interaction between the model and the view in the ToDo List application.
"""
from tkinter import Toplevel, Text, Button, END
from Model import TaskModel
from View import TaskView, CalendarView
from googletrans import Translator
import speech_recognition as sr
import datetime

# Todo list controller


class TaskController:
    """
    @brief Class representing the controller for tasks.
    @author Ivan Onufriienko xonufr00
    This class provides the interface for controlling the interaction between the model and the view for tasks.
    """
    def __init__(self, model, view):                                     # initialization
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
        self.view.calendar_button.config(command=self.open_calendar)
        self.view.translator_button.config(command=self.translate)
        self.view.micro_button.config(
            command=self.micro)  # set commands for buttons

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
        self.view.display_tasks(self.model.tasks, selected_date)

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

    def micro(self):
        """
        @brief Converts speech to text.
        @author Ivan Onufriienko xonufr00
        This method is called when the "Micro" button is clicked.
        """
        r = sr.Recognizer()
        mic = sr.Microphone()

        # From micro
        with mic as source:
            try:
                # 10 seconds waiting
                audio = r.listen(source, timeout=10)
                try:
                    # English
                    text = r.recognize_google(audio, language="en-US")
                    # print("You said: " + text)
                except sr.UnknownValueError:
                    try:
                        # Cestina
                        text = r.recognize_google(audio, language="cs-CZ")
                        # print("Řekli jste: " + text)
                    except sr.UnknownValueError:
                        # print("Sorry, speech not recognized.")
                        text = "Sorry, speech not recognized."
            except sr.WaitTimeoutError:
                text = "No speech detected"

            self.view.my_entry.delete(0, END)  # Clean Entry
            # Put the text
            self.view.my_entry.insert(0, text)

    # complete/uncomplete one task function

    def complete_item(self):
        """
        @brief Marks the selected task as completed or uncompleted.
        @author Oleksii Shelest xshele02
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
                else:
                    self.view.my_list.delete(index)
                    self.view.my_list.insert(index, task_text)
            else:
                # If the task doesn't exist for the selected date, add it to the model
                self.model.add_task(task_text, self.selected_date)

                # Update the view with the newly added task
                self.view.my_list.delete(index)
                self.view.my_list.insert(index, f"✅ {task_text}")

    # open calendar function

    def open_calendar(self):
        """
        @brief Opens the calendar view.
        @author Oleksii Shelest xshele02
        This method is called when the "Calendar" button is clicked.
        """
        calendar_controller = CalendarController(None, None)
        # Get the date using the controller's get_date function
        self.today = calendar_controller.get_date()
        # Create a CalendarView instance with the controller and pass the date
        calendar_view = CalendarView(
            Toplevel(self.view.root), calendar_controller, self.today)
        # Set the controller on the view
        calendar_controller.view = calendar_view
        self.view.root.wait_window(calendar_view.root)

        # Retrieve the selected date after the window is closed
        self.selected_date = calendar_view.get_selected_date()
        self.load_tasks()

    def translate(self):                     # translate function
        """
        @brief Translates the selected task or the text in the entry.
        @author Ivan Onufriienko xonufr00
        This method is called when the "Translate" button is clicked.
        """
        selected_indices = self.view.my_list.curselection()
        from_language = self.view.from_language.get()
        to_language = self.view.to_language.get()
        translator = Translator()
        if (self.view.my_entry.get() != ""):
            task_text = self.view.my_entry.get()
            translation = translator.translate(
                task_text, src=from_language, dest=to_language)
            self.view.my_entry.delete(0, END)  # Delete the current text
            # Insert the translated text
            self.view.my_entry.insert(0, translation.text)
            return
        elif (len(selected_indices) != 0):
            # Get the tasks for the selected date
            filtered_tasks = [
                task for task in self.model.tasks if task["date"] == self.selected_date]
    
            for index in selected_indices:
                # Check if the index is within the bounds of the filtered tasks list
                if 0 <= index < len(filtered_tasks):
                    # Get the index of the task within the entire tasks list
                    global_index = self.model.tasks.index(
                        filtered_tasks[index])
    
                    task_text = self.model.tasks[global_index]["text"]
                    translation = translator.translate(
                        task_text, src=from_language, dest=to_language)
                    self.view.my_list.delete(index)
                    self.view.my_list.insert(index, translation.text)
                    # Update the task text in the model
                    self.model.tasks[global_index]["text"] = translation.text
            # Save the tasks
            self.model.save_tasks()

    # load tasks to listbox function
    def load_tasks(self):
        """
        @brief Loads the tasks for the selected date.
        @author Ivan Onufriienko xonufr00
        This method is called when the selected date is changed.
        """
        tasks = self.model.load_tasks()
        self.view.display_tasks(tasks, self.selected_date)

# Calendar controller


class CalendarController:
    """
    @brief Class representing the controller for the calendar.
    @author Ivan Onufriienko xonufr00
    This class provides the interface for controlling the interaction between the model and the view for the calendar.
    """
    def __init__(self, model, view):    # initialization
        """
        @brief Constructor for CalendarController.
        @author Oleksii Shelest xshele02
        @param model The model containing the tasks.
        @param view The view for displaying and interacting with the calendar.
        """
        self.model = model
        self.view = view

    def get_date(self):
        """
        @brief Gets today's date.
        @author Oleksii Shelest xshele02
        @return Today's date.
        """
        today = datetime.date.today()   # get today's date
        return today
