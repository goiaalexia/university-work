from functionalities import *
import time


def game_start():
    number = generate_number()
    rounds = 1
    start_time = time.time()
    while True:
        print("Round ", rounds, "\n")
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= 60:
            print("Time's up! Computer wins!")
            return
        try:
            guessed_number = int(input("Try to guess the number: "))
        except ValueError:
            elapsed_time = current_time - start_time
            if elapsed_time >= 60:
                print("Time's up! Computer wins!")
                return
            print("Not a valid guess. Computer wins!")
            return
        if check_distinct_digits(guessed_number) is False or guessed_number < 1023 or guessed_number > 9876:
            elapsed_time = current_time - start_time
            if elapsed_time >= 60:
                print("Time's up! Computer wins!")
                return
            print("Not a valid guess. Computer wins!")
            return
        if guessed_number == number:
            elapsed_time = current_time - start_time
            if elapsed_time >= 60:
                print("Time's up! Computer wins!")
                return
            print("You guessed the number! Player wins!")
            return
        if guessed_number == 8086:
            elapsed_time = current_time - start_time
            if elapsed_time >= 60:
                print("Time's up! Computer wins!")
                return
            print("You dirty cheater. Here's your number:", number, "\n")
            rounds += 1
            continue
        if guessed_number != number:
            elapsed_time = current_time - start_time
            if elapsed_time >= 60:
                print("Time's up! Computer wins!")
                return
            code_number = codes(number, guessed_number)
            runner_number = runners(number, guessed_number)
            print("Your guess has", code_number, "codes and", runner_number, "runners\n")
            rounds += 1
            continue
