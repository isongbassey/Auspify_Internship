import tkinter

 

# Create main window
window = tkinter.Tk()
window.title("Calculator")

 

# Calculator display
display = tkinter.Entry(window)
display.grid(row=0, column=0, columnspan=4)

 

# Global variables
first_number = 0
math_operation = ""

 

# Function for number buttons
def button_click(number):
    display.insert(tkinter.END, number)

 

# Addition function
def add():
    global first_number
    global math_operation

 

    math_operation = "addition"

 

    first_number = display.get()
    display.delete(0, tkinter.END)

 

# Subtraction function
def subtract():
    global first_number
    global math_operation

 

    math_operation = "subtraction"

 

    first_number = display.get()
    display.delete(0, tkinter.END)

def multiply():
    global first_number
    global math_operation

 

    math_operation = "multiplication"

 

    first_number = display.get()
    display.delete(0, tkinter.END)

def divide():
    global first_number
    global math_operation

 

    math_operation = "division"

 

    first_number = display.get()
    display.delete(0, tkinter.END)

 

# Equal function
def equal():
    second_number = display.get()

 

    if math_operation == "addition":
        result = int(first_number) + int(second_number)

 

        display.delete(0, tkinter.END)
        display.insert(0, result)

 

    if math_operation == "subtraction":
        result = int(first_number) - int(second_number)

 

        display.delete(0, tkinter.END)
        display.insert(0, result)

    if math_operation == "multiplication":
        result = int(first_number) * int(second_number)

 

        display.delete(0, tkinter.END)
        display.insert(0, result)

    if math_operation == "division":
        try:
            result = int(first_number) / int(second_number)

            display.delete(0, tkinter.END)
            display.insert(0, result)

        except ZeroDivisionError:
            display.delete(0, tkinter.END)
            display.insert(0, "Error")

def clear():
    display.delete(0, tkinter.END)

 

# Number buttons
button_1 = tkinter.Button(window, text="1",
                          command=lambda: button_click("1"))

 

button_2 = tkinter.Button(window, text="2",
                          command=lambda: button_click("2"))

 

button_3 = tkinter.Button(window, text="3",
                          command=lambda: button_click("3"))

 

button_4 = tkinter.Button(window, text="4",
                          command=lambda: button_click("4"))

 

button_5 = tkinter.Button(window, text="5",
                          command=lambda: button_click("5"))

 

button_6 = tkinter.Button(window, text="6",
                          command=lambda: button_click("6"))

 

button_7 = tkinter.Button(window, text="7",
                          command=lambda: button_click("7"))

 

button_8 = tkinter.Button(window, text="8",
                          command=lambda: button_click("8"))

 

button_9 = tkinter.Button(window, text="9",
                          command=lambda: button_click("9"))

 

button_0 = tkinter.Button(window, text="0",
                          command=lambda: button_click("0"))

 

# Operator buttons
button_add = tkinter.Button(window,
                            text="+",
                            command=add)

 

button_subtract = tkinter.Button(window,
                                 text="-",
                                 command=subtract)

 

button_multiply = tkinter.Button(window,
                                 text="*", command=multiply)

 

button_divide = tkinter.Button(window,
                               text="/", command=divide)

 

button_equal = tkinter.Button(window,
                              text="=",
                              command=equal)

button_clear = tkinter.Button(window,
                              text="C",
                              command=clear)

 

# Number button positions
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

 

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

 

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

 

button_0.grid(row=4, column=0)

 

# Operator button positions
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=2)
button_equal.grid(row=4, column=3)
button_clear.grid(row=4, column=1)

 

# Start the application
window.mainloop()
