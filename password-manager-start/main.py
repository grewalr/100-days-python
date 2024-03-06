from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def genearate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)] + [choice(numbers) for _ in range(nr_numbers)] + [choice(symbols) for _ in range(nr_symbols)]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # get the entries
    web_out = website_entry.get()
    email_out = email_user_entry.get()
    password_out = password_entry.get()

    empty_fields_info = "Please don't leave any fields empty!"
    entered_details_info = f"These are the details entered: \nEmail: {email_out} \nPassword: {password_out} \nIs it ok to save?"

    if len(web_out) == 0 or len(password_out) == 0:
        messagebox.showinfo(title="Oops", message=empty_fields_info)
    else:
        is_ok = messagebox.askokcancel(title=web_out, message=entered_details_info)

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{web_out} | {email_out} | {password_out}\n")
                reset()


def reset():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.eval('tk::PlaceWindow . center')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)


# Email/User label
email_user = Label(text="Email/Username:")
email_user.grid(column=0, row=2)


# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Website entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


# Email/User entry
email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "rik@mcgrewal.com")


# Password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


# Gen password button
generate_pass_button = Button(text="Generate Password", command=genearate_password)
generate_pass_button.grid(column=2, row=3)

# Add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
