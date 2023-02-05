
import simulation
import visulization
from algorithms import *

def create_gif(name, rows, cols, alg):
	A = simulation.Airplane(rows, cols)
	time = A.simulateBoarding(alg)
	visulization.visulization(A.sateHistory, name)
	

if __name__ == '__main__':
	algs = [wma]
	algs_names = ["wma"]
	for i, alg in enumerate(algs):
		create_gif(f'{algs_names[i]}.gif', 30, 6, alg)
