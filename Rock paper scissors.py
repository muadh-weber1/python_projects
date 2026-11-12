import random
options=["rock","scissors","paper"]
player_score=0
computer_score=0
while True:
  player_input=input("type rock/paper/scissors/quit").lower()
  if player_input=="quit":
    print("BYE")
    break
  if player_input not in options:
    continue
  random_numbers=random.randint(0,2)
  computer_input=options[random_numbers]
  print("computer chose",computer_input)
  if player_input=="rock" and computer_input=="paper":
    print("you won")
    player_score+=5
  elif player_input=="scissors" and computer_input=="paper":
    print("you won")
    player_score+=5
  elif player_input=="paper" and computer_input=="rock":
    print("you won")
    player_score+=5
  elif player_input==computer_input:
    print("tie")
    player_score+=1
    computer_score+=1
  else:
    print("you lost")
    computer_score+=5
    player_score+=0
print("شكر خزء")
print("computer scores", computer_score )
print("you scored",player_score)
  
if player_score>computer_score:
      print("you won")
elif player_score<computer_score:
  print("computer won")
else:
  print("TIE MATCH")
    
   

  



