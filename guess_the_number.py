#guess the number
chances = 3

import random
ranNum= random.randint(0,9)

print ("Welcome to the guesss the number game \n==================")
for i in range (3):
    num = int(input("enter a number between 0 and 5 \n"))
    if(num == ranNum):
        print("Bingo you got it !!! \n number is {}".format(ranNum) )
        break
    else:
        chances = chances -1
        if (chances == 0):
            print("Sorry try again next time !!! The number is {} \n Thank you for playing ".format(ranNum))
        else:
            print("please guess again you have {} chances".format(chances))
    

