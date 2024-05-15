from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
score = 0


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Test")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {score}", highlightthickness=0, padx=20, pady=20, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Test",
                                                     fill="black",
                                                     font=("Arial", 20, "italic"),
                                                     width=280
                                                     )

        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, padx=200, pady=200,
                               command=self.true_button_pressed)
        self.true_btn.grid(row=2, column=0, padx=20, pady=20)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, padx=200, pady=200,
                                command=self.false_button_pressed)
        self.false_btn.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game!")
            self.false_btn.config(state="disabled")
            self.true_btn.config(state="disabled")

    def true_button_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg="Green")
        elif is_right is False:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)

    def no_response_from_button(self):
        pass
