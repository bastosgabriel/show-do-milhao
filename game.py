from view import View
from question import Question

class Game():
    
    @staticmethod
    def run():
        _round = 1
        while True:
            current_question = Game.generate_question(_round)

            View.draw_question(_round, current_question)

            # VALIDAR ESTA ENTRADA
            user_answer = int(input())

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
    def generate_question(_round):
        return Question("Quantas letras tem em 'Brasil'?", ["5", "6", "7", "9"], "6")

    '''
    Returns True if the answer is right and False otherwise
    '''
    def check_answer(current_question, user_answer):

        selected_answer = current_question.answers[user_answer - 1]

        print(current_question.right_answer)
        print(selected_answer)

        if current_question.right_answer == selected_answer:
            return True
        else:
            return False
        

    