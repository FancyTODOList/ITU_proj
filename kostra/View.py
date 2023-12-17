"""
View.py

Authors:
    - Václav Zapletal xzaple40
    
This file represents applications GUI
"""
from tkinter import *
from tkinter.font import Font
from tkmacosx import Button
from tkcalendar import Calendar
from datetime import date


class TaskView:
    def __init__(self, root, model):
        """
        @brief Initialization of main GUI components
        """
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

        # Label for Points
        self.point_label = Label(self.header_frame, text="Points: ", bg=header_color, fg="white")
        self.point_label.pack(side="left", anchor="w")

        # Label for number of Points
        self.points_display_label = Label(self.header_frame, textvariable=self.points_var, bg=header_color, fg="white")
        self.points_display_label.pack(side="left", anchor="w")

        self.calendar_top = None
        
        # Calendar button
        self.calender_button = Button(self.header_frame, text="Calendar", background="white", fg="black", command=self.show_calendar_top)
        self.calender_button.pack(side="right", anchor="w")
        # Label for current Date
        self.current_date_label = Label(self.header_frame, text=f"Today: {date.today().strftime('%d.%m.%Y')}", font=("Arial", 16), bg=header_color, fg="white")
        self.current_date_label.pack(side="right", anchor="w", padx=10, pady=5)

        
        # Body Frame
        self.body_frame = Frame(root, background=body_color, height=window_height // 2)
        self.body_frame.grid(row=1, column=0, sticky="nsew")

        # Entry for adding tasks
        self.my_entry = Entry(self.body_frame, font=("Helvetica", 20))
        self.my_entry.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
        
        #List of tasks
        self.my_list = Listbox(self.body_frame, font=self.my_font, bd=0, fg="#000000", highlightthickness=0,background=body_color, activestyle="none")
        self.my_list.grid(row=1, column=0, sticky="nsew", pady=10, padx=10) 

        # Add task button
        self.add_button = Button(self.body_frame, text="Add Task", command=self.add_item,background=header_color,fg=button_text_color)
        self.add_button.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

        # Delete task button
        self.delete_button = Button(self.body_frame, text="❌", command=self.delete_item,background=button_color,fg=button_text_color)
        self.delete_button.grid(row=2, column=2, sticky="nsew", pady=10, padx=10)

        # Complete task button
        self.complete_button = Button(self.body_frame, text="Complete", command=self.complete_item,background=button_color,fg=button_text_color)
        self.complete_button.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)  

        # Speech to text button
        self.speech_button = Button(self.body_frame, text="Speech", command=self.speech_to_text,background=button_color,fg=button_text_color)
        self.speech_button.grid(row=2, column=1, sticky="nsew", pady=10, padx=10)

        # Make columns and rows expandable
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.body_frame.grid_columnconfigure(0, weight=1)  # Make the body_frame column expandable

    def display_tasks(self, tasks):
        self.my_list.delete(0, END)
        for task in tasks:
            task_text = task['text']
            completed = '✅' if task['completed'] else ''
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
        """
        @Brief Function for showing calendar
        """
        if self.calendar_top is not None:
            self.calendar_top.deiconify()
        else:
            self.calendar_top = Toplevel(self.root)
            self.calendar_top.withdraw()  # Hide the calendar top initially
            self.calendar_top.protocol("WM_DELETE_WINDOW", self.hide_calendar_top)  # Handle close event

            calendar_frame = Frame(self.calendar_top, background="#daf2dc", height=300, width=400)
            calendar_frame.pack(fill="both", expand=True)

            # Create a Calendar widget for visually selecting dates
            calendar = Calendar(calendar_frame, selectmode="day", date_pattern="dd.MM.yyyy",showweeknumbers=False)
            calendar.pack(padx=10, pady=10)

            # Add a button to get the selected date
            get_date_button = Button(calendar_frame,text="Get Selected Date", command=lambda: self.get_selected_date(calendar))
            get_date_button.pack(pady=10)

    def hide_calendar_top(self):
        # Hide the calendar top window
        if self.calendar_top is not None:
            self.calendar_top.withdraw()

    def get_selected_date(self, calendar):
        # Retrieve the selected date from the Calendar widget
        selected_date = calendar.get_date()
        formatted_date = date(int(selected_date.split('.')[2]), int(selected_date.split('.')[1]), int(selected_date.split('.')[0]))
        
        # Update the current_date_label with the selected date
        self.current_date_label.config(text=f"Selected Date: {formatted_date.strftime('%d.%m.%Y')}")

        

