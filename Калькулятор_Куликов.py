import tkinter as tk
from tkinter import messagebox
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        messagebox.showinfo('Результат', f'{result}')
    except ValueError:
        messagebox.showerror('Ошибка', 'Введите допустимые числа')
def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        messagebox.showinfo('Результат', f'{result}')
    except ValueError:
        messagebox.showerror('Результат', 'Введите допустимые числа')
def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        messagebox.showinfo('Результат', f'{result}')
    except ValueError:
        messagebox.showerror('Ошибка', 'Введите допустимые числа')
def divide():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror('Ошибка', 'Введите допустимые числа')
            return
        result = float(entry1.get()) / float(entry2.get())
        messagebox.showinfo('Результат', f'{result}')
    except ValueError:
        messagebox.showerror('Ошибка', 'Введите допустимые числа') 
window = tk.Tk()
window.geometry('200x200')
window.title('Калькулятор')
entry1 = tk.Entry(window)
entry1.pack()
entry2 = tk.Entry(window)
entry2.pack()
add_button = tk.Button(window, text='+', command=add)
add_button.pack()
subtract_button = tk.Button(window, text='-', command=subtract)
subtract_button.pack()
multiply_button = tk.Button(window, text='*', command=multiply)
multiply_button.pack()
divide_button = tk.Button(window, text='/', command=divide)
divide_button.pack()

window.mainloop()
