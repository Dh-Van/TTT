import numpy as np

class Main:

    counter = [0, 0, 0]

    def init(self):
        board = np.array([0 for _ in range(3**2)]).reshape(3, 3)
        # print(board, end="\n\n")
        
        # board[0][0] = 1
        # board[0][1] = 0
        # board[0][2] = 0
        
        # board[1][0] = 0
        board[1][1] = 1
        # board[1][2] = 0
        
        # board[2][0] = 0
        # board[2][1] = 0
        # board[2][2] = 0
        
        # print(board, end="\n\n")
        return board

    def gen(self, board, lastNum):

        if(lastNum == 2):
            lastNum = 1
        elif(lastNum == 1):
            lastNum = 2

        if(self.counter[2] >= 3**2):
            return

        if(self.counter[0] >= 3):
            self.counter[0] = 0
            self.counter[1] += 1
        if(self.counter[1] >= 3):
            self.counter[1] = 0

        newb = np.copy(board)
        newb[self.counter[0]][self.counter[1]] = 2
        # print(newb)
        for idx, num in np.ndenumerate(newb):
            if(num != 0):
                continue
            newb[idx[0]][idx[1]] = lastNum
            print(newb)
            self.gen(newb, lastNum)

        self.counter[0] += 1
        self.counter[2] += 1
        print("\n\n\n")
        self.gen(board, 1)

m = Main()
b = m.init()
m.gen(b, 1)    