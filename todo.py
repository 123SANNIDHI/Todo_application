from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry("650x450+300+150")

        self.label = Label(self.root, text='To-Do-List', font=('ariel', 25, 'bold'), width=10, bd=5, bg="light blue", fg="black")
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', font=('ariel', 18, 'bold'), width=10, bd=3, bg="light blue", fg="black")
        self.label2.place(x=40, y=90)

        self.label3 = Label(self.root, text='Tasks', font=('ariel', 18, 'bold'), width=10, bd=4, bg="light blue", fg="black")
        self.label3.place(x=370, y=90)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font=('ariel', 18, 'bold'))
        self.main_text.place(x=300, y=150)

        self.text = Text(self.root, height=2, bd=5, width=15, font=('ariel', 18, 'bold'))
        self.text.place(x=20, y=140)

        self.status = Label(self.root, text="Tasks: 0", font=('ariel', 14, 'bold'), bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

        def update_status():
            task_count = self.main_text.size()
            self.status.config(text=f"Tasks: {task_count}")

        def add():
            content = self.text.get(1.0, END).strip()
            if content:
                self.main_text.insert(END, content)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0, END)
                update_status()

        def delete():
            delete_ = self.main_text.curselection()
            if delete_:
                look = self.main_text.get(delete_)
                with open('data.txt', 'r+') as f:
                    new_f = f.readlines()
                    f.seek(0)
                    for line in new_f:
                        if look != line.strip():
                            f.write(line)
                    f.truncate()
                self.main_text.delete(delete_)
                update_status()

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for line in read:
                self.main_text.insert(END, line.strip())
            update_status()

        self.button = Button(self.root, text="Add", font='sarif,20,bold,italic', width=20, bd=10, bg='sky blue', fg='black', command=add)
        self.button.place(x=30, y=230)

        self.button2 = Button(self.root, text="Delete", font='sarif,20,bold,italic', width=20, bd=10, bg='sky blue', fg='black', command=delete)
        self.button2.place(x=30, y=300)

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
