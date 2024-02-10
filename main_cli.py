import random
import time
#Declaring Variables
operations=["s", "w", "g"]
total_chances=10
chance=0
sys_point=0
hum_point=0

#Header Section
print("WELCOME TO SNAKE-WATER-GUN GAME\n")

rules_input=input("Press Y to know the rules first and N to continue without rules:")
rules="1.   There are three things to select from i.e Snake, Water and Gun.\n2.   The Snake drinks the Water and wins.\n3.   The Water damages the Gun.\n4.   The Gun kills the Snake.\n5.   You get 10 chances to win this game.\n"
if rules_input=='Y' or rules_input=='y':
    print(rules)
elif rules_input=='N' or rules=='n':
    print()
    
print("Lets start.....\n")

#Game Starts
print("Enter 's' for Snake \nEnter 'w' for Gun\nEnter 'g' for Gun \n")

while chance<total_chances:
    sys_guess=random.choice(operations)
    hum_guess=input("Snake, Water or  Gun:")

    if sys_guess==hum_guess:
        print("The draw is tied\n0 points given to each")

    #Human Inputs Water:   
    elif sys_guess=='s' and hum_guess=='w':
        sys_point=sys_point+1
        print(f"System's guess is {sys_guess}, Your guess is {hum_guess} \n")
        print("System wins 1 point \n")
        print(f"System's points are {sys_point} and Your points are {hum_point}")
    
    elif sys_guess=='g' and hum_guess=='w':
        hum_point=hum_point+1
        print(f"System's guess is {sys_guess}, Your guess is {hum_guess} \n")
        print("You win 1 point \n")
        print(f"System's points are {sys_point} and Your points are {hum_point}")

    #Human Inputs Snake:
    elif sys_guess=='w' and hum_guess =='s':
        hum_point=hum_point+1
        print(f"System's guess is {sys_guess}, Your guess is {hum_guess} \n")
        print("You win 1 point \n")
        print(f"System's points are {sys_point} and Your points are {hum_point}")

    elif sys_guess=='g' and hum_guess=='s':
        sys_point=sys_point+1
        print(f"System's guess is {sys_guess}, Your guess is {hum_guess} \n")
        print("System wins 1 point \n")
        print(f"System's points are {sys_point} and Your points are {hum_point}")

    #Human Inputs Gun:
    elif sys_guess=='s' and hum_guess=='g':
        hum_point=hum_point+1
        print(f"System's guess is {sys_guess}, Your guess is {hum_guess} \n")
        print("You win 1 point \n")
        print(f"System's points are {sys_point} and Your points are {hum_point}")
    
    elif sys_guess=='w' and hum_guess=='g':
        sys_point=sys_point+1
        print(f"System's guess is {sys_guess}, Your guess is {hum_guess} \n")
        print("System wins 1 point \n")
        print(f"System's points are {sys_point} and Your points are {hum_point}")

    
    
    else:
        print("Unexpected Error occured and you have lost a chance")

    chance=chance+1
    print(f"{total_chances-chance} chances are left out of {total_chances} chances\n")

print("GAME OVER")
if sys_point==hum_point:
    print(f"Both system and You have {sys_point} and so the Game is Tied")
elif sys_point>hum_point:
    print(f"Better Luck Next Time !! System has {sys_point} and You have {hum_point}")
elif sys_point<hum_point:
    print(f"CONGRATULATIONS!!! YOU HAVE DEFEATED THE SYSTEM!! YOU HAVE {hum_point} WHILE SYSTEM HAS {sys_point}")
print(time.time())



        












  

