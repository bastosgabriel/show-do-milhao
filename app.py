from game import Game
from view import View
from question import Question

def switch(input):
    if input in 'cC':
        # Run main game
        Game.run()
        # View.draw_game_end(win_or_loose)

    elif input in 'rR':
        # Show the rules

    else:
        # Do the default

while True:
    # view.draw_main_menu()
    
    switch(input())
    