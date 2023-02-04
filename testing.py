from simulation import Airplane
from visulization import visulization
from algorithms import *
import matplotlib.pyplot as plt


def main():
	algs = [sinp, wma, randomBoarding, southwest, split, btf, ftb]
	algs_names = ["sinp", "wma", "randomBoarding", "southwest", "split", "btf", "ftb"]
	alg_times = []
	for i, alg in enumerate(algs):
		A = Airplane(40, 6)
		alg_time = A.simulateBoarding(alg)
		print(f'The {alg} algorithm took {alg_time}')
		alg_times.append(alg_time)
	
	x = range(len(algs))
	plt.xticks(x, algs)
	plt.bar(range(len(algs)), alg_times, x_ticks = x)

if __name__ == '__main__':
	main()
			
	
