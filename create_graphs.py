
import simulation
import visulization
import algorithms as algs

def create_gif(name, rows, cols, alg):
	A = simulation.Airplane(rows, cols)
	time = A.simulateBoarding(alg)
	visulization.visulization(A.sateHistory, name)
	


if __name__ == '__main__':
	create_gif('random.gif', 30, 6, algs.randomBoarding)
