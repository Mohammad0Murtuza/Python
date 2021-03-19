#Pokemon Konto Reagon

import random
import time

name = input("What is your Pokemon name?\n>>>")

Pokemon = ["Squartle","Balbasaur","Charmander","Pikachu","Spearow","Caterpie"]

Pokemon_1 = random.choice(Pokemon )

print(" ")
print("an {} appeared!".format(Pokemon_1 ))
print(" ")
player = 100
life2 = 100

#Your attack

while player > 1:
  time.sleep(1)
  print("==================")
  print(" ")
  print("{}'s life: {}\n{}'s life: {}".format(name, player, Pokemon_1 , life2))
  print(" ")
  time.sleep(1)
  print("What {} will do?".format(name))
  attack = int(input("[1] Normal attack\n[2] Special attack\n[3] Recover life\n>>>"))
  print(" ")
  
  if attack == 1:
    time.sleep(1)
    print("{} dealt 15 damage!".format(name))
    life2 = life2 - 15
    time.sleep(1)
    print("{} have {} life now!".format(Pokemon_1 , life2))
    print(" ")
    
  elif attack == 2:
    time.sleep(1)
    chance = random.randint(1,2)
    
    if chance == 1:
      print("{} dealt 35 damage!".format(name))
      life2 = life2 - 35
      time.sleep(1)
      print("{} have {} life now!".format(Pokemon_1 , life2))
      print(" ")
      
    else:
      print("{} failed!".format(name))
      
  elif attack == 3:
    time.sleep(1)
    print("{} recovered 30 life!".format(name))
    time.sleep(1)
    player = player + 30
    print("{} have {} life now!".format(name, player))
    
    #Win or lose
    
  if player < 1:
    time.sleep(1)
    print("{} lose...".format(name))
    time.sleep(2)
    break
    
  elif life2 < 1:
    time.sleep(1)
    print("{} wins!!".format(name))
    time.sleep(2)
    break
    
    #enemy attack
  
  print("==================")
  print(" ")
  print("{} time!".format(Pokemon_1 ))
  time.sleep(2)
  print(" ")
  
  attackofenemy = random.randint(1,3)
  
  if attackofenemy == 1:
    print("{} dealt 10 damage!".format(Pokemon_1 ))
    player = player - 10
    time.sleep(1)
    print("{} have {} life now!".format(name, player))
    print(" ")
  
  elif attackofenemy== 2:
    print("{} dealt 15 damage!".format(Pokemon_1 ))
    player = player - 15
    time.sleep(1)
    print("{} have {} life now!".format(name, player))
    print(" ")
    
  elif attackofenemy== 3:
    print("{} dealt 20 damage!".format(Pokemon_1 ))
    player = player - 20
    time.sleep(1)
    print("{} have {} life now!".format(name, player))
    print(" ")
    
  print(" ")
  
  #win or lose 2
  
  if player < 1:
    time.sleep(1)
    print("{} lose...".format(name))
    time.sleep(2)
    break
    
  elif life2 < 1:
    time.sleep(1)
    print("{} wins!!".format(name))
    time.sleep(2)
    break
