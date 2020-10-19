# guessinggame.py
#   This program thinks of an animal that the user must guess
#   by: Sam Clemente

def main():
    animal = "Swan"
    print("I'm thinking of an animal")
    
    while True:
        guess = str(input("Guess what it is: "))
        if guess == animal:
            print("You're right!")
            break
        else:
            print("No")
main()
