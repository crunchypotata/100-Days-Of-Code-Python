print("🌟Factorial Finder🌟")
print()

n = int(input("Input your number: "))

def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value-1)
print(factorial(n))