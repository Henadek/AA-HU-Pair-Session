import numpy as np

def matrix_transformer(x, y):
	try:
		rez = np.array([x,y]).transpose()
		return rez
	except Exception as e:
		return e

a = [1,2,3]
b = [4,5,6]

matrix_transformer(a,b)
