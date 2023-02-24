import matplotlib.pyplot as plt
import numpy as np

class CubeRootFunctions:
	""" Model Cube Root Functions."""


	def __init__(self, a, c, h, k):
		""" Initialise attributes of cube root functions."""
		self.a = a
		self.c = c
		self.h = h
		self.k = k
	

	def convert_to_float(self):
		""" Return float values of user input."""
		self.a = float(self.a)
		self.c = float(self.c)
		self.h = float(self.h)
		self.k = float(self.k)
		return self.a, self.c, self.h, self.k


	def style_graph(self):
		"""Style graph."""
		plt.style.use('ggplot')
		plt.xlabel('x', c='b', loc='right')
		plt.ylabel('y', c='b', loc='top')
		plt.grid(True, linestyle=':')


	def plot_and_show_graph(self):
		""" Plot and display graph."""
		x = np.linspace(-20, 20, 50)
		y = self.a*np.cbrt((self.c*x) - self.h) + self.k
		crf = CubeRootFunctions(self.a, self.c, self.h, self.k)
		crf.style_graph()
		plt.title(f"Graph of y = ({self.a}* cbrt({self.c}x - {self.h})) + "
				f"{self.k}", c='red', fontsize=12, fontweight='bold')
		plt.plot(x, y, color='red')
		plt.text(min(x), max(y), 
				f"Inflection point: ({self.h}, {self.k})", c='b')
		plt.show()