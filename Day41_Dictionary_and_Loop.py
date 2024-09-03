print("🌟Website Rating🌟")
print()

web = {"name": None, "URL": None, "description": None, "rating": None}

for name in web.keys():
  web[name] = input(f"{name}: ")


for name, value in web.items():
  print(f"{name}:{value}")
print()

