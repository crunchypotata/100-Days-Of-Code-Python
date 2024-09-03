import random

bingoNum = []             

for number in range(8):
  number = random.randint(0,90)          
  if number not in bingoNum:
    bingoNum.append(number)
    
            
def prettyPrint():
  for row in bingoNum:
    print(row)
              

bingoNum = [  [bingoNum[0], bingoNum[1], bingoNum[2]],
              [bingoNum[3], "BINGO", bingoNum[4]],
              [bingoNum[5], bingoNum[6], bingoNum[7]] ]


print("BINGO GENERATOR")
print()

prettyPrint()

