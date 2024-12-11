#project submission for python project
import tkinter as T
from tkinter import messagebox
from math import *
#font for  application wise use
f = ('Times New Roman', 18)

#function for application evaluation
def evaluate_expression(event=None):
    try:
        expression = inbox.get()
        # Convert to radians in case of sin, cos etc
        expression = expression.replace('sin(', 'sin(radians(')
        expression = expression.replace('cos(', 'cos(radians(')
        expression = expression.replace('tan(', 'tan(radians(')
        expression = expression.replace('csc(', '1/sin(radians(')
        expression = expression.replace('sec(', '1/cos(radians(')
        expression = expression.replace('cot(', '1/tan(radians(')
        result = eval(expression, {"__builtins__": None}, {"radians": radians, "sin": sin, "cos": cos, "tan": tan, "log": log, "pow": pow, "sqrt": sqrt})
        inbox.delete(0, T.END)
        inbox.insert(T.END, str(result))
    except Exception as er:
        messagebox.showerror('Error', f'invalid input: {er}')

#clears the input field
def clear_entry(event=None):
    inbox.delete(0,T.END)

#resets the main
core = T.Tk()
core.title('Scientific Calculator by (SSGS) made with python')

#Input space for calculator
inbox = T.Entry(core, width = 36, font= f, fg= 'White', bg= 'Black', bd= 10, insertwidth= 5, borderwidth= 5)
inbox.grid(row= 0, column= 0, columnspan= 5)

#keyboard layout
keypad = [
    '7', '8', '9', '/', 'Clr',
    '4', '5', '6', '*', 'sqrt',
    '1', '2', '3', '-', 'pow',
    '0', '.', '+', '=', 'log',
    '(', '))',')',',','sin',
    'cos','tan', 'csc', 'sec', 'cot'
]

row = 1
col = 0
for key in keypad:
    if key == 'Clr':
        T.Button(core, text= key, padx= 20, pady= 20, font= f, command= clear_entry).grid(row= row, column= col)
    elif key == '=':
        T.Button(core, text= key, padx= 20, pady= 20, font= f, command= evaluate_expression).grid(row= row, column= col)
    else:
        T.Button(core, text= key, padx= 20, pady= 20, font= f,
                  command= lambda key = key: inbox.insert(T.END, key)).grid(row= row, column= col)
    col +=1
    if col > 4:
        col = 0
        row += 1

#setting enter on keyboard as command to evaluate in calculator after input
inbox.bind('<Return>',evaluate_expression)

#Scientific Calculator loop
core.mainloop()
