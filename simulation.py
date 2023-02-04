from random import shuffle
import numpy as np
import copy

class Airplane:
    def __init__(self, n_rows, n_cols):
        self.rows = n_rows
        self.cols = n_cols

        #index seating by seating[row][col]
        self.seating = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        self.sateHistory = []

    def rowHelper(self, currentRow, passenger):
        #Time to get to seat = sum(people to move over)
        desiredSeat = passenger[0]
        climbable = None
        if desiredSeat < self.cols//2:
            desiredSeat = self.cols - (desiredSeat + 1)
            climbable = self.seating[currentRow][:self.cols//2:-1]
        else:
            climbable = self.seating[currentRow][self.cols//2:]
        time = sum(climbable[:desiredSeat])
        
        return [time, passenger]

    def next(self, boardQueue, aisle):
        #to start, move one timestep at a time
        #then we can generalize later
        for currentRow, cell in reversed(list(enumerate(aisle))):
            print(cell)
            if cell == None:
                continue
            #ASSUME PASSENGERS ARE TUPLES OF SEAT LOCATIONS
            if type(cell) == list:
                if cell[0] == 0:
                    self.seating[cell[1][0]][cell[1][1]] = 1
                    aisle[currentRow] = None
                else:
                    cell[0] -= 1
                continue
            #if cell is in the current row, start a countdown, or move person to seat
            if cell[0] == currentRow:
                aisle[currentRow] = self.rowHelper(currentRow, cell)
                continue

            if currentRow != (self.rows - 1):
                if aisle[currentRow + 1] == None:
                    aisle[currentRow] = None
                    aisle[currentRow + 1] = cell
                continue

        if aisle[0] == None and len(boardQueue) != 0:
            aisle[0] = boardQueue.pop(0)
        
        tempSeat = copy.deepcopy(self.seating)
        passAisle = [2 if i != None else 0 for i in aisle]
        for i, row in enumerate(tempSeat):
            row.insert(self.cols//2, passAisle[i])
        self.sateHistory.append(np.array(tempSeat))
        return boardQueue, aisle

    

    def simulateBoarding(self, boardingProcedure):
        boardQueue = boardingProcedure(self.rows, self.cols)
        aisle = [None for _ in range(self.rows)]
        totalTime = 0
        
        def notEmpty(lst):
            return not all( [True if i == None else False for i in lst])
        #for _ in range(30):
        while(len(boardQueue) > 0 or notEmpty(aisle)):
            boardQueue, aisle = self.next(boardQueue, aisle)
            totalTime += 1
        return totalTime


def boardRandom(n, m):
    seats = [(i,j) for i in range(n) for j in range(m)]
    shuffle(seats)
    return seats

A = Airplane(40, 6)
A.simulateBoarding(boardRandom)


from visulization import visulization
visulization(A.sateHistory)