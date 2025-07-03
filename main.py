from src.utils.get import get_num
import random, sys, threading, os
from time import sleep
guess=0
load = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]

def main():
    game=True
    while game :
        point=100
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in load:
            
            sys.stdout.write("\r Let me choose a number between 1 to 100 "+i+"\r")
            sleep(0.2)
            sys.stdout.flush()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"now guess in 10 rounds😃\n POINTS: {point}")
        number=random.randint(1, 100)
        guess=get_num()

        while number != guess:
            point -= 10
            os.system('cls' if os.name == 'nt' else 'clear')
            if guess > number :
                print(f"choose lower than that😎\n POINTS: {point}")
            if guess < number :
                print(f"choose higher than that😎\n POINTS: {point}")
            if guess == number :
                break
            if point <= 0 :
                break
            guess= get_num()

        os.system('cls' if os.name == 'nt' else 'clear')
        if point == 0 :
            print("YOU LOSE! 🤣 ")
            
        else:
            print(f"WELL DONE😏  \nI choose number: {number}✅")
        r=input("Start again ?(y/n) ")
        if r=="n" : 
            game=False 
            print("BYE! 👋")

if __name__ == "__main__" :
    main()