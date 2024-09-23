import csv 

total = 0.0

with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) 
  for row in reader: 
    total += float(row["Quantity"]) * float(row["Cost"])
    
print("🌟Shop $$ Tracker🌟")
print()
print(f"Your shop took ${round(total,2)} today")
