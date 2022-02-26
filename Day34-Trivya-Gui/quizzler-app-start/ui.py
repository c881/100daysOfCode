import tkinter as tk

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        self.canvas = tk.Canvas(width=250, height=350)
        self.score_label = tk.Label(text="Score:0", fg="white")
        self.score_label.grid(row=0, column=1)
        # qustion_text = self.canvas.create_text(150, 150, text="Question Goes HERE", width=150,
        #                                   font=("Arial", 20, "bold"), fill=THEME_COLOR)
        # self.canvas.grid(row=1, column=0)
        self.true_image = tk.PhotoImage("images/true.png")
        self.false_image = tk.PhotoImage("images/false.png")
        self.true_button = tk.Button(image=self.true_image, highlightthickness=0)  # , command=true)
        self.true_button.grid(row=2, column=0)
        self.false_button = tk.Button(image=self.false_image, highlightthickness=0)  # , command=false)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()


def main():
    qi = QuizInterface()

if __name__ == "main":
    main()