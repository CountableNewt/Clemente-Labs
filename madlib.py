#madlib.py
#   Creates a MadLib with user input
#   by: Sam Clemente

def main():
    noun = str(input("Enter a noun: "))
    verb = str(input("Enter a verb: "))
    adj = str(input("Enter an adjective: "))
    place = str(input("Enter a place: "))

    print("The", adj, noun, verb, "at", place)

main()
