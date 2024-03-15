from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = "#00FF00"
RED = "#FF0000"
WHITE = "#FFFFFF"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.eval('tk::PlaceWindow . center')
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=FONT
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=self.true_image, highlightthickness=0, command=self.is_correct)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=self.false_image, highlightthickness=0, command=self.is_incorrect)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You have reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            

    def is_correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feeback(is_right)

    def is_incorrect(self):
        is_right = self.quiz.check_answer("False")
        self.give_feeback(is_right)

    def give_feeback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)

        self.window.after(1000, func=self.get_next_question)
