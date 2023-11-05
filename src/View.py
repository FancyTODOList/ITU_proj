from tkinter import *
from tkinter.font import Font
from tkcalendar import Calendar
import datetime
class TaskView:
    def __init__(self, root):
        self.root = root
        self.root['bg'] = '#DDBEAA'
        self.root.title('ToDo List!')
        self.root.geometry("500x500")
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

        self.button_frame = Frame(root)
        self.button_frame.pack(pady=20)

        self.delete_button = Button(self.button_frame, text="Delete Item", command=self.delete_item)
        self.add_button = Button(self.button_frame, text="Add Item", command=self.add_item)
        self.complete_button = Button(self.button_frame, text="Complete", command=self.complete_item)
        self.calendar_button = Button(self.button_frame, text="Calendar", command=self.open_calendar)
        self.translator_button = Button(self.button_frame, text="Translator", command=self.open_translator)
        self.delete_button.grid(row=0, column=2, sticky='ew', pady=10, ipadx=10)
        self.add_button.grid(row=1, column=0, columnspan=4, sticky='ew', pady=10)
        self.complete_button.grid(row=0, column=1, sticky='ew', pady=10, ipadx=10)
        self.calendar_button.grid(row=0, column=0, sticky='ew', pady=10, ipadx=10)
        self.translator_button.grid(row=0, column=3, sticky='ew', pady=10, ipadx=10)

    def delete_item(self):
        pass

    def add_item(self):
        pass

    def complete_item(self):
        pass

    def open_calendar(self):
        pass

    def open_translator(self):
        pass

class TranslatorView:
    def __init__(self, root):
        self.root = root
        self.root.title('Translator')
        self.root.configure(background='white')
        self.root.resizable(width=True, height=True)

        input = Text(self.root, width=30, height=5, background="#DDBEAA")
        input.place(x=150, y=50)

        output = Text(self.root, width=30, height=5, background="#DDBEAA")
        output.place(x=150, y=150)

        translate_button = Button(self.root, text="Translate",
                                  command=lambda: self.translate(input, output), background="#5BA199")
        translate_button.place(x=50, y=250)

        window_width = 450
        window_height = 350

        x = (self.root.winfo_reqwidth() - window_width) // 2 + self.root.winfo_x()
        y = (self.root.winfo_reqheight() - window_height) // 2 + self.root.winfo_y()

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    def translate(self, input, output):
        pass

class CalendarView:
    def __init__(self, root):
        self.root = root
        self.root.title('Calendar')
        self.root.configure(background='#469597')
        self.root.resizable(width=False, height=False)

        window_width = 250
        window_height = 200

        x = (self.root.winfo_reqwidth() - window_width) // 2 + self.root.winfo_x()
        y = (self.root.winfo_reqheight() - window_height) // 2 + self.root.winfo_y()

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        today = datetime.date.today()
        cal = Calendar(self.root, selectmode="day",
                       year=today.year, month=today.month, day=today.day, bg="lightblue")
        cal.pack(padx=10, pady=10)
