# 🎲 Code runners
a console-based version of the code runner game, in which the human must determine the value of a pseudo-random number generated by the computer. 

The game works in the following way:  

1. When a new game is started, the computer generates a four digit random secret number; the first digit is non-zero and all digits are distinct (e.g. `1234`, `1984`, `1980`, `1024` are okay; `3435`, `2001`, `0123`, `8888` are not okay)
2. The game is played over a number of rounds. Each round is played in the following way:  
  
  **(a)** The human player enters a four digit number; if the number is not a valid guess (see rules from 1.), the game is over and the computer wins  
  **(b)** The computer informs the player about the number of codes and the number of runners. Codes are correct digits in the correct position, runners are correct digits but in incorrect positions   
  **(c)** `8086` is a cheat code that when entered as a guess, causes the computer to reveal the number it selected (the game otherwise continues as usual)  
    
3. The game ends after being played for more than 60 seconds, as measured in real-time **[1p]**, or when the player guesses the correct number **[1p]**. In either case, display a corresponding message.
