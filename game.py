import random

number = random.randint(1,10)
tries = 0
username = input("enter your name:")
username = username.strip()


print(f"Hello! {username}")
print("Would you like to play a game?")
print("1) yes")
print("2) no")

option = input("select your option:")
option = int(option)


if option==1:
    print("I'm thinking a numbr between 1 and 10")
    print("you have to guess the number in three tries")
    

    guess= input("guess a number:")
    guess= int(guess)
    tries+=1

    if guess>number:
        print ("guess lower...")
    if guess<number:
        print("guess higher...")



    while guess!=number and tries<3:
        guess= input("try again ")
        guess=int(guess)
        tries+=1



        if guess>number:
            print("guess lower")
        if guess<number:
            print("guess higher")


    if guess==number:
        print("you won")
        print(f"nuber of tries: {tries} ")
    else:
        print("you lost")


elif option==2:
    print("thankyou")
else:
    print("invalid input")    
