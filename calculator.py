import tkinter as tk

def on_button_click(value):
    current_text = entry.get()
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "DEL":
        entry.delete(len(current_text) - 1)
    elif value == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("DEL", 5, 0), ("=", 5, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col)

root.mainloop()

