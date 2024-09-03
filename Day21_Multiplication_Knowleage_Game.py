print("Math Game!")
print()

number = int(input("Chose the number from 1 to 10: "))
print("Ok, let's fun!")

score = 0

for j in range (1, 11):
  print(j, "x", number, "= ")
  answer = int(input("Your answer: "))
  
  if answer == j*number:
    print("Correct!")
    score += 1
  
  else:
    print("Wrong! The correct answer is", j * number)

print()
print("Your score is", score, "out of 10")

if score == 10:
 print("\033[32m Wow, you are a math genius! \033[0m ")
elif score >5:
 print("Not bad!")
elif score <5: 
 print("\033[31m You need to practice more!!! \033[0m 😱😱😱 ")