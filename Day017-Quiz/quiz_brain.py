import html

class QuizBrain:
    def __init__(self,questions_list):
        self.questions_list = questions_list
        self.question_number = 0

    def next_question(self):
        c_question = self.questions_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(c_question.q_text)
        return c_question.q_answer == input(f"Q. {self.question_number}: {q_text} (True/ False): ")

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
