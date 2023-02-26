displayGrid = [["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
               ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
               ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
               ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]]

length = 0
charactersLeft = 0
currentWord = 0

# User input for the message.
message = input("Please enter a message. \n")
messageArray = message.split()

# Displaying the grid.
for loop in displayGrid:
    string = ""
    for eachLine in loop:
        string = string + "   " + eachLine
    print(string, "\n")

# Blank checker.
rowBlank = 0
columnBlank = 0
while displayGrid[rowBlank][columnBlank] == "B":
    # Calculating whether the word will fit.
    row = 0
    column = 0
    pos = 0
    enoughSpace = False
    wordLength = len(messageArray[currentWord])
    while charactersLeft < wordLength:
        while enoughSpace != True:
            if displayGrid[row][pos] == "B":
                charactersLeft += 1
                pos += 1
                if charactersLeft == wordLength:
                    enoughSpace = True
            else:
                if row < 4:
                    row += 1
                    pos = 0
                    charactersLeft = 0
                else:
                    print("Message is too long to be displayed.")