from game import Game
from view import View
from question import Question

def switch(input):
    if input in 'cC':
        # Run main game
        win_or_loose = Game.run()
        View.draw_game_end(win_or_loose)
        return

    elif input in 'rR':
        # Show the rules
        View.draw_rules()
        return

while True:
    View.draw_main_menu()
    switch(input())  