import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def createLangComparisonGraph(langs):
	"""Creates a bar graph comparing the total repositories
	for each language"""
	repo_counts = []
	my_style = LS("#333366", base_style=LCS)
	for lang in langs:
		repo_counts.append(lang.response_dict['total_count'])
	chart = pygal.Bar(style=my_style)
	chart.title = "Total GitHub Repo Counts for Programming Languages, 2018"
	chart.x_labels = languages
	chart.add('', repo_counts)
	chart.render_to_file("renders/language-comp.svg")

def createReposGraph(langObj):
	my_config = pygal.Config()
	my_config.show_legend = False
	my_config.x_label_rotation = 45
	my_config.title_font_size = 24
	my_config.label_font_size = 14
	my_config.major_label_size = 18
	my_config.truncate_label = 15
	my_config.width = 1000
	my_config.y_label = "GitHub Repos"

	my_style = LS("#333366", base_style=LCS)
	chart = pygal.Bar(my_config, style=my_style)
	chart.title = "Most-Starred " + langObj.name + " Projects on GitHub"
	chart.x_labels = langObj.repo_names
	chart.add('', langObj.repo_dicts)
	chart.render_to_file("renders/" + langObj.name + ".svg")
