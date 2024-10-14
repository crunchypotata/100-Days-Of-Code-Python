import os
import time
import pygame


pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()
pygame.mixer.pause()


def pause():
  pygame.mixer.pause()
  
pause()



def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    chose = int(input("Press 2 anytime to pause playng and return to the menu: "))
    if chose == 2:
      pause()
      return
    else:
      continue



while True:
  print("Best music player ever")
  time.sleep(5)
  os.system("clear")
  
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("Press anything else to see the menu again")
  u_input = int(input())
  
  if u_input == 1:
    print("Let's find something interesting")
    play()
  elif u_input == 2:
    print("Bye!")
    exit()
  else: 
    continue
  
