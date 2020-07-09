from game import Game
from view import View

while True:

    user_input = View.draw_main_menu()['main menu']

    if user_input == 'Começar':
        # Run main game
        game = Game()
        View.draw_game_end(game.run())
       
    elif user_input == 'Ler regras':
        # Show the rules
        View.draw_rules()
        input()

    elif user_input == 'Fechar':
        # Close the game
        break