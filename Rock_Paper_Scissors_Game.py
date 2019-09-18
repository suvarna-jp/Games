# Rock_Paper_Scissors_Game.py

from random import randint
from datetime import datetime

def startGame():

    start_time = datetime.now().replace(microsecond=0)
    current_time = datetime.now().replace(microsecond=0)
    time_diff = current_time - start_time

    print("\nWelcome to the \n\tTerminal Rock-Paper-Scissors Game!!")
    print("\nRules :: Both, 'you' & 'the computer' choose one of the following options \n\t[R] Rock | [P] Paper | [S] Scissors")
    print("The winner would be decided based on the following rules :")
    print("\n>>> Rock would blunt the scissors \n>>> Paper would cover the rock \n>>> Scissors would cut the paper")
    print("\nYou play against the Computer & see who wins!! ")

    # list of options to play Rock_Paper_Scissors_Game
    options = ["Rock", "Paper", "Scissors"]

    # Variables to record the number of games & wins
    games_played = 0
    player_wins = 0
    computer_wins = 0

    # wanna_play would remain True until the player chooses to Exit game
    wanna_play = True

    while wanna_play:

        # Random option assigned to the computer
        computer_option = options[randint(0,2)]

        #set player to True
        print("Choose an option to play :: ")
        print("\n[R] Rock \n[P] Paper \n[S] Scissors \n[E] Exit Game?")
        player_input = input("\nEnter your option :: ")

        if(player_input == None or player_input.strip() == ""):
            print("You entered an empty value. Try again...")
            print("Please select an option : Type R|P|S|E and hit <enter> ")
            continue
        elif(player_input == 'R'):
            player_option = "Rock"
            games_played += 1
        elif(player_input == 'P'):
            player_option = "Paper"
            games_played += 1
        elif(player_input == 'S'):
            player_option = "Scissors"
            games_played += 1
        elif(player_input == 'E'):
            player_input = input("Are you sure you wanna Exit the game? [Y] Yes | [N] No :: ")
            if (player_input != None and player_input == 'Y'):
                if(player_wins==computer_wins==0):
                    pass
                else:
                    current_time = datetime.now().replace(microsecond=0)
                    time_diff = current_time - start_time
                    print("\nYou chose to Exit!")
                    print("The final scores are :: ")
                    print("======================================================")
                    print(f"Total games played :: {games_played} \nTotal time taken :: {time_diff}")
                    print(f"\nYou won {player_wins} times \nComputer won {computer_wins} times")
                    print("======================================================")
                    if(player_wins > computer_wins):
                        print("Congratulations!! You won most games against the computer!!")
                    elif(computer_wins > player_wins):
                        print("Computer won most games against you!! Better luck next time!!")
                    else:
                        print("Yow won the same number of times as the computer! :-)")

                print("\nThankyou for choosing to play Terminal Rock-Paper-Scissors Game!!")
                print("GoodBye! & See you again!!\n")

                wanna_play = False
                break
            elif(player_input != None and player_input != 'N'):
                print("You chose an Invalid input. Please try again!!")
                continue
            else:
                continue
        else:
            print("You entered an invalid input. Try again...")
            print("Please select an option : Type R|P|S|E and hit <enter> ")
            continue

        print("\n____________________________________________")
        print("Player Option \t|Vs| \tComputer Option")
        print(f"\n  {player_option}   \t|Vs| \t  {computer_option}  ")
        print("____________________________________________\n")

        if player_option == computer_option:
            print("OOOHH! \nIt was a --Tie--!")
        elif player_option == "Rock":
            if computer_option == "Paper":
                print("Uh-Oh! You lose!")
                print(f"{computer_option} covered {player_option}")
                computer_wins += 1
            else:
                print("Yoohooo!! You win!")
                print(f"{player_option} smashed {computer_option}")
                player_wins += 1
        elif player_option == "Paper":
            if computer_option == "Scissors":
                print("Uh-Oh! You lose!")
                print(f"{computer_option} cut the {player_option}")
                computer_wins += 1
            else:
                print("Yoohooo!! You win!")
                print(f"{player_option} covered {computer_option}")
                player_wins += 1
        elif player_option == "Scissors":
            if computer_option == "Rock":
                print("Uh-Oh! You lose!")
                print(f"{computer_option} smashed {player_option}")
                computer_wins += 1
            else:
                print("Yoohooo!! You win!")
                print(f"{player_option} cut the {computer_option}")
                player_wins += 1
        else:
            print("Invalid option!! Try Again...")

        current_time = datetime.now().replace(microsecond=0)
        time_diff = current_time - start_time
        print(f"\nNumber of games played :: {games_played}  ||  Total time taken :: {time_diff}")
        print("======================================================================")
        print("Player Wins \t|Vs| \tComputer Wins")
        print(f"\n\t  {player_wins}   \t|Vs| \t  {computer_wins}  \n")
        print("\n[Note: --Tie-- is not counted as a 'Win']")
        print("======================================================================\n")
        

if __name__ == "__main__":
    startGame()

