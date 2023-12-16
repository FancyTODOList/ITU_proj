import json
#  This is the Model class. It is responsible for loading and saving the tasks.


class TaskModel:
    def __init__(self):
        # Load the tasks from the JSON file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:       # Open the JSON file
                tasks = json.load(file)
        except FileNotFoundError:
            with open("tasks.json", "w") as file:       # If the file doesn't exist, create it
                tasks = []
                json.dump(tasks, file)
        return tasks

    def save_tasks(self):
        with open("tasks.json", "w") as file:           # Save the tasks to the JSON file
            json.dump(self.tasks, file)

    def add_task(self, task_text, task_date):
        task = {"text": task_text, "date": task_date,
                "completed": False}  # Create a new task
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):                       # Delete a task
        del self.tasks[index]
        self.save_tasks()

    def complete_task(self, index):
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        # Set task as completed or not completed
        self.save_tasks()
