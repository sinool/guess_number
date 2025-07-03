import os
def get_num() ->int :
    while True :
        try:
            guess = int(input("now guess 😃 : "))
        except ValueError :
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Enter a number 😡")
        else :
            return guess