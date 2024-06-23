import random
health = 10
lvl = 1
flag = 1
print("This is a health postion game \nYou have aloted 10 health")
print("By using the postion you can increase your health and it depends on your difficulty")

while(flag):
  opt = int(input("Enter difficulty level : \n1.Easy\n2.Medium\n3.Hard\n4.quit \nenter here: "))
  if(opt == 1):
    print("Choose another\n")
    
  elif(opt == 4):
    flag = 0
  
  else:
    lvl = opt
    health += int(random.randint(1,90) / lvl)
    print("Your health is now : \n",health)
    
    
  
