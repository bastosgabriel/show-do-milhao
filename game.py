from view import View
from question import Question
import random

class Game():
    
    @staticmethod
    def run():
        _round = 1
        already_asked_questions = []

        while True:
            current_question = Game.generate_question(_round, already_asked_questions)
            already_asked_questions.append(current_question.text)

            View.draw_question(_round, current_question)

            while True:
                try:
                    user_answer = int(input())

                    if user_answer > 4 or user_answer < 1:
                        View.draw_question(_round, current_question)
                        continue

                except ValueError:
                    View.draw_question(_round, current_question)
                    continue
                
                else:
                    break

            # If answer is correct
            if Game.check_answer(current_question, user_answer):
                View.draw_question_end("acertou")
                input()
                _round += 1
                if _round == 17:
                    win_or_loose = 1
                    break
            else:
                View.draw_question_end("errou")
                input()
                win_or_loose = -1
                break

        return win_or_loose

    '''
    Returns the Question object with the current question
    '''
    def generate_question(_round, already_asked_questions):

        file_questions = open("perguntas_ativas.txt","r")
        file_answers = open("respostas_ativas.txt","r")

        if 0 < _round < 6:
            questions_range = [0, 9]
        elif 5 < _round < 11:
            questions_range = [10, 19]
        elif 10 < _round < 17:
            questions_range = [20, 29]

        question_lines = file_questions.readlines()
        answer_lines = file_answers.readlines()

        file_questions.close()
        file_answers.close()

        # Generates a new question if that question was already asked
        while True:
            question_drawn = random.randint(questions_range[0], questions_range[1])

            if question_lines[question_drawn] in already_asked_questions:
                continue
            else:
                break

        return Question(question_lines[question_drawn],
                        [answer_lines[(question_drawn + 1) * 4 - 4], 
                         answer_lines[(question_drawn + 1) * 4 - 3], 
                         answer_lines[(question_drawn + 1) * 4 - 2], 
                         answer_lines[(question_drawn + 1) * 4 - 1]],
                         answer_lines[(question_drawn + 1) * 4 - 4])

    '''
    Returns True if the answer is right and False otherwise
    '''
    def check_answer(current_question, user_answer):

        selected_answer = current_question.answers[user_answer - 1]

        if current_question.right_answer == selected_answer:
            return True
        else:
            return False
        

    