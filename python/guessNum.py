import random

# num = random.randint(1000, 2000)
num = 1234
q1 = "Enter the Guess Number : "
q2 = "Try Again : "
guessCount = 0



def Guessing(c):
  un = int(input(q1))
  c = c + 1
  if(un != num):
    Guessing(c)
  else:
    print("You Won !")
    print("Number of Guesses : ", c)
  
Guessing(guessCount)