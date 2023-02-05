#Algorithms from the paper:
# https://towardsdatascience.com/a-simulation-framework-to-analyze-airplane-boarding-methods-410def726350
# Super Ideal Not Practical (SINP)
# Window-Middle-Aisle (WMA)
# Random
# Southwest
# Back-To-Front (BTF)
# Front-To-Back (FTB)

import numpy as np
import random


# the order starts with window seats and moves to aisle
# for each group, order starts with the back and moves to front
def sinp (nOfRows, nOfColumns):
	boardingQueue = []

	columnOrder = []

	for i in range(int(nOfColumns / 2)):
		columnOrder.append(i)
		columnOrder.append(nOfColumns-1-i)

	for column in columnOrder:
		for row in reversed(range(nOfRows)):
			boardingQueue.append((row, column))

	#print(boardingQueue)
	return boardingQueue


# the order starts with window seats and moves to aisle
# for each group, order is random
def wma(nOfRows, nOfColumns):
	boardingQueue = []

	columnGroups = []
	seatGroups = []

	for i in range(int(nOfColumns / 2)):
		group = []
		group.append(i)
		group.append(nOfColumns-1-i)
		columnGroups.append(group)
	

	for group in columnGroups:
		groupSeats = []
		for column in group:
			for row in range(nOfRows):
				groupSeats.append((row, column))
		groupSeats = random.sample(groupSeats, len(groupSeats))
		boardingQueue.extend(groupSeats)
	return boardingQueue


# completely random
def randomBoarding (nOfRows, nOfColumns):
	boardingQueue = []
	for column in range(nOfColumns):
		for row in range(nOfRows):
			boardingQueue.append((row, column))
	boardingQueue = random.sample(boardingQueue,len(boardingQueue))
	return boardingQueue

# people pick their seats, so they pick window or isle first, and once they are all full, they sit in middle seats.
def southwest (nOfRows, nOfColumns):
	boardingQueue = []

	windowColumns = [0,nOfColumns-1]

	aisleLeft = int(nOfColumns / 2) - 1
	aisleColumns = [aisleLeft, aisleLeft + 1]

	middleSeats = []
	aisleSeats = []
	windowSeats = []

	for column in range(nOfColumns):
		for row in range(nOfRows):
			if (column in windowColumns):
				windowSeats.append((row, column))
			elif (column in aisleColumns):
				aisleSeats.append((row, column))
			else:
				middleSeats.append((row, column))



	sidesSeats = windowSeats + aisleSeats
	boardingQueue = random.sample(sidesSeats,len(sidesSeats)) + random.sample(middleSeats,len(middleSeats))
	return boardingQueue

#This will divide the rows into n boarding groups
def split(nOfRows, nOfGroups):
	return np.array_split(range(nOfRows), nOfGroups)


# rows are divided into boarding groups
# groups in the back boards first
def btf(nOfRows, nOfColumns, nOfGroups = 3):

	groupedRows = split(nOfRows, nOfGroups)
	boardingQueue = []
	groupedSeats = []	

	for boardingGroup in reversed(groupedRows):
		groupSeats = []
		for column in range(nOfColumns):
			for row in boardingGroup:
				groupSeats.append((row, column))
		groupSeats = random.sample(groupSeats, len(groupSeats))
		boardingQueue.extend(groupSeats)
	return boardingQueue


# rows are divided into boarding groups
# groups in the front boards first
def ftb(nOfRows, nOfColumns, nOfGroups = 3):

	groupedRows = split(nOfRows, nOfGroups)
	boardingQueue = []
	groupedSeats = []	

	for boardingGroup in groupedRows:
		groupSeats = []
		for column in range(nOfColumns):
			for row in boardingGroup:
				groupSeats.append((row, column))
		groupSeats = random.sample(groupSeats, len(groupSeats))
		boardingQueue.extend(groupSeats)
	return boardingQueue
