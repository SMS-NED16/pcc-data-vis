
import pygal
from pygal.style import LightSolarizedStyle

HEIGHT = 600
WIDTH = 700

points = [((-1, 0), (1, 5), (4, 3), (2, 6), (7, 2)), 
				((3, 6), (5, 4), (7, 10), (9, 8),(8, 6)),
          ((7, 11), (9, 6), (11, 13), (13, 6))]

types = ['A numbers', 'B numbers', 'C numbers']

xy_chart = pygal.XY(height=HEIGHT, width=WIDTH, style=LightSolarizedStyle,
                    stroke=True, show_legend=True,
                    human_readable=True, fill=False, show_dots=True,
                    dot_size=4)                  
xy_chart.title = 'Points and Types'
xy_chart.x_labels = map(lambda x: str(x) if not x % 3 else '', range(20))
for type, point in zip(types, points):
    xy_chart.add(type, point)
xy_chart.render_to_file('xy_chart.svg')