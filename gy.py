import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Mobile Calculator")
window.geometry("300x500")  # Mobile-friendly size
window.configure(bg="#f0f0f0")  # Light gray background

# Variable to store the expression
expression = ""

# Function to update the expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Function to clear the expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Create an entry field for the equation
equation = tk.StringVar()
entry = tk.Entry(window, textvariable=equation, font=('arial', 20, 'bold'), 
                 bg="white", bd=10, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons (mobile layout: 4x4 grid + extra row for operations)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'  # Clear button
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        cmd = clear
    elif button == '=':
        cmd = equalpress
    else:
        cmd = lambda x=button: press(x)
    
    btn = ttk.Button(window, text=button, command=cmd, width=10, 
                     style='Custom.TButton')
    btn.grid(row=row_val, column=col_val, padx=2, pady=2)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Customize button style
style = ttk.Style()
style.configure('Custom.TButton', font=('arial', 15, 'bold'), 
                background='#4CAF50', foreground='white')  # Green buttons
style.map('Custom.TButton', 
          background=[('active', '#45a049')])  # Darker green when clicked

# Start the application
window.mainloop()

# Optional: Save the window as an image (requires PIL)
try:
    from PIL import ImageGrab
    window.update()  # Ensure window is rendered
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    x1 = x + window.winfo_width()
    y1 = y + window.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save("calculator_screenshot.png")
    print("Calculator screenshot saved as 'calculator_screenshot.png'")
except:
    print("Could not save screenshot. Install Pillow for this feature.")
