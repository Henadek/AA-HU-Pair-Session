import unittest
from transformer import matrix_transformer
import numpy as np


class TestTransformer(unittest.TestCase):
	def testInputType(self):
		# checks if the input is a numpy array or a list
		# x = np.array([1,2,3])
		x = [1,2,3]
		y = [2,4,6]
		if type(x)==int or type(x)==np.ndarray:
			try:
				self.assertIsInstance(x, list)
			except:
				self.assertIsInstance(x, np.ndarray)
		elif type(y)==int or type(y)==np.ndarray:
			try:
				self.assertIsInstance(y, list)
			except:
				self.assertIsInstance(y, np.ndarray)

	def testInput(self):
		# checks if the list contains actual integers
		x = [1,2,3]
		y = [2,4,6]
		for i,j in zip(x,y):
			self.assertIsInstance(i, int)
			self.assertIsInstance(j, int)

	def testTransform(self):
		x = [1,'2',3]
		y = [2,4,6]
		result = np.array([[1,2],[2,4],[3,6]])
		np.testing.assert_array_equal(matrix_transformer(x,y),result)


if __name__=='__main__':
	unittest.main()