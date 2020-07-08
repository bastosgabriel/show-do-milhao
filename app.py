from game import Game
from view import View
from question import Question

while True:
    View.draw_main_menu()
    
    user_input = input()

    if user_input in 'cC':
        # Run main game
        win_or_loose = Game.run()
        View.draw_game_end(win_or_loose)
        input()
        

    elif user_input in 'rR':
        # Show the rules
        View.draw_rules()
    
    elif user_input in 'fF':
        break
    