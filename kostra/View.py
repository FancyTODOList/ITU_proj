from tkinter import *
from tkinter.font import Font
from tkcalendar import Calendar
from datetime import datetime


class TaskView:
    def __init__(self, root):
        self.root = root
        self.root['bg'] = '#DDBEAA'
        self.root.title('ToDo List!')
        window_width = 600
        window_height = 600

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.resizable(width=False, height=False)

        self.my_font = Font(family="Regular", size=30, weight="bold")

        self.my_frame = Frame(root)
        self.my_frame.pack(pady=10)

        self.my_list = Listbox(self.my_frame, font=self.my_font, width=25, height=5, bg="#DDBEAA", bd=0,
                               fg="#000000", highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
        self.my_list.pack(side=LEFT, fill=BOTH)

        self.my_scrollbar = Scrollbar(self.my_frame)
        self.my_scrollbar.pack(side=RIGHT, fill=BOTH)

        self.my_list.config(yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_list.yview)

        self.my_entry = Entry(root, font=("Helvetica", 24))
        self.my_entry.pack(pady=20)

        self.button_frame = Frame(root, background="#DDBEAA")
        self.button_frame.pack(pady=20)

        self.delete_button = Button(
            self.button_frame, text="Delete Item", command=self.delete_item, background="#469597")
        self.add_button = Button(
            self.button_frame, text="Add Item", command=self.add_item, background="#469597")
        self.complete_button = Button(
            self.button_frame, text="Complete", command=self.complete_item, background="#469597")
        self.calendar_button = Button(
            self.button_frame, text="Calendar", command=self.open_calendar, background="#469597")
        self.translator_button = Button(
            self.button_frame, text="Translate", command=self.translate, background="#469597")
        self.micro_button = Button(
            self.button_frame, text="Micro", command=self.translate, background="#469597")
        self.delete_button.grid(
            row=0, column=2, sticky='ew', pady=10, ipadx=10)
        self.add_button.grid(row=1, column=0, columnspan=4,
                             sticky='ew', pady=10)
        self.complete_button.grid(
            row=0, column=1, sticky='ew', pady=10, ipadx=10)
        self.calendar_button.grid(
            row=0, column=0, sticky='ew', pady=10, ipadx=10)
        self.translator_button.grid(
            row=0, column=3, sticky='ew', pady=10, ipadx=10)
        self.micro_button.grid(
            row=2, column=0, columnspan=4, sticky='ew', pady=10)
        # List of languages
        languages = ['English', 'Spanish', 'French', 'German', 'Italian', 'Russian', 'Chinese', 'Japanese', 'Korean', 'Arabic', 'Hindi', 'Turkish', 'Portuguese', 'Dutch', 'Polish', 'Romanian',
                     'Greek', 'Swedish', 'Czech', 'Danish', 'Finnish', 'Hungarian', 'Norwegian', 'Slovak', 'Ukrainian', 'Bulgarian', 'Croatian', 'Lithuanian', 'Slovenian', 'Estonian', 'Latvian', 'Maltese']

        # Create variables to hold the selected languages
        self.from_language = StringVar(self.root)
        self.to_language = StringVar(self.root)

        # Set default languages
        self.from_language.set('Czech')
        self.to_language.set('English')

        # Create dropdown lists
        from_language_menu = OptionMenu(
            self.root, self.from_language, *languages)
        to_language_menu = OptionMenu(self.root, self.to_language, *languages)

        # Place the dropdown lists
        from_language_menu.place(x=500, y=340)
        to_language_menu.place(x=500, y=380)

        # Bind mouse events for dragging items
        self.my_list.bind("<Button-1>", self.on_start_drag)
        self.my_list.bind("<B1-Motion>", self.on_drag_motion)

        # Initialize variables for storing drag data
        self.drag_start_index = None
        self.dragged_index = None

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

    def open_calendar(self):
        pass

    def translate(self):
        pass

    def micro(self):
        pass
    
    def on_start_drag(self, event):
        # Get the index of the item that was clicked
        self.drag_start_index = self.my_list.nearest(event.y)

    def on_drag_motion(self, event):
        # Get the index of the item that the cursor is over
        current_index = self.my_list.nearest(event.y)

        # Check if the current index is different from the start index
        if current_index != self.drag_start_index:
            # Remove the dragged item
            item = self.my_list.get(self.drag_start_index)
            self.my_list.delete(self.drag_start_index)

            # Insert the item before the current index
            self.my_list.insert(current_index, item)

            # Update the start index for further dragging
            self.drag_start_index = current_index
    
class CalendarView:
    def __init__(self, root, controller, initial_date):
        self.root = root
        self.root.title('Calendar')
        self.controller = controller
        self.root.configure(background='#469597')
        self.root.resizable(width=False, height=False)

        window_width = 450
        window_height = 350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.get_date_button = Button(
            self.root, text="Get date", command=self.get_selected_date,  background="#5BA199")
        self.get_date_button.place(x=180, y=200)
        self.selected_date = Label(self.root, text="Selected date:   ")
        self.selected_date.place(x=150, y=250)

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.cal = Calendar(self.root, selectmode="day",
                            year=initial_date.year, month=initial_date.month, day=initial_date.day)
        self.cal.pack(padx=10, pady=10)

    def get_selected_date(self):
        selected_date_str = self.cal.get_date()
        selected_date = datetime.strptime(selected_date_str, "%m/%d/%y")
        formatted_date = selected_date.strftime("%d. %m. %Y")
        self.selected_date.config(text=f"Selected date: {formatted_date}")
        return formatted_date
