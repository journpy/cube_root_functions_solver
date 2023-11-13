from cube_root_functions import CubeRootFunctions


class CubeRootFunctionsLoop(CubeRootFunctions):
	""" Inherits attributes and methods from class CubeRootFunctions."""


	def __init__(self, a, c, h, k):
		""" Initialise attributes of the parent class."""
		super().__init__(a, c, h, k)


	def main_loop(self):
		"""Main program loop"""
		while True:
			self.a = input("Enter a: ")
			if self.a == 'q' or self.a == 'Q':
				break
			self.c = input("Enter c: ")
			if self.c == 'q' or self.c == 'Q':
				break
			self.h = input("Enter h: ")
			if self.h == 'q' or self.h == 'Q':
				break
			self.k = input("Enter k: ")
			if self.k == 'q' or self.k == 'Q':
				break
			crfl = CubeRootFunctionsLoop(self.a, self.c, self.h, self.k)
			crfl.convert_to_float()
			crfl.plot_and_show_graph()



