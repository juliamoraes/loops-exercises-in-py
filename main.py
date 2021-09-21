import random 

value = random.randint(0,100)

while (value !=answer): 
   answer = int(input("Pick a number between 1 to 100")) 
   if(value > answer):
    print("Higher number, try it again")
   if (value < answer):
    print("Lower number, try it again")
   if (value == answer):
    print("You`ve guessed it right")



