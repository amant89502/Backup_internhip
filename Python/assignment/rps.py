import random
game_list=['r','p','s']
a=random.choice(game_list)
print(a)

b=input("Enter anyone r,p or s--")
for i in 1,10:

  if(a==b):
    print("Draw")
    break
  elif(a=='r' and b=='p'):
    print(" You won!")
    break
  elif(a=='p' and b=='r'):
      print("you lost")
      break
  elif(a=='s' and b=='p'):
    print("You lost")
    break
  elif(a=='p' and b=='s'):
    print("You won")
    break
  elif(a=='r' and b=='s'):
    print("you lost")
    break
  elif(a=='s' and b=='r'):
    print("You won")
    break