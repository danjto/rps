#import modules
import random


#set win/lose vars,list of plays and winning pairs
winner = "You WON! Congratulations!"
loser = "You LOST! Better luck next time!"
plays = ["ROCK","PAPER","SCISSORS"]
beats = [("ROCK","SCISSORS"),("PAPER","ROCK"),("SCISSORS")]


def main():
    #assign random play to computer
    play_comp = random.choice(plays)


    #force player to choose a valid option
    while True:

        #player chooses play
        play_player = input("ROCK, PAPER or SCISSORS? ").upper()

        #check player input is valid. If not, try again.
        if play_player in plays:
            break
        else:
            print(f"{play_player}. Invalid selection. Try again.")


    #announce plays
    print(f"You play {play_player}")
    print(f"Computer plays {play_comp}")


    #determine winner
    if play_player == play_comp:
        print("It's a DRAW!")
    else:
        #if winning pair
        if (play_player,play_comp) in beats:
            print(winner)

        else:
            print(loser)


while True:
    main()
    if input("Play again? (Y/N) ").strip().upper() != "Y":
        break
