"""
main.py

Authors:
    - Ivan Onufriienko xonufr00
    - Oleksii Shelest xshele02

This file contains the main function for the ToDo List application. It creates the model, view, and controller, and starts the main event loop.
"""

from tkinter import Tk
from Model import TaskModel
from View import TaskView
from Controller import TaskController

if __name__ == "__main__":
    """
    @brief Main function for the ToDo List application.
    
    This function creates the model, view, and controller, and starts the main event loop.
    """
    model = TaskModel()  # Create the model
    view = TaskView(Tk(), model)  # Create the view
    TaskController(model, view)  # Create the controller
    view.root.mainloop()  # Start the main event loop