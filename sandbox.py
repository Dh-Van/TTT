import numpy as np

# board = np.zeros((3, 3))
winConditions = []
counter = 0
for c in range(0, 8):
    newC = np.array(["" for _ in range(3**2)]).reshape(3, 3)
    if(c < 3):
        for i in range(3):
            newC[c][i] = "/"
    elif(c >= 3 and c < 6):
        for i in range(3):
            newC[i][c % 3] = "/"
    elif(c == 6):
        for i in range(3):
            newC[i][i] = "/"
    elif(c == 7):
        for i in range(3):
            newC[2 -  i][i] = "/"

    winConditions.append(newC)

testBoard = np.array([
    ["x", "x", "x"],
    ["x", "o", "x"],
    ["x", "x", "x"]
])

testBoard[testBoard == "x"] = "/"

for c in winConditions:
    check = c == testBoard
    result = np.all(check[0] == check[0][1]) and check[0][1] == True
    print(result)