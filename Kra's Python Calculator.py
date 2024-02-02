import tkinter as tk
from tkinter import StringVar

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("error, not possible")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

def on_key_press(event):
    key = event.char
    if key.isdigit() or key in ['+', '-', '*', '/', '.']:
        button_press(key)
    elif event.keysym == 'BackSpace':
        clear()
    elif key == '\r':  # Handles Enter key for equals
        equals()

window = tk.Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

label = tk.Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

frame = tk.Frame(window)
frame.pack()

# Bind keyboard events
window.bind('<Key>', on_key_press)

button0 = tk.Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

button1 = tk.Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = tk.Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = tk.Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = tk.Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = tk.Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = tk.Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = tk.Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = tk.Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = tk.Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

plus = tk.Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = tk.Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = tk.Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = tk.Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = tk.Button(frame, text='=', height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

decimal = tk.Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

# Backspace button
backspace = tk.Button(window, text='←', height=4, width=12, font=35, command=clear)
backspace.pack()

window.mainloop()
