print("🌟Star Wars Name Generator🌟")
print()

name = input("What's your first name? ").strip()
surname = input("What's your surname? ").strip()
motherName = input("your mother's maiden name? ").strip()
city = input("The city where you were born? ").strip()
print()

nameSW = f"{name[0:3].capitalize()}{surname[0:3].lower()} {motherName[0:2].capitalize()}{city[-3:]}"

print(f"Your Star Wars name is {nameSW}")



