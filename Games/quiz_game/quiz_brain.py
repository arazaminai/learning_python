class QuizBrain: 

    def __init__(self, q_list):
        """Brain of the game"""
        self.q_number = 0
        self.q_list = q_list
        self.score = 0
    
    def still_has_question(self):
        """Checks if there's still questions in the list"""
        if self.q_number == len(self.q_list):
            print("You Have completed the Quiz")
            print(f"Your final score is {self.score}/{self.q_number}")
            return False
        return True
    
    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")

        print(f"The correct answer is {correct_answer}")
        print(f"You score is {self.score}/{self.q_number}\n")
