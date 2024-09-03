print("== Very precisely Weekly Horoscope Forecast! ==")
print()
print(
    "That's amazing Horoscope was written our PRO Horoscope medium. She predicts future over than 10 years!!! Let's make your personal Horoscope!"
)
print()
name = input("What's your name? ")
print()
print("Hello", name, "we waited you!")
print()
horoscopeType = input(
    "What type of the horoscope interests you? General, love, money, career?: "
)
print()
print()

if horoscopeType == "General" or horoscopeType == "general":
  horoscopeSign = input("What's your horoscope sign?: ")
  if horoscopeSign == "Aries" or horoscopeSign == "aries":
    print()
    print(
        "You're on fire this week, Aries! Just don't set off the smoke alarms with your awesomeness. Take charge and blaze new trails—sunscreen not included!"
    )
  elif horoscopeSign == "Taurus" or horoscopeSign == "taurus":
    print("")
  else:
    print("Very suspicious, try one more time!")

elif horoscopeType == "Money" or horoscopeType == "money":
  print(
      "Noo, something happened! Try the LOVE horoscope, our medium says that it's more important now!"
  )
  print()
  horoscopeType = input(
      "What type of the horoscope interests you? General, love, money, career?: "
  )

elif horoscopeType == "Career" or horoscopeType == "career":
  print(
      "Noo, something happened! Try the LOVE horoscope, our medium says that it's more important now!"
  )
  print()
  horoscopeType = input(
      "What type of the horoscope interests you? General, love, money, career?: "
  )

elif horoscopeType == "Love" or horoscopeType == "love":
  print(
      "Hmm, or medium said that today available only general horoscope. Please, try general or you can buy premium subscription here"
  )

else:
  print(
      "Noo, something happened! Try the LOVE horoscope, our medium says that it's more important now!"
  )
  print()
  horoscopeType = input(
      "What type of the horoscope interests you? General, love, money, career?: "
  )
