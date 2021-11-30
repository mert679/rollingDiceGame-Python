import random

startGame = str(input("Press y for start game: "))

max_value = 6
min_value = 1

def diceGame():
  diceCounter = 0
  computerWin = 0
  userWin =0
  draws= 0
  while True:
    if startGame == "y":
        
        try:
          userDecision= int(input("Enter value between 1-6 "))
        except:
          print("You entered an invalid number.")
          continue
        diceCounter +=1
        numberOnDice = random.randrange(min_value,max_value+1)
        if userDecision > max_value or min_value>userDecision:
          print("The value is out of range.")
          continue
        if numberOnDice < userDecision:
          userWin +=1
          print("User wins",userDecision,"vs",numberOnDice)
            
        elif numberOnDice > userDecision:
          computerWin += 1
          print("Computer wins",numberOnDice,"vs",userDecision)
        else:
          draws += 1
          print("Thats draws")
        if diceCounter == 5:
          print("Reporting the results:")
          print("Total number of dice rolls:",diceCounter)
          print("The user won",userWin,"times")
          print("The computer won",computerWin,"times")
          print("The draws were",draws,"times")
          break

while True:
  diceGame()
  goAgain = input("press any key other than y to quit the game. Press y to play rolling dice. :)")
  if(goAgain !="y"):
    break

print()
print("The game has ended")
