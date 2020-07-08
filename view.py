import os
import platform

if platform.system() == 'Windows':
    clear = lambda: os.system('cls')
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    clear = lambda: os.system('clear')

class View():
    
    def printRed(msg): print(f"\033[91m {msg}\033[00m") 
    def printGreen(msg): print(f"\033[92m {msg}\033[00m") 
    def printYellow(msg): print(f"\033[93m {msg}\033[00m") 
    def printLightPurple(msg): print(f"\033[94m {msg}\033[00m") 
    def printPurple(msg): print(f"\033[95m {msg}\033[00m") 
    def printCyan(msg): print(f"\033[96m {msg}\033[00m") 
    def printLightGray(msg): print(f"\033[97m {msg}\033[00m") 
    def printBlack(msg): print(f"\033[98m {msg}\033[00m") 

    @staticmethod
    def draw_main_menu():
        clear()
        print("this is the main menu")
        print("C para começar")
        print("R para ler regras")
        

    @staticmethod
    def draw_question(_round, current_question):
        clear()
        print(f"Rodada {_round}: {current_question.text}")
        print(f"(1): {current_question.answers[0]}")
        print(f"(2): {current_question.answers[1]}")
        print(f"(3): {current_question.answers[2]}")
        print(f"(4): {current_question.answers[3]}")
        
    
    @staticmethod
    def draw_rules():
        clear()
        print("this is draw_rules")
        

    @staticmethod
    def draw_question_end(answer_result):
        clear()
        if answer_result == "acertou":
            print("this is draw_question_end ACERTOU")

        elif answer_result == "errou":
            print("this is draw_question_end ERROU")
        

    @staticmethod
    def draw_game_end(win_or_loose):
        clear()
        print(f"this is draw_game_end {win_or_loose}")
        