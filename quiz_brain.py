# Step 3:
# The next thing is to actually tell the users to answer the questions
# 1. Create a quizbrain class
# 2. Write an init method
# 3. Initialise the question list to an input


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

        # Retrieve the item at the current question_number from the question_list
        # Use the input() function to show the user the question text and ask for the user's answer

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print('You are right!')

        else:
            print(f'That is wrong answer!')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')

    # Now we have to figure out how to keep displaying the questions
