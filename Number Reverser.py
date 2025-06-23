import tkinter as tk
from tkinter import messagebox

def reverse_number():
    num = entry.get()
    if not num.lstrip('-').isdigit():
        messagebox.showerror("Invalid Input", "Enter a valid integer.")
        return
    reversed_num = str(int(num[::-1])) if not num.startswith('-') else '-' + str(int(num[:0:-1]))
    result_label.config(text=f"Reversed: {reversed_num}", fg="navy")
    root.after(3000, reset)

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Number Reverser")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Enter a number:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack()
entry.bind("<Return>", lambda e: reverse_number())

tk.Button(root, text="Reverse", font=("Arial", 12), command=reverse_number).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

entry.focus()
root.mainloop()
