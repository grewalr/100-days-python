from tkinter import *
import pandas
import random
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
FRENCH = "French"
ENGLISH = "English"

# ---------- Main ---------- #
lang_df = None
try:
    lang_df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    lang_df = pandas.read_csv("./data/french_words.csv")
finally:
    lang_dict = lang_df.to_dict()
    lang_dict_a = lang_df.to_dict(orient="records")

current_card = {}


def generate_random_word():
    rand = random.choice(list(lang_dict[FRENCH].items()))
    french_word = lang_dict[FRENCH][rand[0]]
    canvas.itemconfig(word_text, text=french_word)


def generate_random_word_a():
    global current_card
    current_card = random.choice(lang_dict_a)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language_text, text=FRENCH, fill="black")
    canvas.itemconfig(word_text, text=current_card[FRENCH], fill="black")


def count_down(count):
    global current_card
    count -= 1

    if count > 0:
        window.after(1000, count_down, count)
    else:
        canvas.itemconfig(canvas_image, image=card_back_img)
        canvas.itemconfig(language_text, text=ENGLISH, fill="white")
        canvas.itemconfig(word_text, text=current_card[ENGLISH], fill="white")


def start_timer():
    generate_random_word_a()
    secs_remaining = 3
    count_down(secs_remaining)


def is_word_known():
    """ Remove word from the dictionary"""
    lang_dict_a.remove(current_card)
    print(len(lang_dict_a))
    start_timer()


def is_word_unknown():
    fr = current_card[FRENCH]
    en = current_card[ENGLISH]
    file_path = "./data/words_to_learn.csv"

    new_data = {
        fr: en
    }

    try:
        with open(file_path, "r") as data_file:
            # Reading old data
            data = json.load(data_file)

            # Updating old data with new data
            data.update(new_data)
    except FileNotFoundError:
        with open(file_path, "w") as data_file:
            # Saving updated data
            json.dump(new_data, data_file, indent=4)
    else:
        with open(file_path, "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)

    start_timer()

# ----------- UI ----------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")

canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_text = canvas.create_text(400, 150, text="", font=FONT_LANGUAGE, fill="black")
word_text = canvas.create_text(400, 263, text="", font=FONT_WORD, fill="black")
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=is_word_unknown)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_img, highlightthickness=0, command=is_word_known)
right_button.grid(column=1, row=1)

start_timer()

window.mainloop()
