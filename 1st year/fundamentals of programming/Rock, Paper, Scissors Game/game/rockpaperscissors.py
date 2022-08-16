import random
from enum import Enum


class Choice(Enum):
    rock = 1
    paper = 2
    scissors = 3
    none = 4

    @staticmethod
    def input_list():
        """
        returns a list from the enumerator
        :return: list of options (rock, paper, scissors, none)
        """
        options = list()
        for option in Choice:
            options.append(option.name)
        return options


class RockPaperScissors:

    def __init__(self):
        self._player_option = ""
        self._computer_option = ""
        self._computer_wins = 0
        self._player_wins = 0
        self._running = True

    def print_state(self):
        """
        prints the current score
        :return: none
        """
        print(f"SCORE\nPLAYER {self._player_wins} - {self._computer_wins} COMPUTER\n\n")

    def winner(self):
        """
        prints the winner of the game
        :return: none
        """
        if self._player_wins > self._computer_wins:
            print(f"Player wins, great job!")
        elif self._computer_wins > self._player_wins:
            print("Computer wins, beep boop!")
        else:
            print("Tie, ggwp!")

    def check_if_continue(self):
        """
        checks to see if the player wants to continue playing
        :return: none
        """
        cont = None
        while cont != "y" and cont != "n":
            cont = input("Continue? (y/n): ")
            if cont != "y" and cont != "n":
                print("Invalid option!")
                continue
            break
        if cont == "n":
            self._running = False
            self.winner()
        print("\n")

    def get_player_input(self):
        """
        gets player input, checking for wrong input
        :return: none
        """
        self._player_option = None
        options = Choice.input_list()
        while self._player_option not in options:
            self._player_option = input("Choose your option!\n\nChoice: ")
            if self._player_option == "none, lmao":  # silly easter egg
                self._player_option = "none"
            if self._player_option == "none":  # but not the basic one
                self._player_option = "we don't like this one"
            if self._player_option not in options:
                print("Invalid option!")

    def get_computer_input(self):
        """
        generates a random move for the computer
        :return: none
        """
        self._computer_option = random.randint(1, 3)
        self._computer_option = Choice(self._computer_option).name

    def round_winner(self):
        """
        checks for the round winner and updates the score
        :return: none
        """
        if self._player_option == self._computer_option:  # tie
            self._player_wins += 1
            self._computer_wins += 1
            print(f"\nComputer chose {self._computer_option}.\nRound tie!\n\n")

        elif (self._player_option == "rock" and self._computer_option == "paper") or (
                self._player_option == "paper" and self._computer_option == "scissors") or (
                self._player_option == "scissors" and self._computer_option == "rock"):  # computer win
            self._computer_wins += 1
            print(f"\nComputer chose {self._computer_option}.\nlmao, Computer wins the Round!\n\n")

        elif self._player_option == "none":  # easter egg
            self._player_wins = 999
            print("\n")
            self.print_state()
            print("\nOur True Ruler.")
            self._running = False
            print("\nPlease, Show Us How To Slay.\n\n")

        else:  # player win
            self._player_wins += 1
            print(f"\nComputer chose {self._computer_option}.\nPlayer wins the Round, gg!\n\n")

    def start(self):
        """
        game start! I could move this and create a UI class, but I don't want to
        :return: none
        """
        while self._running:
            self.print_state()
            self.get_player_input()
            self.get_computer_input()
            self.round_winner()
            if not self._running:  # for the easter egg
                break
            self.check_if_continue()
