import tkinter as tk

tasks = ["Pet Dog", "Walk Cat", "Feed Squirrel"]
checkboxStatuses = []
class ToDoList:
        #WORK IN PROGRESS
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1920x1080+325+150")
        self.window.title("To Do List")

        self.label = tk.Label(self.window, text="To Do", font=('Arial', 50))
        self.label.pack()

        for i in tasks:
            checkboxStatuses.append(tk.IntVar)
            tk.Checkbutton(self.window, text=i, font=('Arial', 24)).pack(fill=tk.X)

        self.textbox = tk.Text(self.window, height=3, font=('Arial', 24))
        self.textbox.pack()

        self.button = tk.Button(self.window, text="Add New Task", font=('Arial', 18), command=self.add_task)
        self.button.pack()
        self.window.mainloop()

    def add_task(self):
        for status in checkboxStatuses:
            if status == 0:
                self.textbox.get('1.0', tk.END)




ToDoList()
