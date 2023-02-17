import random
num = int(input("Enter a number between 1 and 20: "))
comp =  random.randint(1,20)
player = num
print("Player's number: " + str(num))
print("Computer's number: " + str(comp))
if player == comp:
  print("You won!")
else:
  print("You lost, better luck next time.")