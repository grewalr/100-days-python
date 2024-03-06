from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

def button_clicked():
    km = entry.get()
    miles = int(km) * 1.6
    conversion_label.config(text=str(miles))


# Text Label
text_label = Label(text="is equal to", font=("Arial", 16, "bold"))
text_label.grid(column=0, row=1)

# Conversion Label
conversion_label = Label(text="0")
conversion_label.grid(column=1, row=1)

# Entry
entry = Entry(width=7)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# Label 'Miles'
miles_label = Label(text="Miles", font=("Arial", 16, "bold"))
miles_label.grid(column=2, row=0)

# Label 'Km'
km_label = Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
