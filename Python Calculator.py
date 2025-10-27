import tkinter as tk
from tkinter import StringVar
def button_press(value): global equation_text; equation_text += value; equation_label.set(equation_text)
def equals(): global equation_text; equation_text = str(eval(equation_text)) if equation_text else reset_equation("Error"); equation_label.set(equation_text)
def clear(): reset_equation("")
def reset_equation(value): global equation_text; equation_text = value; equation_label.set(value)
def on_key_press(event): actions = {"Return": equals, "BackSpace": clear}; actions.get(event.keysym, lambda: button_press(event.char) if event.char in "0123456789+-*/." else None)()
window = tk.Tk(); window.title("Calculator"); window.geometry("300x400")
equation_text, equation_label = "", StringVar()
tk.Label(window, textvariable=equation_label, font=("consolas", 20), bg="white", width=20, height=2, anchor="e").pack(pady=10)
frame = tk.Frame(window); frame.pack(pady=10)
window.bind("<Key>", on_key_press)
for text, row, col in [("1", 0, 0), ("2", 0, 1), ("3", 0, 2), ("+", 0, 3), ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3), ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3), ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("/", 3, 3)]:
    tk.Button(frame, text=text, height=2, width=5, font=("consolas", 15), command=(equals if text == "=" else lambda t=text: button_press(t))).grid(row=row, column=col, padx=5, pady=5)
tk.Button(window, text="Clear", height=2, width=10, font=("consolas", 15), command=clear).pack(pady=10)
window.mainloop()

