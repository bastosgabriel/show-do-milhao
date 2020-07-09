import random

class Question():
    
    def __init__(self, text, answers, right_answer):
        self.text = text
        # random.sample() returns a shuffled list
        self.answers = random.sample(answers, len(answers)) 
        self.right_answer = right_answer