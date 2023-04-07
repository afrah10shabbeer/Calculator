import math
import tkinter as tk


def is_operator(symbol):
    if symbol == "+" or symbol == "-" or symbol == "x" or symbol == "/":
        return True
    return False


# Clearing entry field and inserting result by setting associated StringVal to empty string
def clear_and_display(result):
    input_text.set("")
    input_entry.insert(0, result)


# Function to check if a string represents a floating number or not
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def button_clicked(button_symbol):

    # Getting the entire text from the entry field
    expression = input_text.get()
    if button_symbol == "=":

        # Extracting operands from the expression
        for i in range(0, len(expression)):
            if is_operator(expression[i]):
                operator = expression[i]

                operand_1 = float(expression[0:i])
                operand_2 = float(expression[i+1:])
                break

        if operator == "+":
            result = operand_1 + operand_2
        elif operator == "-":
            result = operand_1 - operand_2
        elif operator == "x":
            result = operand_1 * operand_2
        elif operator == "/":
            if operand_2 == 0:
                result = "Cannot divide by 0"
            else:
                result = operand_1 / operand_2
        elif operator == "!":
            result = math.factorial(operand_1)

        # Clearing the entry field and displaying result
        clear_and_display(result)

    elif button_symbol == "Clear":

        # Clearing the entire entry filed by setting its associated StringVar object to empty string
        input_text.set("")

    elif button_symbol == "Back":

        # Copying entire expression except the last character
        new_text = expression[:-1]
        print(new_text)
        input_text.set("") # Clearing the entire entry field
        input_entry.insert(0,new_text) # Displaying the new text on entry field

    # Unary Reciprocal operation
    elif button_symbol == "1/ X":

        # Entire operand must be numeric

        if expression.isdigit() or is_float(expression):
            value_operand = float(expression)
            result = 1 / value_operand
            clear_and_display(result)

    # Unary Factorial operation
    elif button_symbol == "X !":

        # Entire operand must be numeric
        if expression.isdigit():
            integer_operand = int(expression)
            result = math.factorial(integer_operand)
            clear_and_display(result)

    elif button_symbol == ".":

        # Last char should not be a symbol, "35." is valid but "3+." is not valid
        if not is_operator(expression[-1]):
            input_entry.insert(tk.END, ".")

    else:

        # Display this operator on entry field only when no other operator was clicked '8-/' this is invalid!
        if is_operator(button_symbol):

            # Edge case, Check if entry field is empty?
            if len(expression) == 0:
                return
            last_character = expression[-1]
            if is_operator(last_character): # If already an operator was used, don't insert another operator
                return

        # Inserting button_symbol at the END of the entry field
        input_entry.insert(tk.END, button_symbol)


if __name__ == "__main__":

    # Creating a main window of the application
    window = tk.Tk()

    # Setting the maximum and minimum size of the window to make it fixed-size
    window.minsize(500, 450)
    window.maxsize(500, 450)

    # Giving title to the main window
    window.title("Calculator")

    # Applying padding to the entire window
    window.configure(padx=30, pady=10, bg="#000000")

    # Create a StringVar object to store the input text
    input_text = tk.StringVar()

    # Create an Entry widget
    input_entry = tk.Entry(window, textvariable=input_text, font=('Helvetica', 30), width=19)

    # Create a new frame widget to hold all the buttons
    button_frame = tk.Frame(window, padx=15, pady=15)

    button_labels = ["7", "8", "9", "Clear",
                     "4", "5", "6", "+",
                     "1", "2", "3", "-",
                     "0", ".", "Back", "x",
                     "1/ X", "X !", "=", "/"]

    # Create a loop to create the buttons
    for i in range(len(button_labels)):
        # Calculate the row and col of the button
        row = (i // 4) + 1  # Move the buttons to the row below the input_entry widge
        col = i % 4

        # Set button color
        if is_operator(button_labels[i]):
            button_color = "#004de6"
            font_color = "#ffffff"

        elif button_labels[i] == "Clear":
            button_color = "#ffffb3"

        elif button_labels[i] == "=":
            button_color = "#ff3333"
            font_color = "#000000"

        else:
            button_color = "#e7e4e4"
            font_color = "#000000"

        # Add a button
        button = tk.Button(window, text=button_labels[i], command=lambda x=button_labels[i]: button_clicked(x),width=12,height=3,
                           bg=button_color, fg=font_color)

        button.grid(row=row, column=col, pady=7)

    # Add the input entry widget and the button frame widget to the main window
    input_entry.grid(row=0, columnspan=4, padx=10, pady=10)
    button_frame.grid(columnspan=4)

    # Start the main event loop
    window.mainloop()


