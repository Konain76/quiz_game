from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for x in range(0, len(question_data)):
    question_text = question_data[x]["text"]
    question_answer = question_data[x]["answer"]
    n_question = Question(question_text, question_answer)
    question_bank.append(n_question)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you've completed the quiz")
print(f" your final score is {quiz.score}/{quiz.question_number}")
