from simulation import Airplane
import numpy as np


def test_next():
	num_rows = 100
	num_cols = 6
	plane = Airplane(num_rows, num_cols)
	boardingQ = [[(i,j) for i in range(num_cols)] for j in range(num_rows)]
	aisleList = [None]*num_rows
	aisleList.append(boardingQ.pop()
	plane.next(boardingQ, aisle_list)
	assert len(aisleList) == 1
	plane.next(boardingQ, aisle_list)
	assert Airplane.seating_matrix[0,0] == 1
	assert (0,0) not in boardingQ and (0,0) not in aisleList
	for i in range(10):
		plane.next(boardingQ, aisle_list)
		print(boardingQ, aisle_list)
	
def test_nearly_empty():
	num_rows = 100
	num_cols = 6
	plane = Airplane(num_rows, num_cols)
	boardingQ = [(50, i) for i in range(6)]
	aisleList = [None]*num_rows
	num_nexts = 0
	too_long = False
	while True:
		plane.next(boardingQ, aisle_list)
		num_nexts += 1
		if num_nexts > 1_000_000:
			too_long = True
			break
		if len(boardingQ)>0:
			continue
		for i in range(6):
			if (50, i) in aisleList:
			continue
		break
	assert not too_long

def main():
	test_nearly_empty()
	test_next()

if __name__ == '__main__':
	main()
			
	
