from domain.board import *
from ui.ai import *


class UI:
    def __init__(self):
        self._running = True
        self._game = AIController()

    def menu(self):
        print("WELCOME TO ACHI!\n\n")
        while self._running is True:  # GAME RUNNING
            if self._game.get_turn() == "human":  # HUMAN TURN
                if self._game.get_piece_count() != 0:
                    print("PLACEMENT PHASE")
                    print(self._game)  # PLACEMENT PHASE
                    print("Your turn!\n")
                    x = input("Please input the x coordinate of your move: ")
                    y = input("Please input the y coordinate of your move: ")
                    try:
                        self._game.execute_move(x, y)  # DO MOVE
                    except ValueError as ve:
                        print(ve)
                    if self._game.check_for_win() is True:  # IF WON THEN END GAME
                        self._running = False
                        print(self._game)
                        print("Human wins!")

                else:
                    print("MOVEMENT PHASE")
                    print(self._game)
                    print("Your turn!\n")
                    x = input("Please input the x coordinate of the piece you want to move: ")
                    y = input("Please input the y coordinate of the piece you want to move: ")
                    try:
                        self._game.execute_a_moving_piece(x, y)
                    except ValueError as ve:
                        print(ve)
                    if self._game.check_for_win() is True:
                        self._running = False
                        print(self._game)
                        print("Player wins! (MOVEMENT PHASE)")

            else:
                if self._game.get_piece_count() != 0:
                    self._game.do_move()
                    if self._game.check_for_win() is True:  # IF WON THEN END GAME
                        self._running = False
                        print(self._game)
                        print("Computer wins!")
                else:
                    self._game.do_moving_move()
                    if self._game.check_for_win() is True:
                        self._running = False
                        print(self._game)
                        print("Computer wins! (MOVEMENT PHASE)")


if __name__ == "__main__":
    g = UI()
    g.menu()
