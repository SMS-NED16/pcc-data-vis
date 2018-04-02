import json
import pygal
from pygal_maps_world.i18n import COUNTRIES
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle


for country_code in sorted(COUNTRIES.keys()):
	print(country_code, COUNTRIES[country_code])

#load the data into a list
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

#Build a dictionary of population data
cc_populations = {};
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population

#Group the countres into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10 * (10 ** 6):
		cc_pops_1[cc] = pop
	elif pop < 10 ** 9:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

#see how many countries are in each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle("#336699")
wm = World(style=wm_style)
wm.title = "World Population in 2010 by Country"
wm.add("0 - 10M", cc_pops_1)
wm.add("10M - 1bn", cc_pops_2)
wm.add(">1bn", cc_pops_3)

wm.render_to_file('world_population.svg')