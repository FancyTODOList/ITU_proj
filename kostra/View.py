from tkinter import *
from tkinter.font import Font
from tkcalendar import Calendar
from datetime import datetime


class TaskView:
    def __init__(self, root, model):
        self.root = root
        self.model = model
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

        self.my_font = Font(family="Regular", size=20, weight="bold")

        self.my_frame = Frame(root)
        self.my_frame.pack(pady=10)

        self.my_list = Listbox(self.my_frame, font=self.my_font, width=35, height=7, bg="#DDBEAA", bd=0,
                               fg="#000000", highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
        self.my_list.pack(side=LEFT, fill=BOTH)

        self.my_scrollbar = Scrollbar(self.my_frame)
        self.my_scrollbar.pack(side=RIGHT, fill=BOTH)

        self.my_list.config(yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_list.yview)

        self.my_entry = Entry(root, font=("Helvetica", 20))
        self.my_entry.pack(pady=20)

        self.button_frame = Frame(root, background="#DDBEAA")
        self.button_frame.pack(pady=20)

        self.delete_button = Button(
            self.button_frame, text="Delete Task", command=self.delete_item, background="#469597")
        self.add_button = Button(
            self.button_frame, text="Add Task", command=self.add_item, background="#469597")
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
        self.short_languages = ['English', 'Polish',
                                'Czech', 'Slovak', 'Ukrainian', 'Bulgarian']
        self.long_languages = ['English', 'Spanish', 'French', 'German', 'Italian', 'Chinese',
                               'Japanese', 'Korean', 'Arabic', 'Hindi', 'Turkish', 'Portuguese',
                               'Dutch', 'Polish', 'Romanian', 'Greek', 'Swedish', 'Czech', 'Danish',
                               'Finnish', 'Hungarian', 'Norwegian', 'Slovak', 'Ukrainian', 'Bulgarian',
                               'Croatian', 'Lithuanian', 'Slovenian', 'Estonian', 'Latvian', 'Maltese',
                               'Afrikaans', 'Albanian', 'Amharic', 'Armenian', 'Azerbaijani', 'Basque',
                               'Belarusian', 'Bengali', 'Bosnian', 'Catalan', 'Cebuano', 'Chichewa',
                               'Corsican', 'Filipino', 'Frisian', 'Galician', 'Georgian', 'Gujarati',
                               'Haitian Creole', 'Hausa', 'Hawaiian', 'Hmong', 'Icelandic', 'Igbo',
                               'Indonesian', 'Irish', 'Javanese', 'Kannada', 'Kazakh', 'Khmer',
                               'Kurdish', 'Kyrgyz', 'Lao', 'Latin',
                               'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maori', 'Marathi',
                               'Mongolian', 'Myanmar', 'Nepali', 'Pashto', 'Persian',
                               'Punjabi', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona',
                               'Sindhi', 'Sinhala', 'Somali', 'Spanish', 'Sundanese', 'Swahili',
                               'Tajik', 'Tamil', 'Telugu', 'Thai', 'Uzbek', 'Vietnamese', 'Welsh',
                               'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']

        # Create variables to hold the selected languages
        self.from_language = StringVar(self.root)
        self.to_language = StringVar(self.root)

        # Set default languages
        self.from_language.set('Czech')
        self.to_language.set('English')

        # Create dropdown lists
        self.from_language_menu = OptionMenu(
            self.root, self.from_language, *self.short_languages)
        self.to_language_menu = OptionMenu(
            self.root, self.to_language, *self.short_languages)

        # Place the dropdown lists
        self.from_language_menu.place(x=500, y=340)
        self.from_language_menu.config(bg="#469597", highlightthickness=0)  
        self.to_language_menu.place(x=500, y=380)
        self.to_language_menu.config(bg="#469597", highlightthickness=0)
        # Create a variable to hold the state of the checkmark
        self.long_languages_var = BooleanVar()

        # Associate the variable with the checkmark
        self.long_languages_checkmark = Checkbutton(
            self.root, text="I'm polyglot", variable=self.long_languages_var, command=self.update_language_list, background="#DDBEAA", highlightthickness=0)
        self.long_languages_checkmark.place(x=500, y=420)
        
        # Create a label to display the time
        self.time_label = Label(root, text="", font=("Helvetica", 24))
        self.time_label.pack(pady=20)

        # Update the time label every second
        self.update_time_label()

    def update_time_label(self):
        # Get the current time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Update the time label
        self.time_label.config(text=f"{current_time}", background="#DDBEAA", foreground="#469597")

        # Call this method again after 1000 milliseconds
        self.root.after(1000, self.update_time_label)
            
    def update_language_list(self):
        # Check if the checkmark is checked
        if self.long_languages_var.get():
            # If it's checked, use the long language list
            languages = self.long_languages
        else:
            # If it's unchecked, use the short language list
            languages = self.short_languages

        # Update the dropdown lists
        self.from_language_menu['menu'].delete(0, 'end')
        self.to_language_menu['menu'].delete(0, 'end')
        for language in languages:
            self.from_language_menu['menu'].add_command(
                label=language, command=lambda l=language: self.from_language.set(l))
            self.to_language_menu['menu'].add_command(
                label=language, command=lambda l=language: self.to_language.set(l))

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

    def open_calendar(self):
        pass

    def translate(self):
        pass

    def micro(self):
        pass


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

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.cal = Calendar(self.root, selectmode="day",
                            year=initial_date.year, month=initial_date.month, day=initial_date.day)
        self.cal.pack(padx=10, pady=10)

    def get_selected_date(self):
        selected_date_str = self.cal.get_date()
        selected_date = datetime.strptime(selected_date_str, "%m/%d/%y")
        formatted_date = selected_date.strftime("%d. %m. %Y")
        return formatted_date
