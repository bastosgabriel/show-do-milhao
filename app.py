from game import Game
from view import View

while True:

    user_input = View.draw_main_menu()['main menu']

    if user_input == 'Começar':
        # Run main game
        game = Game()
        win_or_loose = game.run()
        View.draw_game_end(win_or_loose)
       
    elif user_input == 'Ler regras':
        # Show the rules

        View.draw_rules()

    elif user_input == 'Fechar':
        break