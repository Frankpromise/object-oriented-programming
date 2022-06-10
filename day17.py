# inside the main py, import the question model
# Second step: We will create a question bank for question objects

# 1. Write a for loop to iterate over the question_data
# 2. Create a question object from each entry in question_data
# 3. Append each question object to the question_bank

from question_model import Question
from data_question import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)
# Create new quiz brain

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f'You have completed the quiz')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')

# print(question_bank[0])


