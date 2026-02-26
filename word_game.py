import random
def game():
    num = random.randint(1,100)
    a = 0
    while(True):
        g = int(input("enter your guess: "))
        a+=1
        if(g > num):
            print("Too high!! enter again")
        elif(g < num):
            print("Too low!! enter again")
        else:
            print("Correct")
            print("Total attempt taken:  ",a)
            break
while True:
    game()
    ans = input("Do you want to play again? (yes/no):  ")
    if ans != "yes":
        print("Thank you for playing")
        break