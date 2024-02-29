
class QuizBrain:

    def __init__(self, question_list):
        self.number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Corect brodiaga!")
            self.score += 1
        else:
            print("Incorect loshara!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.number}")

    def next_question(self):
        index = self.number
        self.number += 1
        text = self.question_list[index].text
        correct_answer = self.question_list[index].answer
        user_answer = input(f"Q.{self.number}: {text} (True/False)?: ")
        self.check_answer(user_answer, correct_answer)

