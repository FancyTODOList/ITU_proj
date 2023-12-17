from tkinter import *
from tkinter.font import Font
from tkmacosx import Button
from tkcalendar import Calendar

class TaskView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.root['bg'] = 'blue'
        self.root.title('ToDo List!')
        window_width = 700
        window_height = 500

        header_color = "#4d5198"
        body_color = "#daf2dc"
        button_color = header_color
        button_text_color = "white"

        self.points_var = StringVar()
        points_value = "0"
        self.points_var.set(points_value)

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position for centering
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window geometry
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.my_font = Font(family="Arial", size=20, weight="bold")



        # Header Frame
        self.header_frame = Frame(root, background=header_color, height=window_height // 2)
        self.header_frame.grid(row=0, column=0, sticky="nsew")
        
        # Header
        self.header_label = Label(self.header_frame, text="ToDo list", font=("Arial", 50), bg= header_color,fg="white")
        self.header_label.pack(anchor="center")  # Use pack instead of grid

        self.point_label = Label(self.header_frame,text="Points",bg=header_color,fg="white")
        self.point_label.pack(side="right")

        self.points_display_label = Label(self.header_frame, textvariable=self.points_var, bg=header_color, fg="white")
        self.points_display_label.pack(side="right")  # Align the label to the right side

        #Calendar button
        self.calender_button = Button(self.header_frame, text="Calendar" ,background="white",fg="black",command=self.show_calendar_top)
        self.calender_button.pack(side="left")
        

        # Body Frame
        self.body_frame = Frame(root, background=body_color, height=window_height // 2)
        self.body_frame.grid(row=1, column=0, sticky="nsew")

        self.my_entry = Entry(self.body_frame, font=("Helvetica", 20))
        self.my_entry.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
        

        self.my_list = Listbox(self.body_frame, font=self.my_font, bd=0, fg="#000000", highlightthickness=0,background=body_color, activestyle="none")
        self.my_list.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)  # Set columnspan to make it span two columns

        # Buttons
        self.add_button = Button(self.body_frame, text="Add Task", command=self.add_item,background=header_color,fg=button_text_color)
        self.add_button.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)


        self.delete_button = Button(self.body_frame, text="❌", command=self.delete_item,background=button_color,fg=button_text_color)
        self.delete_button.grid(row=2, column=2, sticky="nsew", pady=10, padx=10)

        self.complete_button = Button(self.body_frame, text="Complete", command=self.complete_item,background=button_color,fg=button_text_color)
        self.complete_button.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)  

        self.speech_button = Button(self.body_frame, text="Speech", command=self.speech_to_text,background=button_color,fg=button_text_color)
        self.speech_button.grid(row=2, column=1, sticky="nsew", pady=10, padx=10)

        # Make columns and rows expandable
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.body_frame.grid_columnconfigure(0, weight=1)  # Make the body_frame column expandable

    def display_tasks(self, tasks, selected_date):
        self.my_list.delete(0, END)
        for task in tasks:
            task_text = task['text']
            completed = '✅' if task['completed'] else ''
            if task['date'] == selected_date:  # Filter tasks for the selected date
                self.my_list.insert(END, f'{completed}{task_text}')

    def delete_item(self):
        pass

    def add_item(self):
        pass

    def complete_item(self):
        pass

    def speech_to_text(self):
        pass

    def show_calendar_top(self):
        pass

