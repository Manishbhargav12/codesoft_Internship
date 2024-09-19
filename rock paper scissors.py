import random
my=["ROCK","PAPER","SCISSORS"]
def y():
    return(random.choice(my))
CPU= 0
user= 0
while True:
    try:
        User_Input=str(input("""Enter Your's Choice
        1.ROCK
        2.PAPER
        3.SCISSORS
        """))
        my=["ROCK","PAPER","SCISSORS"]
        def y():
            return(random.choice(my))
        User_Input=User_Input.upper()
        CPU1=y()
    #main code of Program
        if(CPU1==User_Input):
            print(f"CPU Choice :{CPU1} Tied")
        elif(User_Input=="PAPER" and CPU1=="ROCK"):
            print(f"CPU Choice :{CPU1}: You have Won")
            user=user+1
        elif(User_Input=="PAPER" and CPU1=="SCISSORS"):
            print(f"CPU Choice :{CPU1}: You have Lost")
            CPU=CPU+1
        elif(User_Input=="ROCK" and CPU1=="SCISSORS"):
            print(f"CPU Choice :{CPU1}: You have Won")
            user=user+1
        elif(User_Input=="ROCK" and CPU1=="PAPER"):
            print(f"CPU Choice :{CPU1}: You have Lost")
            CPU=CPU+1
        elif(User_Input=="SCISSORS" and CPU1=="PAPER"):
            print(f"CPU Choice :{CPU1}: You have Won")
            user=user+1
        elif(User_Input=="SCISSORS" and CPU1=="ROCK"):
            print(f"CPU Choice :{CPU1}: You have Lost")
            CPU=CPU+1
        # print(f"Your Score:{user}, Cpu Score:{CPU}")
        a=input("Do You Want To Play Again y/n ")
        if(a.lower()!="y"):
            break
    except Exception as e:
        print("Invalid Input")
print(f"Your Score:{user}, Cpu Score:{CPU}")
if(user<CPU):
    print("Oops You Lose")
elif(user>CPU):
    print("You won Champion")
elif(user==CPU):
    print("Tied")