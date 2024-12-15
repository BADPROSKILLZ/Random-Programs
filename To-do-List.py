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

        self.textbox = tk.Text(self.window, height=3, font=('Arial', 24))
        self.textbox.pack()

        self.button = tk.Button(self.window, text="Add New Task", font=('Arial', 18), command=self.addTask)
        self.button.pack()

        while True:
            self.printTasks()
            self.window.mainloop()

    def addTask(self):
        print(self.textbox.get('1.0', tk.END))
        if self.textbox.get('1.0', tk.END) not in tasks:
            tasks.append(self.textbox.get('1.0', tk.END))
            self.printTasks([self.textbox.get('1.0', tk.END)])

    def printTasks(self, taskList = tasks):
        for i in taskList:
            self.status = tk.IntVar()
            checkboxStatuses.append(self.status)
            tk.Checkbutton(self.window, text=i, font=('Arial', 24), variable=self.status).pack(side='left')
            


ToDoList()
