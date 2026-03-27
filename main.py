#User Interface for the calculator
import tkinter

#Button values used in calculator
button_values = [
    ['AC', '+/-', '%', '÷'],
    ['7', '8', '9', 'x'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '√', '=']
]

right_symbols = ['÷', 'x', '-', '+', '=']
top_symbols = ['AC', '+/-', '%']

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

#Colors for the calculator
color_light_gray = '#D4D4D2'
color_black = '#1C1C1C'
color_dark_gray = '#505050'
color_orange = '#FF9500'
color_white = 'white'

window = tkinter.Tk()
window.title('Calculator')
window.resizable(False, False)
window.mainloop()