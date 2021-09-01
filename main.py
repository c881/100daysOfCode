from data import question_data
from question_model import Question
import quiz_brain

questions_bank = []

for quest in question_data:
    # new_q = Question(question_data[idx]["text"], question_data[idx]["answer"])
    questions_bank.append(Question(quest["text"], quest["answer"]))

for _ in questions_bank:
    print(_)


