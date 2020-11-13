# fave-color.py
#   User may enter their favorite color, but if I don't like it
#   they will be roasted senselessly
#   by: Sam Clemente

colorList = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "INDIGO", "PURPLE",
             "VIOLET", "CYAN", "MAGENTA", "TEAL", "PINK", "FUCHSIA"]

def showTitle():
    pass

def askForColor():
    return "RED"

def confirmColor():
    return True

def containsElement():
    return True

def praiseUser():
    pass

def ridiculeUser():
    pass

def main():
    showTitle()

    while True:
        askForColor()
        if confirmColor():
            break

    if containsElement():
        praiseUser()
    else:
        ridiculeUser()

main()
