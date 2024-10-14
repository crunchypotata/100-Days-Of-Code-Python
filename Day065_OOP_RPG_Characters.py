print("🌟Generic RPG🌟")

class character: 
  name = None
  hp = 100
  mp = 100
  
  def __init__(self, name):
    self.name = name

  def info(self):
    print(f"Name: {self.name}\nHp: {self.hp}\nMagic Points: {self.mp}")

  def setStats(self, name, hp, mp):
    self.hp = hp
    self.mp = mp

class player(character):
  nickname = None
  lives = 3
  
  def __init__(self, nickname):
    self.name = "Player"
    self.nickname = nickname

  def info(self):
    print((f"Name: {self.name}\nHP: {self.hp}\nMP: {self.mp}\nLives: {self.lives}\nNickname: {self.nickname}"))

  def alive(self):
    if self.lives >0:
      print(f"{self.nickname} is alive!")
      return True
    else:
      print(f"{self.nickname} was expired!")
      return False
      
pl = player("Rick")
pl.info()
print()
print(pl.alive())
print()

class enemy(character):

  type = None
  strength = None
  
  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength

  def info(self):
    print((f"Name: {self.name}\nHP: {self.health}\nMP: {self.magic}\nType: {self.type}\nStrength: {self.strength}\n"))

class orc(enemy):
  speed = None

  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed

  def info(self):
    print((f"Name: {self.name}\nHP: {self.hp}\nMP: {self.mp}\nType: {self.type}\nStrength: {self.strength}\nSpeed {self.speed}"))

bill = orc(250)
ted = orc(205)
charon = orc(270)

bill.info()
print()
ted.info()
print()
charon.info()
print()

class vampire(enemy):
  day = True

  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    self.day = day

  def info(self):
    print((f"Name: {self.name}\nHP: {self.hp}\nMP: {self.mp}\nType: {self.type}\nStrength: {self.strength}\nDay {self.day}"))

boris = vampire(False)
luck = vampire(True)

boris.info()
print()
luck.info()
print()


  