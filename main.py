from data import question_data
from question_model import Question
import quiz_brain

questions_bank = []

for quest in question_data:
    questions_bank.append(Question(quest["text"], quest["answer"]))

# for question in questions_bank:
#     print(question)


