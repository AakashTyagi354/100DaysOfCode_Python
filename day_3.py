

print("welcome to Treasur Island")
print("Your misson is to find the treasure")
choice1 = input("You are at crossroad, where do you wantto go? Type 'left' or 'right': ").lower();

if choice1 == "left":
   choice2 =  input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for boat. Type 'swim' to swim across. ").lower();
   if choice2 == "wait":
       choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. one red , one yellow and one blue which colour do you choose!. ").lower();
       if choice3 == "red":
           print("It is room full of fire. Game Over!!");
       elif choice3 == "yellow":
           print("You found a treasure! You Win!!")
       elif choice3 == "blue":
            print("It is room full of fire. Game Over!!");
       else:
            print("It is room full of fire. Game Over!!");
   else:
       print("You got attacked by an angrytrout. Gave over!!")
else:
    print("game over!!")


