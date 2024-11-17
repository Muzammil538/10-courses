import random

rpc = ["Rock", "Paper", "Scissor"]

cp = random.choice(rpc)

def RPCGame():
  user = input("Enter : ")
  for x in rpc:
    if(user.lower == x.lower):
      if(user.lower == "rock"): 
        if(cp == "rock"):
          print("It's a tie!")
          break
        
        elif(cp == "paper"):
          print("Paper covers rock! Computer wins!")
          continue
        elif(cp == "scissor"):
          print("Rock crushes scissor! You win!")
          break
      elif(user.lower == "paper"): 
        if(cp == "paper"):
          print("It's a tie!")
          break
        
        elif(cp == "rock"):
          print("Paper covers rock! You wins!")
          continue
        elif(cp == "scissor"):
          print("scissor cuts paper! Computer win!")
          break
      elif(user.lower == "scissor"): 
        if(cp == "scissor"):
          print("It's a tie!")
          break
        
        elif(cp == "rock"):
          print("Rock break scissor! Computer wins!")
          continue
        elif(cp == "paper"):
          print("scissor cuts paper! You win!")
          break
    else:
      print("Wrong Input")
      RPCGame()
     
RPCGame()