import os
import platform

if platform.system() == 'Windows':
    clear = lambda: os.system('cls')
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    clear = lambda: os.system('clear')

class View():
    
    def printRed(msg): print(f"\033[91m {msg}\033[00m", end='')
    def printGreen(msg): print(f"\033[92m {msg}\033[00m", end='')
    def printYellow(msg): print(f"\033[93m {msg}\033[00m", end='')
    def printLightPurple(msg): print(f"\033[94m {msg}\033[00m", end='')
    def printPurple(msg): print(f"\033[95m {msg}\033[00m", end='')
    def printCyan(msg): print(f"\033[96m {msg}\033[00m", end='')
    def printLightGray(msg): print(f"\033[97m {msg}\033[00m", end='')
    def printBlack(msg): print(f"\033[98m {msg}\033[00m", end='')

    '''
    Draw the main menu
    '''
    @staticmethod
    def draw_main_menu():
        clear()

        print("/----------------------------------------------/")
        print("/          Bem-vindo ao Show do Milhão         /")
        print("/             da familia Aguiar!               /")
        print("/                                              /")
        print("/                                              /")
        print("/           ", end='')
        View.printGreen("C")
        print("OMEÇAR      LER", end='')
        View.printGreen("R")
        print("EGRAS           /")
        print("/                                              /")
        print("/                                              /")
        print("/                                              /")
        print("/         pressione a letra em destaque        /")
        print("/           para escolher uma opção            /")
        print("/----------------------------------------------/")
        
    '''
    Draw the question scene
    '''
    @staticmethod
    def draw_question(_round, current_question):
        clear()

        print("/----------------------------------------------/")
        print(f"/ {_round}º Rodada - pergunta 1/5                   /")
        print("/                                              /")
        print(f"/ {current_question.text}                            /")
        print("/                                              /")
        print("/                                              /")
        print(f" (1): {current_question.answers[0]}            /")
        print(f" (2): {current_question.answers[1]}            /")
        print(f" (3): {current_question.answers[2]}            /")
        print(f" (4): {current_question.answers[3]}            /")
        print("/                                              /")
        print("/         pressione a letra em destaque        /")
        print("/           para escolher uma opção            /")
        print("/----------------------------------------------/")
    
    '''
    Draw the rules scene
    '''
    @staticmethod
    def draw_rules():
        clear()
        print("this is draw_rules")
        
    '''
    Draw the post question scene, which tells you if you succeed or failed 
    '''
    @staticmethod
    def draw_question_end(answer_result):
        clear()
        if answer_result == "acertou":
            print("this is draw_question_end ACERTOU")

        elif answer_result == "errou":
            print("this is draw_question_end ERROU")
        
    '''
    Draw last game scene, which tells you if you won or loose
    '''
    @staticmethod
    def draw_game_end(win_or_loose):
        clear()
        print(f"this is draw_game_end {win_or_loose}")
        