import random
import time

wins = 0
losses = 0
draws = 0
rounds = 0

rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("================================")
print("     ROCK PAPER SCISSORS")
print("================================")
print("1 = Rock")
print("2 = Paper")
print("3 = Scissors")
print("n = New Game")
print("q = Quit")
print("================================")

while True:

    player = input("\nChoose: ").lower()

    if player == "q":
        print("\nGame closed")
        break

    if player == "n":
        wins = 0
        losses = 0
        draws = 0
        rounds = 0
        print("\nNew game started!")
        continue

    if player not in ["1", "2", "3"]:
        print("\nWrong button! Try again.")
        continue

    computer = random.randint(1, 3)

    print("\nRock...")
    time.sleep(0.5)

    print("Paper...")
    time.sleep(0.5)

    print("Scissors...")
    time.sleep(0.5)

    print("GO!\n")

    print("YOU:")

    if player == "1":
        print(rock)
        player_name = "Rock"

    elif player == "2":
        print(paper)
        player_name = "Paper"

    else:
        print(scissors)
        player_name = "Scissors"

    print("COMPUTER:")

    if computer == 1:
        print(rock)
        computer_name = "Rock"

    elif computer == 2:
        print(paper)
        computer_name = "Paper"

    else:
        print(scissors)
        computer_name = "Scissors"

    rounds += 1

    print("You chose:", player_name)
    print("Computer chose:", computer_name)

    if int(player) == computer:
        draws += 1
        print("\nDRAW!")

    elif (
        (player == "1" and computer == 3) or
        (player == "2" and computer == 1) or
        (player == "3" and computer == 2)
    ):
        wins += 1
        print("\nYOU WIN!")

    else:
        losses += 1
        print("\nYOU LOSE!")

    print("\n========== SCORE ==========")
    print("Wins:   ", wins)
    print("Losses: ", losses)
    print("Draws:  ", draws)
    print("Rounds: ", rounds)
    print("===========================")