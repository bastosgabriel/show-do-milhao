import os
import platform

from PyInquirer import style_from_dict, prompt, Separator
from examples import custom_style_1

# This creates a function called clear() that executes the system command to clear the terminal
if platform.system() == 'Windows':
    clear = lambda: os.system('cls')
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    clear = lambda: os.system('clear')


class View():
    '''
    The view class is responsible for all the visualization of questions, answers and etc on the terminal.
    It's also responsible for retrieving the user inputs using PyInquirer.
    '''
    
    @staticmethod
    def draw_main_menu():
        '''
        Draw the main menu and returns the user input.
        '''
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
    
    @staticmethod
    def draw_question(game):
        '''
        Draw the question scene and returns the user answer. Receives the game object as parameter to print the question, answers, round etc
        '''
        def disable_power(uses, used_power):
            if (uses == 0) or (used_power):
                return 'opção desabilitada'
            else:
                return False

        def disable_by_answer(current_answer, disabled_answers):
            if current_answer in disabled_answers:
                return 'opção desabilitada'
            else:
                return False

        clear()

        # Check if its the last round
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
                        {
                            'name': f"1: {game.current_question.answers[0]}",
                            'disabled': disable_by_answer(game.current_question.answers[0], game.disabled_answers)
                        }, 
                        {
                            'name': f"2: {game.current_question.answers[1]}",
                            'disabled': disable_by_answer(game.current_question.answers[1], game.disabled_answers)
                        }, 
                        {
                            'name': f"3: {game.current_question.answers[2]}",
                            'disabled': disable_by_answer(game.current_question.answers[2], game.disabled_answers)
                        }, 
                        {
                            'name': f"4: {game.current_question.answers[3]}",
                            'disabled': disable_by_answer(game.current_question.answers[3], game.disabled_answers)
                        }, 
                        Separator(),
                        {
                            'name': f'5: Pular questão (Pulos restantes: {game.skips})',
                            'disabled': disable_power(game.skips, game.used_power)
                        },
                        {
                            'name': f'6: Usar cartas (Usos restantes: {game.cards_uses})',
                            'disabled': disable_power(game.cards_uses, game.used_power)
                        },
                        Separator(),
                        Separator(" Prêmio: R$ {}".format(game.prizes[str(game.current_round)]['Acertar'])),
                    ],
                }
            ]
        
        return prompt(question, style=custom_style_1)
    
    @staticmethod
    def draw_rules():
        '''
        Draw the rules scene.
        '''

        clear()
        print("O jogo possui 3 fases. Cada uma contendo 5 perguntas.")
        print("Na  primeira  fase,  as  perguntas  valem R$ 1 mil")
        print("com  incremento  de  R$  1  mil  por  pergunta.")
        print("Na segunda,  R$ 10 mil com incrementos de R$ 10 mil.")
        print("A terceira funciona igualmente porém com R$ 100 mil.")
        print("A  pergunta  final  vale  R$  1  milhão.")
        print("O jogador tem a opção de parar o jogo antes de responder")
        print("a próxima pergunta. Neste caso, ele fica com o último")
        print("prêmio recebido.")
        print("Se errar uma resposta, fica com metade do último prêmio")
        print("A não ser que seja a pergunta final, neste caso o")
        print("participante não leva nada")
        
    @staticmethod
    def draw_question_end(answer_result, game):
        '''
        Draw the post question scene, which tells you if you succeed or failed based on answer_result parameter.
        Also gives you the option to stop the game.
        '''

        clear()
        if answer_result == "acertou":
            confirmation = [
                {
                    'type': 'list',
                    'message': "PARABÉNS!! Você acertou a resposta, deseja continuar?",
                    'name': 'confirmation',
                    'choices': [
                        f"Continuar para pergunta de R$ {game.prizes[str(game.current_round)]['Acertar']}", 
                        f"Parar e ficar com R$ {game.prizes[str(game.current_round)]['Parar']}",
                        Separator(),
                        Separator(f"Errando a próxima pergunta você fica com: R$ {game.prizes[str(game.current_round)]['Errar']}")
                    ],
                }
            ]
        
            return prompt(confirmation, style=custom_style_1)

        elif answer_result == "errou":
            confirmation = [
                {
                    'type': 'list',
                    'message': "Poxa, esta não era a resposta correta",
                    'name': 'confirmation',
                    'choices': [
                        "OK :(",
                        Separator(f"Te restou R$ {game.prizes[str(game.current_round)]['Errar']}")
                    ],
                }
            ]
        
            return prompt(confirmation, style=custom_style_1)
        
    @staticmethod
    def draw_game_end(win_or_loose):
        '''
        Draw the last game scene, which tells you if you won or lost the game
        '''

        clear()
        if win_or_loose == 1:
            print("                                    PARABÉNS!!!!1!!! VOCÊ É O VENCEDOR                                  ")
            print("                                                                                                        ")
            print("                                                  ██████                                                ")
            print("                                              ████░░▒▒  ████                                            ")
            print("                                            ██▒▒░░░░▒▒░░░░░░██                                          ")
            print("                                          ██░░▒▒░░░░▒▒░░░░░░▒▒██                                        ")
            print("                                        ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██                                        ")
            print("                                        ██░░▒▒░░░░░░▒▒░░░░░░▒▒▓▓                                        ")
            print("                                      ▓▓▒▒▒▒▒▒░░░░░░▒▒░░░░░░▒▒░░██                                      ")
            print("                                      ██░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██                                      ")
            print("                                      ██░░░░▒▒░░░░░░▒▒░░░░░░▒▒░░██                                      ")
            print("                                    ██▒▒░░░░▒▒░░░░░░▒▒░░░░░░▒▒▒▒██                                      ")
            print("                                    ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░██                                      ")
            print("                                    ██░░░░░░▒▒░░░░▒▒░░░░░░░░▒▒░░██                                      ")
            print("                                    ██░░░░▒▒░░░░░░▒▒░░░░░░░░▒▒░░██                                      ")
            print("                                  ██▒▒░░░░▒▒░░░░░░▒▒  ░░░░░░▒▒▒▒░░██                                    ")
            print("                                  ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██                                    ")
            print("                                  ██░░░░░░▒▒░░░░░░▒▒░░░░░░░░▒▒░░░░██                                    ")
            print("                                  ██░░░░░░▒▒░░░░░░▒▒░░░░░░░░░░░░░░██                                    ")
            print("                                  ██▒▒▒▒░░▒▒░░░░░░▒▒░░░░░░░░▒▒▒▒▒▒██                                    ")
            print("                        ██▓▓████  ▓▓░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░██                                    ")
            print("                        ██▒▒▒▒▒▒▓▓██░░░░░░▒▒░░░░░░▒▒░░░░░░░░████░░██                                    ")
            print("                          ██▒▒▒▒▓▓▓▓▓▓░░░░▒▒░░░░░░▒▒░░░░▓▓▓▓▒▒██░░██        ██▓▓                        ")
            print("                          ██▒▒▒▒▒▒▒▒▓▓██░░▒▒░░░░░░▒▒░░██▒▒▒▒▒▒██▒▒▒▒██  ████▒▒██                        ")
            print("                            ▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒██░░░░██▓▓▒▒▒▒▒▒██                        ")
            print("                            ██▒▒▒▒▒▒▒▒▒▒██▒▒░░░░░░██▒▒▒▒▒▒▒▒▒▒██░░░░██▒▒▒▒▒▒██                          ")
            print("                            ██▒▒▒▒▒▒▓▓▒▒▒▒██░░░░░░██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██▓▓▓▓▓▓██                          ")
            print("                            ██▒▒▒▒▒▒▒▒▓▓▒▒██░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▓▓██░░██▒▒▓▓██                            ")
            print("                          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░██▒▒▓▓██                            ")
            print("                          ██▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██▒▒▓▓██                            ")
            print("                          ██▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒██░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██▒▒▓▓██                            ")
            print("                          ██▒▒▒▒▒▒░░░░▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▒▒▓▓██                            ")
            print("                          ██▒▒▒▒▒▒░░░░░░▒▒▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓██                            ")
            print("                        ██▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▓▓██                            ")
            print("                        ██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▓▓▓▓▒▒                          ")
            print("                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▒▒██                          ")
            print("                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒██                          ")
            print("                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▒██                          ")
            print("                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██▒▒▒▒██                          ")
            print("                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▒██                          ")
            print("                        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓██                          ")
            print("                          ██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓██                            ")
            print("                          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██▓▓██                            ")
            print("                          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██                            ")
            print("                            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒████                              ")
            print("                            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒████                              ")
            print("                              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██                                ")
            print("                                ██▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒██                                  ")
            print("                                  ████▒▒▒▒▒▒▒▒▒▒▓▓████▒▒▒▒▒▒▒▒▓▓████                                    ")
            print("                                      ████████████▓▓▓▓██████████                                        ")
            print("                                        ░░██▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██░░                                        ")
            print("                                          ██▓▓▒▒▓▓▒▒▒▒▒▒▒▒▓▓██                                          ")
            print("                                            ██▓▓████████████                                            ")
            print("                                                                                                        ")
            print("                                          GANHOU 1 BAITA MILHÃO                                         ") 
            input()

        elif win_or_loose == 0:
            print("Bacana, você saiu com um prêmio razoável!")
            input()
        
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
            print("      :(       :( Você perdeu :(       :(       ")

            input()


    @staticmethod
    def draw_cards(game):
        '''
        Draw the cards scene, that is when the user decided to drawn a card to potentially disable wrong answers.
        '''
        clear()

        card = [
            {
                'type': 'list',
                'message': 'Escolha sua carta!',
                'name': 'card',
                'choices': ["1: 🂠", "2: 🂠", "3: 🂠", "4: 🂠"]
            }
        ]

        return prompt(card, style=custom_style_1)

    @staticmethod
    def draw_card_reveal(game, chosen_card):
        '''
        Draw the card reveal scene. That is when the player get to know what card he actually choose.
        '''

        print("")

        if chosen_card == '3':
            print(f"Você escolheu um {chosen_card} de espadas! ", end='')
            print("🂣")
            print("Isso significa que serão desabilitadas 3 respostas erradas!")

        if chosen_card == '2':
            print(f"Você escolheu um {chosen_card} de espadas! ", end='')
            print("🂢")
            print("Isso significa que serão desabilitadas 2 respostas erradas!")
  
        if chosen_card == 'A':
            print(f"Você escolheu um {chosen_card} de espadas! ", end='')
            print("🂡")
            print("Isso significa que será desabilitada 1 resposta errada!")

        if chosen_card == 'K':
            print(f"Você escolheu um {chosen_card} de espadas! ", end='')
            print("🂮")
            print("Isso significa que nenhuma resposta será desabilitada! :(")

        input()
        