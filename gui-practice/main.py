import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title = "Widgets Demo"
root.geometry("350x100")

label = tk.Label(root, text="Hello", font="Helvetica")
label.pack(expand=True)

def on_click():
    label.config(text="Button clicked!")

button = tk.Button(
    root,
    text="Click Me",
    command=on_click,
)
button.pack(padx=5, pady=5)

def show_state():
    checked = "Checked" if var.get() else "Unchecked"
    checkbox.config(text=f"Check me! ({checked})")

def selection_changed(event):
    label.config(text=f"{event.widget.get()} selected!")

combobox = ttk.Combobox(root, values=["One", "Two", "Three"])
combobox.set("One")
combobox.bind("<<ComboboxSelected>>", selection_changed)
combobox.pack(padx=5, pady=5, fill="x")

# A helper label to show the selected value
label = tk.Label(root, text="One selected!")
label.pack(padx=5, pady=5, fill="x")

var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Check me! (Checked)", variable=var)
checkbox.select()
checkbox.config(command=show_state)
checkbox.pack(padx=5, pady=10)

root.mainloop()