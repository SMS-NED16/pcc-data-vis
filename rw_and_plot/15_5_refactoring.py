from random import choice

class RandomWalk():
	"""A class to generate random walks"""

	def __init__(self, num_points=5000):
		"""Initialize attribures of a walk"""
		self.num_points = num_points

		#All walks start at (0, 0)
		self.x_values = [0]
		self.y_values = [0]
		self.directions = ([-1, 1])
		self.choices = list(range(0,5))

	def get_step(self):
		"""Decide which direction to move in and how far to go in this direction"""
		step_direction = choice(self.directions)
		step_choices = choice(self.choices)
		return step_direction * step_choices

	def fill_walk(self):
		"""Calculate all the points in the walk"""
		#Keep taking steps until the walk reaches the desired length
		while len(self.x_values) < self.num_points:
			x_step = get_step()
			y_step = get_step()

			#Reject moves that go nowhere
			if x_step == 0 and y_step == 0:
				continue

			#Calculate the next x and y values
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)