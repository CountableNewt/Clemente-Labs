# guessinggame.py
#   This program thinks of an animal that the user must guess
#   by: Sam Clemente

def main():
    animal = "Swan"
    print("I'm thinking of an animal")
    
    while True:
        guess = str(input("Guess what it is or type 'quit' to give up: ")).upper()
        if guess == animal.upper:
            print("You're right!")
            break
        elif guess == "QUIT":
            print("The answer was:", animal)
            print("Goodbye!")
            break
        else:
            print("No")
main()
