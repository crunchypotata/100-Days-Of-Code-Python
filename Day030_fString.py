# print("30 Days Down - What did you think?")
# print()
# for i in range(1, 31):
#   thought = input(f"Day {i}:\n")
#   print()
#   myText = f"You thought Day {i} was"
#   print(f"{myText:^35}")
#   print(f"{thought:^35}")
#   print()



print("Review of 100 day of Code")
print()
for i in range(1, 31):
  day = i
  answer = input(f"What do you think about {day: <2} day?\n")
  response = f"You thought that {day: <2} was {answer}!"
  print()
  print(response)
  print()
