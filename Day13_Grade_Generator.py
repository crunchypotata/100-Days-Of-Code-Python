print("\033[32m", "Grade Generator", "\033[0m")
print()
testName = input("What is the name of the test?: ")
maxScore = int(input("What is the maximum score you can receive?: "))
yourScore = int(input("What is your score?: "))
print()
numberScore = float(yourScore / maxScore)
finalNumber = round(numberScore, 2)
if finalNumber >= .90:
  print("\033[32m","Yay, you got an A+", "\033[0m")
elif finalNumber >= .80 and finalNumber <= .89:
  print("You got an A-")
elif finalNumber >= .70 and finalNumber <= .79:
  print("You got a B")
elif finalNumber >= .60 and finalNumber <= .69:
  print("You got a C")
elif finalNumber >= .50 and finalNumber <= .59:
  print("You got a D")
elif finalNumber <= .49:
  print("\033[31m","You got a U,", "you need study more!" "\033[0m")

