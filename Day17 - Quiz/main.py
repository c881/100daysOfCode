from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions_bank = []

for quest in question_data:
    # new_q = Question(question_data[idx]["text"], question_data[idx]["answer"])
    questions_bank.append(Question(quest["text"], quest["answer"]))

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()

