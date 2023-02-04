from random import shuffle

class Airplane:
    def __init__(self, n_rows, n_cols):
        self.rows = n_rows
        self.cols = n_cols

        self.seating = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        self.currentState = [[0 for _ in range(n_cols + 1)] for _ in range(n_rows)]

    def rowHelper(self, currentRow, passenger):
        #move people out of the way if they need to be
        #for now just move the person to the seat they are assigned to
        self.seating[passenger[0]][passenger[1]] = 1
        

    def next(self, boardQueue, aisle):

        #to start, move one timestep at a time
        #then we can generalize later
        for currentRow,cell in reversed(list(enumerate(aisle))):
            print(currentRow, cell)
            if cell == None:
                continue
            if cell[0] == currentRow:
                self.rowHelper(currentRow, cell)
            if currentRow != self.rows - 1:
                if aisle[currentRow + 1] == None:
                    aisle[currentRow] = None
                    aisle[currentRow + 1] = cell
        if aisle[0] == None:
            aisle[0] = boardQueue.pop(0)
        return None

    def simulateBoarding(self, boardingProcedure):
        boardQueue = boardingProcedure(self.rows, self.cols)
        aisle = [None for _ in range(self.rows)]
        totalTime = 0
        for i in range(100):
            self.next(boardQueue, aisle)
            totalTime += 1
            print(boardQueue)
            print()
            print(aisle)
            print()
            print()
        return totalTime


def boardRandom(n, m):
    seats = [(i,j) for i in range(n) for j in range(m)]
    
    shuffle(seats)
    return seats

A = Airplane(4, 2)
A.simulateBoarding(boardRandom)
