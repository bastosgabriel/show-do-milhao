import os
import platform

from PyInquirer import style_from_dict, prompt, Separator
from examples import custom_style_1

if platform.system() == 'Windows':
    clear = lambda: os.system('cls')
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    clear = lambda: os.system('clear')



class View():
    
    '''
    Draw the main menu and returns the user input
    '''
    @staticmethod
    def draw_main_menu():
        clear()

        menu = [
            {
                'type': 'list',
                'message': 'Bem-vindo ao Show do Milhao da família Aguiar!',
                'name': 'main menu',
                'choices': ["Começar", "Ler regras", "Fechar"]
            }
        ]

        return prompt(menu, style=custom_style_1)
    
    '''
    Draw the question scene and returns the user answer
    '''
    @staticmethod
    def draw_question(game):
        clear()

        if game.current_round == 16:
            question = [
                {
                    'type': 'list',
                    'message': f"{game.current_question.text}",
                    'name': 'question',
                    'choices': [
                        Separator(f"PERGUNTA FINAL!"),
                        Separator(),
                        f"1: {game.current_question.answers[0]}",
                        f"2: {game.current_question.answers[1]}",
                        f"3: {game.current_question.answers[2]}",
                        f"4: {game.current_question.answers[3]}",
                        Separator(),
                        Separator(" Prêmio: R$ {}".format(game.prizes[str(game.current_round)]['Acertar'])),
                    ],
                }
            ]
        else:
            question = [
                {
                    'type': 'list',
                    'message': f"{game.current_question.text}",
                    'name': 'question',
                    'choices': [
                        Separator(f"{game.current_phase}º Fase - Pergunta {game.current_phase_question}/5"),
                        Separator(),
                        f"1: {game.current_question.answers[0]}",
                        f"2: {game.current_question.answers[1]}",
                        f"3: {game.current_question.answers[2]}",
                        f"4: {game.current_question.answers[3]}",
                        Separator(),
                        Separator(" Prêmio: R$ {}".format(game.prizes[str(game.current_round)]['Acertar'])),
                    ],
                }
            ]
        
        return prompt(question, style=custom_style_1)
    
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
            confirmation = [
                {
                    'type': 'list',
                    'message': "PARABÉNS!! Você acertou a resposta, deseja continuar?",
                    'name': 'confirmation',
                    'choices': ["Continuar", "Parar"],
                }
            ]
        
            return prompt(confirmation, style=custom_style_1)

        elif answer_result == "errou":
            confirmation = [
                {
                    'type': 'list',
                    'message': "Poxa, esta não era a resposta correta",
                    'name': 'confirmation',
                    'choices': ["OK :("],
                }
            ]
        
            return prompt(confirmation, style=custom_style_1)
        
    '''
    Draw last game scene, which tells you if you won or lost the game
    '''
    @staticmethod
    def draw_game_end(win_or_loose):
        clear()
        if win_or_loose == 1:
            print("PARABÉNS!!!!1!!! VOCÊ É UM VENCEDOR")
            print("         /\     /\               ")
            print("        {  `---'  }              ")
            print("        {  O   O  }              ")
            print("      ~~|~   V   ~|~~            ")
            print("         \  \|/  /               ")
            print("          `-----'__              ")
            print("          /     \  `^\_          ")
            print("         {       }\ |\_\_   W    ")
            print("         |  \_/  |/ /  \_\_( )   ")
            print("         \__/  /(_E     \__/     ")
            print("           (  /                  ")
            print("            MM                   ")

        elif win_or_loose == 0:
            print("Bacana, vc saiu com um premio razoavel!")
        
        elif win_or_loose == -1:
            print("              :( Você perdeu :(                 ")
            print("          ,                                     ")
            print("          \`-._          __                     ")
            print("           \  `-..____,.'  `.                   ")
            print("           :`.         /     \`.                ")
            print("            : )       :       : \               ")
            print("            ;'        '   ;  |   :              ")
            print("            )..      .. .:.`.;   :              ")
            print("            /::...  .:::...   ` ;               ")
            print("            ; _ '    __        /:\              ")
            print("            `:o>   /\o_>      ;:. `.            ")
            print("           `-`.__ ;   __..--- /:.  \            ")
            print("           === \_/   ;=====_.':.    ;           ")
            print("            ,/'`--'...`--....        ;          ")
            print("                ;                     ;         ")
            print("              .'                       ;        ")
            print("            .'                         ;        ")
            print("          .'     ..     ,      .       ;        ")
            print("         :       ::..  /      ;::.     |        ")
            print("        /      `.;::.  |       ;:..    ;        ")
            print("        :        |:.   :       ;:.    ;         ")
            print("        :        ::     ;:..   |.     ;         ")
            print("        :       :;       :::....|     |         ")
            print("        /\     ,/ \       ;:::::;     ;         ")
            print("        .:. \:..|    :    ; '.--|     ;         ")
            print("       ::.  :''  `-.,,;     ;'   ;     ;        ")
            print("    .-'. _.'\      / `;      \,__:      \       ")
            print("    `---'    `----'   ;      /    \,.,,,/       ")
            print("                       `----`                   ")
            print("              :( Você perdeu :(                 ")