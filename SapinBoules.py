import random

def drawXmasTree(baseLength):
    print(int((baseLength/2)) * " " + "*")

    isEven = baseLength % 2
    if isEven == 0 :
        lastStar = 1
    else:
        lastStar = 0

    for i in range(1, int(baseLength/2)):
        spaceBefore = baseLength/2-i
        spaceBetween = i*2-1
        print(int(spaceBefore)*" " + "*" + randomBaubles(spaceBetween) + "*")

    print(int(baseLength + lastStar)*"*")

    for i in range(1, 4):
        print(int((baseLength/2)-1)*" " + "***")

def randomBaubles(length):
    row = ""
    for i in range (0, length):
        baubleOrNot = random.random()
        if baubleOrNot > 0.98:
            baubleOrNot = "¤"
        elif 0.96 < baubleOrNot < 0.98:
            baubleOrNot = "~"
        elif 0.94 < baubleOrNot < 0.96:
            baubleOrNot = "o"
        elif 0.92 < baubleOrNot < 0.94:
            baubleOrNot = "x"
        elif 0.90 < baubleOrNot < 0.92:
            baubleOrNot = "8"
        else:
            baubleOrNot = " "
        row += baubleOrNot
    return row

if __name__ == "__main__":
    try:
        baseLength = int(input("Saisir la taille du sapin : "))
    except Exception as e :
        print("Erreur : saisir un chiffre")
        baseLength = 3

    drawXmasTree(baseLength)