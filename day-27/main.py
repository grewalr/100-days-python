from tkinter import *

def button_clicked():
    text_input = input.get()
    my_label.config(text=text_input)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button 1
button1 = Button(text="Click Me 1", command=button_clicked)
button1.grid(column=1, row=1)

# Button 2
button2 = Button(text="Click Me 2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
















window.mainloop()