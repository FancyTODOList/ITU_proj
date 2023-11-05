import json

class TaskModel:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            with open("tasks.json", "w") as file:
                tasks = []
                json.dump(tasks, file)
        return tasks

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, task_text):
        task = {"text": task_text, "completed": False}
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def complete_task(self, index):
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        self.save_tasks()
    
    