import random

option=["rock","paper","scissor"]
computer=random.choice(option)
player=input("your choice of option:")
print(f"player:{player}")
print(f"computer:{computer}")
if (player==computer):
    print("its a tie")
elif ((player=="rock" and computer=="scissor")or(
    player=="scissor" and computer=="paper")or
      (player=="paper" and computer=="rock ")):
    print("you win")
elif player in option:
    result="computer win"
else:
    print("invalid inputs")
