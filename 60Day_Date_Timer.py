import datetime

today = datetime.date.today() 

print("Calendar")
print()

event = input("What's event? ")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
eventD = datetime.date(year, month, day)

difference = eventD - today
difference = difference.days

if difference > 0: 
  print(f"Coming soon! {difference} day to go")
elif difference < 0: 
  print(f"😭😭😭 You missed it. It was {difference} day ago")
else:
  print(f"{event} is today!PARTY TIME!")
