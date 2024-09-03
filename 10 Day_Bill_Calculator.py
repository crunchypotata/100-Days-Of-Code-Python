bill = float(input("What was the bill?: "))
people = int(input("How many people were?: "))
tip = int(input("What percentage do you want to tip?: "))
answer = bill / people + tip / 100 * bill
print("You owe", answer)

