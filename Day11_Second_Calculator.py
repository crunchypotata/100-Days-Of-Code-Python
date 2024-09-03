print("Second's Canculator")
# choose = input("Which second do you want to calculate?: ")
choose2 = input("Do you want to calculate lear year or regular year? (y/n): ")
second = 1
minute = 60 * second
hour = minute * 60
day = hour * 24
year = day * 365
leapYear = day * 366
if choose2 == "y":
  print(year)
elif choose2 == "n":
  print(leapYear)
else:
  print("Try one more")
