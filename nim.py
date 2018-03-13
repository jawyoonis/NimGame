import random
import time
import sys

def picking_ball():
    number_ball= int(input("how many ball you want to pick:"))
    if number_ball >=15:
        return number_ball
    else:
        print("wrong input")



def player_one():
    user= int(input("pick the number of balls between 0 and 4: "))
    if user >0 and user <= 4:
        return user
    else:
        print("wrong input!!")



def player_two():
    user_two= random.randint(0, 4)
    if user_two >0 and user_two <=4:
        return user_two
    else:
        print("invalid number")




def main():
    print("welcome to nim game!!!")
    count= picking_ball()
    time.sleep(2)
    print("you have " + str(count) + " balls to start the game!")
    while count > 0:

        print("user's turn")
        time.sleep(1)
        user_input= player_one()
        count=int(count)-user_input
        print("user picked " + str(user_input) + " balls")
        if count <= 0:
            print("user has won")
            sys.exit()
        time.sleep(2)
        print("computer's turn")
        computer_input= player_two()
        count= int(count)-int(computer_input)
        print("computer picked " + str(computer_input) + " balls")
        if count <= 0:
            print("computer has won")
            sys.exit()
        time.sleep(2)
        print("remainider " + str(count))




























if __name__ == "__main__":
    main()
