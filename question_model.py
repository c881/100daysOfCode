class Question:
    def __init__(self, q_text, q_answer):
        self.q_text = q_text
        self.q_answer = q_answer

    def __str__(self):
        return "text = " + self.q_text + " ,answer = " + self.q_answer