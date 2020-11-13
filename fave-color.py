# fave-color.py
#   User may enter their favorite color, but if I don't like it
#   they will be roasted senselessly
#   by: Sam Clemente

colorList = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "PURPLE",
             "VIOLET", "CYAN", "MAGENTA", "TEAL", "PINK", "FUCHSIA"]

userColor = ""

def showTitle():
    print("Color Preference Evaluator\n\nTell me your favorite color\nbut if I don't like it you will be roasted senselessly")

def askForColor():
    return input("Enter your favorite color: ").strip().upper()

def confirmColor():   
    confirm = input("\nYou selected {0}. Is this correct? (Y/N) ".format(userColor)).upper()
    if confirm == "Y":
        return True
    else:
        return False
        
def containsElement():
    for i in range(len(colorList)):
        if userColor == colorList[i]:
            return True
    return False

def praiseUser():
    print("\nCongrats, you picked a good color.\nThis time.")

def ridiculeUser():
    print("\nYou picked {0}!?!?!?\nPfft, nerd.\nI doubt that's even a *REAL* color.".format(userColor))

def main():
    global userColor
    
    showTitle()

    while True:
        userColor = askForColor()
        if confirmColor():
            break

    if containsElement():
        praiseUser()
    else:
        ridiculeUser()

main()
