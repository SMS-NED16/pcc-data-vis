import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

#Status code f o200 indiates a successful response
print("Status code: " , r.status_code)

#Stroe the API response in a variable
response_dict = r.json()

#Process results
print(response_dict.keys())

print("Total Repositories: ", response_dict['total_count'])

#Explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned", len(repo_dicts))

#Examine the first repository
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

#Extracting values for some keys in the first repository
# print("\nSelected information about each repository")
# for repo_dict in repo_dicts:
# 	try:
# 		print("\n******************************")
# 		print("Name", repo_dict['name'])
# 		print("Onwer:", repo_dict['owner']['login'])
# 		print("Stars: ", repo_dict['stargazers_count'])
# 		print("Repository: ", repo_dict['html_url'])
# 		print("Created: ", repo_dict['created_at'])
# 		print("Updated: ", repo_dict['updated_at'])
# 		print("Description: ", repo_dict['description'])
# 	except UnicodeEncodeError:
# 		print("Could not read data for " + repo_dict['name'])

#Visualiization
names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#Creating config object to pass to pygal Bar
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_soze = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

#Plotting bar chart with Pygal
my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)
chart.x_labels = names
chart.add('', stars)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.render_to_file('python_repos.svg')

#Creating a new pygal bar chart
names, plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	try:
		count = repo_dict['stargazers_count']
		desc = repo_dict['description']
	except AttributeError:
		print("Some bullshit error")
	else:
		plot_dict = {
			'value': int(repo_dict['stargazers_count']),
			'label': str(repo_dict['description']),
			'xlink': repo_dict['html_url']
		}
	plot_dicts.append(plot_dict)

chart_2 = pygal.Bar(my_config, style=my_style)
chart_2.title = "Python Projects"
chart_2.x_labels = names
chart_2.add('', plot_dicts)
chart_2.render_to_file("graph_descriptions.svg")
