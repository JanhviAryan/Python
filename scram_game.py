import random
def game():
    a= ["book" , "cat" , "play" , "sing" , "dance" , "fan" , "home", "racket" , "laptop" ,"shoes"]
    word = random.choice(a)
    scram= ''.join(random.sample(word, len(word)))
    b = 5
    print("Unscramble the word:", scram)
    while b > 0:
        guess = input("Enter your word: ")

        if guess == word:
            print("Congratulation!! Correct")
            break
        else:
            b-= 1
            print("Wrong guess!! Attempts left:", b)
    if b == 0:
        print("You lost!! The correct word was:", word)
while True:
    game()
    ans = input("Do you want to play again? (yes/no): ")
    if ans != "yes":
        print("Thank you for playing!!")
        break