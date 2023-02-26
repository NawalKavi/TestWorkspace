displayGrid = [["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
               ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
               ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
               ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]]

length = 0
charactersLeft = 0

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
    wordLength = len(messageArray[0])
    while charactersLeft < 0:
        if displayGrid[row][pos] == "B":
            charactersLeft += 1
            pos += 1
        elif displayGrid[[row][pos] != "B" and row < 4:
            row += 1