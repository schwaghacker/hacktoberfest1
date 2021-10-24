#Stone,Paper,Scissor game

import random
lst = ['t','p','s']

hp=0
cp=0
left=10

print("Welcome to the stone paper scissor game")
name = input("enter your name: ")

print("Enter t for stone\n enter p for paper\n and enter s scissor")


for _ in range(left):
    inp=input("enter your choice: ")
    ran = random.choice(lst)


    if inp == ran:
        print("You both got tied")

    elif inp=="t" and ran=="s":
        hp += 1
        print(name + " choose stone and the computer choose scissor")
        print("You won!!")


    elif inp=="t" and ran=="p":
        cp += 1
        print(name + " choose stone and the computer choose paper")
        print("You loose")


    elif inp=="p" and ran=="t":
        hp += 1
        print(name + " choose paper and the computer choose stone")
        print("You won!!")

    elif inp=="p" and ran=="s":
        cp += 1
        print(name + " choose paper and the computer choose scissor")
        print("You lose")

    elif inp=="s" and ran=="p":
        hp += 1
        print(name + " choose scissor and the computer choose paper")
        print("you won!!")

    elif inp=="s" and ran=="t":
        cp += 1
        print(name + " choose scissor and the computer choose stone")
        print("You lose")

    else:
        print("wrong input")

print("Game over!")

print(f" {name} points {hp} ")

print(f"Computer points {cp}")

if hp==cp:
    print("You both got tied")

elif hp>cp:
    print(name + " wins!")

elif cp>hp:
    print("Computer wins!!")
