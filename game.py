import random
import math
from view import View
from question import Question


class Game():
    '''
    The game class is responsible for all the main methods involving the gameplay and
    attributes of the game
    '''
    def __init__(self):
        self.prizes = {
            '1':  {'Acertar': '1 mil',    'Parar': '0 mil',   'Errar': '0'  },
            '2':  {'Acertar': '2 mil',    'Parar': '1 mil',   'Errar': '500'},
            '3':  {'Acertar': '3 mil',    'Parar': '2 mil',   'Errar': '1'  },
            '4':  {'Acertar': '4 mil',    'Parar': '3 mil',   'Errar': '1.5'},
            '5':  {'Acertar': '5 mil',    'Parar': '4 mil',   'Errar': '2'  },
            '6':  {'Acertar': '10 mil',   'Parar': '5 mil',   'Errar': '2.5'},
            '7':  {'Acertar': '20 mil',   'Parar': '10 mil',  'Errar': '5'  },
            '8':  {'Acertar': '30 mil',   'Parar': '20 mil',  'Errar': '10' },
            '9':  {'Acertar': '40 mil',   'Parar': '30 mil',  'Errar': '15' },
            '10': {'Acertar': '50 mil',   'Parar': '40 mil',  'Errar': '20' },
            '11': {'Acertar': '100 mil',  'Parar': '50 mil',  'Errar': '25' },
            '12': {'Acertar': '200 mil',  'Parar': '100 mil', 'Errar': '50' },
            '13': {'Acertar': '300 mil',  'Parar': '200 mil', 'Errar': '100'},
            '14': {'Acertar': '400 mil',  'Parar': '300 mil', 'Errar': '150'},
            '15': {'Acertar': '500 mil',  'Parar': '400 mil', 'Errar': '200'},
            '16': {'Acertar': '1 MILHÃO', 'Parar': '500 mil', 'Errar': '0'  }
        }

        self.current_question = ''
        self.current_round = 1
        self.current_phase = 1
        self.current_phase_question = 1
        self.already_asked_questions = []
        

    def run(self):
        '''
        This method is responsible for the main game logic. Returns a variable called win_or_loose:
        win_or_loose = 1 if you won;
        win_or_loose = -1 if you lost;
        win_or_loose = 0 if you decided to stop the game
        '''

        while True:
            self.current_question = self.generate_question()
            self.already_asked_questions.append(self.current_question.text)

            user_answer = int(View.draw_question(self)['question'][0])
            
            # If the answer is correct
            if self.check_answer(user_answer):
                self.current_round += 1
                self.current_phase = math.ceil(self.current_round/5)
                self.current_phase_question = self.current_round - ((self.current_phase - 1) * 5)

                if self.current_round == 17:
                    win_or_loose = 1
                    break

                user_input = View.draw_question_end("acertou")['confirmation']

                if user_input == "Continuar":
                    continue

                elif user_input == "Parar":
                    win_or_loose = 0
                    break

            else:
                View.draw_question_end("errou")
                win_or_loose = -1
                break

        return win_or_loose


    def generate_question(self):
        '''
        Returns the Question object with the current question
        '''

        file_questions = open("perguntas_ativas.txt","r")
        file_answers = open("respostas_ativas.txt","r")

        if 0 < self.current_round < 6:
            questions_range = [0, 9]
        elif 5 < self.current_round < 11:
            questions_range = [10, 19]
        elif 10 < self.current_round < 17:
            questions_range = [20, 29]

        question_lines = file_questions.readlines()
        answer_lines = file_answers.readlines()

        file_questions.close()
        file_answers.close()

        # Generates a new question if that question was already asked
        while True:
            question_drawn = random.randint(questions_range[0], questions_range[1])

            if question_lines[question_drawn] in self.already_asked_questions:
                continue
            else:
                break

        return Question(question_lines[question_drawn],
                        [answer_lines[(question_drawn + 1) * 4 - 4], 
                         answer_lines[(question_drawn + 1) * 4 - 3], 
                         answer_lines[(question_drawn + 1) * 4 - 2], 
                         answer_lines[(question_drawn + 1) * 4 - 1]],
                         answer_lines[(question_drawn + 1) * 4 - 4])


    def check_answer(self, user_answer):
        '''
        Returns True if the answer is right and False otherwise
        '''

        selected_answer = self.current_question.answers[user_answer - 1]

        if self.current_question.right_answer == selected_answer:
            return True
        else:
            return False