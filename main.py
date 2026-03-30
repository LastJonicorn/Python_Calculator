#User Interface for the calculator
import tkinter

#Button values used in calculator
button_values = [
    ['AC', '+/-', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '√', '=']
]

right_symbols = ['÷', '×', '-', '+', '=']
top_symbols = ['AC', '+/-', '%']

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

#Colors for the calculator
color_light_gray = '#D4D4D2'
color_black = '#1C1C1C'
color_dark_gray = '#505050'
color_orange = '#FF9500'
color_white = 'white'

#Window setup
window = tkinter.Tk()
window.title('Calculator')
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame,
    text='0',
    font=('Arial',45),
    background=color_black,
    foreground=color_white,
    anchor='e',
)

label.grid(row = 0, column = 0, columnspan=column_count, sticky='we')

def button_clicked(value):
    print(value)

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(
            frame,
            text=value,
            font=('Arial', 30),
            width=column_count-1,
            height=1,
            command=lambda v=value: button_clicked(v)
        )
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)

        button.grid(row=row+1, column=column)

frame.pack()

#Center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

#format '(width)x(height)+(x position)+(y position)'
#window.geometry() can't have spaces between elements
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop() #Window stays open