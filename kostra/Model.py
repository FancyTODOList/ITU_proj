"""
Model.py

Authors: 
    - Ivan Onufriienko xonufr00
    - Oleksii Shelest xshele02

This file contains the TaskModel class, which is responsible for loading and saving tasks.
"""
import json


class TaskModel:
    """
    @brief Class representing the model for tasks.
    @author Ivan Onufriienko xonufr00
    This class is responsible for loading and saving tasks.
    """
    def __init__(self):
        """
        @brief Constructor for TaskModel.
        @author Oleksii Shelest xshele02
        Loads the tasks from the JSON file.
        """
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        @brief Loads the tasks from the JSON file.
        @author Ivan Onufriienko xonufr00
        @return The list of tasks.
        """ 
        try:
            with open("tasks.json", "r") as file:       # Open the JSON file
                tasks = json.load(file)
        except FileNotFoundError:
            with open("tasks.json", "w") as file:       # If the file doesn't exist, create it
                tasks = []
                json.dump(tasks, file)
        return tasks

    def save_tasks(self):
        """
        @author Oleksii Shelest xshele02
        @brief Saves the tasks to the JSON file.
        """
        with open("tasks.json", "w") as file:           
            json.dump(self.tasks, file)

    def add_task(self, task_text, task_date):
        """
        @brief Adds a new task.
        @author Ivan Onufriienko xonufr00
        @param task_text The text of the task.
        @param task_date The date of the task.
        """
        task = {"text": task_text, "date": task_date,
                "completed": False}  # Create a new task
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):                       
        """
        @brief Deletes a task.
        @author Ivan Onufriienko xonufr00
        @param index The index of the task to delete.
        """
        del self.tasks[index]
        self.save_tasks()

    def complete_task(self, index):
        """
        @brief Marks a task as completed or uncompleted.
        @author Oleksii Shelest xshele02
        @param index The index of the task to complete or uncomplete.
        """ 
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        # Set task as completed or not completed
        self.save_tasks()
