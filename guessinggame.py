# guessinggame.py
#   This program thinks of an animal that the user must guess
#   by: Sam Clemente

def main():
    animal = "Swan"
    print("I'm thinking of an animal")
    
    while True:
        guess = str(input("Guess what it is or type a word beginning with 'q' to give up: ")).upper()
        if guess == animal.upper():
            print("You're right!")
            response = str(input("Do you like swans (y / n)? ")).upper()
            if response == "Y":
                print("Nice")
            elif response == "N":
                print("Wack")
            break
        elif guess[0] == "Q":
            print("The answer was:", animal)
            print("Goodbye!")
            break
        else:
            print("No")
main()
