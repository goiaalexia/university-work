from domain.board import Board, MoveError
from domain.point import Point
from ui.ai import AI


class UserInterface:
    def __init__(self, rowss, columnss, modee, turnn):
        self._game_mode = modee  # players / ai
        self._ai_turn = turnn
        self._game_board = Board(rowss, columnss)
        if self._ai_turn is True:
            self._game_board.set_turn("second")
        self._game_board.create_board()
        self._game_running = True
        self._ai = AI()

    def print_board(self):
        print(self._game_board)

    def game_over(self):
        self._game_running = False

    def print_turn(self):
        if self._game_mode == "players":
            if self._game_board.get_turn() == "first":
                print("\nCurrent player: Player 1.\n")
            else:
                print("\nCurrent player: Player 2.\n")
        else:
            if self._ai_turn is False:
                print("\nYour turn!\n")

    def start(self):
        """
        the start of the game <3
        :return: None
        """
        print("OBSTRUCTION GAME")
        if self._game_mode == "players":
            while self._game_running:
                self.print_board()
                self.print_turn()
                try:
                    x = int(input("Enter the x coordinate of your move: "))
                    y = int(input("Enter the y coordinate of your move: "))
                    point = Point(x, y)
                    self._game_board.execute_move(point)
                    if self._game_board.available_moves() == 0:
                        self.game_over()
                        print(self._game_board)
                        if self._game_board.get_turn() == "first":
                            print(f"\nPlayer 2 wins!")
                        else:
                            print(f"\nPlayer 1 wins!")
                except ValueError:
                    print("Not a valid move! (move coordinates should be integers, dude)")
                except MoveError as yummy_message:
                    print(yummy_message)
        else:
            while self._game_running is True:
                if self._ai_turn is False:  # if it's the user's turn
                    try:
                        print(self._game_board)
                        self.print_turn()
                        x = int(input("Enter the x coordinate of your move: "))
                        y = int(input("Enter the y coordinate of your move: "))
                        point = Point(x, y)
                        self._game_board.execute_move(point)
                        self._ai_turn = not self._ai_turn
                        if self._game_board.available_moves() == 0:
                            self.game_over()
                            print(self._game_board)
                            print(f"\nYou win!")
                    except ValueError:
                        print("Not a valid move! (move coordinates should be integers, dude)")
                    except MoveError as yummy_message:
                        print(yummy_message)
                else:
                    move = self._ai.get_input(self._game_board)
                    self._game_board.execute_move(move)
                    self._ai_turn = not self._ai_turn
                    if self._game_board.available_moves() == 0:
                        self.game_over()
                        print(self._game_board)
                        print(f"\nComputer wins!")


if __name__ == "__main__":
    with open("settings.properties", "r") as f:
        mode = f.readline().strip().split(" ")[2]  # players / ai
    initial_input_is_not_good = True
    turn = 1
    while initial_input_is_not_good is True:
        try:
            turn = int(input("Enter 1 if you want to begin, and 2 if you want the computer/ other player to begin: "))
        except ValueError:
            print("Dude. 1 or 2. It's not that difficult. :> (integers)")
            continue
        if turn != 1 and turn != 2:
            print("Dude. 1 or 2. It's not that difficult. :>")
            continue
        initial_input_is_not_good = False
    if turn == 1:
        turn = False
    else:
        turn = True
    rows = columns = 0
    while True:
        try:
            rows = int(input("Please enter the number of rows: "))
            columns = int(input("Please enter the number of columns: "))
        except ValueError:
            print("Input numbers lmao")
            continue
        break
    ui = UserInterface(rows, columns, mode, turn)
    ui.start()
