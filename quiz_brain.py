class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.list)


    def next_guess(self):
        current_question = self.list[self.question_number]
        guess = input(f"Q{self.question_number + 1}: {current_question.text}. True or False?").lower()
        self.question_number += 1
        self.check_answer(guess, current_question.answer)

    def check_answer(self, guess, correct_answer):
        if guess.lower() == correct_answer.lower():
            self.score += 1
            print(f"Score: {self.score} Round: {self.question_number}/ {len(self.list)}")
            print("Correct")
            print("\n")

        else:
            self.score += 0
            print(f"Score: {self.score} Round: {self.question_number}/ {len(self.list)}")
            print(f"Wrong, the correct answer is {correct_answer}")
            print("\n")











