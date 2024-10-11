import random
computerScore = 0
PlayerScore = 0
while True:
   choices = ["rock","paper","scissors"]

   computer = random.choice(choices)

   player = None

   while player not in choices:
      player = input("rock, paper, or scissors ?:").lower()


   if player == computer:
      print("Computer:", computer)
      print("Player:", player)
      print("It's tie")
   elif player == "rock":
      if computer == "paper":
        print("Computer:", computer)
        print("Player:", player)
        print("You lose!")
        computerScore += 1
      if computer == "scissors":
        print("Computer:", computer)
        print("Player:", player)
        print("You Win!")
        PlayerScore += 1
   elif player == "scissors":
      if computer == "rock":
        print("Computer:", computer)
        print("Player:", player)
        print("You lose!")
        computerScore += 1
      if computer == "paper":
        print("Computer:", computer)
        print("Player:", player)
        print("You win!")
        PlayerScore += 1
   elif player == "paper":
     if computer == "scissors":
        print("Computer:", computer)
        print("Player:", player)
        print("You lose!")
        computerScore += 1
     if computer == "rock":
        print("Computer:", computer)
        print("Player:", player)
        print("You win!")
        PlayerScore += 1
   play_again = input("Play again? (yes / no): ").lower()

   if play_again != "yes":
       break
print("BYE !")
print("PLAYER SCORE :",PlayerScore)
print("COMPUTER SCORE :",computerScore)






