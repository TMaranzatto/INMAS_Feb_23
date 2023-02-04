
class Airplane:
    def __init__(self, n_rows, n_cols):
        self.rows = n_rows
        self.cols = n_cols

        self.seating = [[(i,j) for i in range(n_cols)] for j in range(n_rows)]

    def simulateBoarding(self, boardingProcedure):
        return None
    

def randomBoarding(seatingArrangement):
    from random import shuffle
    #assume seatingArrangement is a 2D array of i-j pairs
    #where i is the col, and j is the row
    seats = [item for sublist in seatingArrangement for item in sublist]
    shuffle(seats)
    return seats


A = Airplane(100, 6)
print(randomBoarding(A.seating))
