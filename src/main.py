from tkinter import Tk
from Model import TaskModel
from View import TaskView
from Controller import TaskController

if __name__ == "__main__":
    model = TaskModel()
    view = TaskView(Tk())
    controller = TaskController(model, view)
    view.root.mainloop()