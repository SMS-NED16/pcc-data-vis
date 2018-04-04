import requests

class LangData():
	"""A simple class to store a programming language's name and 
	GitHub repository data fetched via the GitHub API"""
	def __init__(self, identifier):
		self.identifier = identifier
		self.name = identifier.upper()
		self.response_dict = {}
		self.repo_names = []
		self.repo_dicts = []
		self.getData()

	def createURL(self):
		"""Use identifier to create target URL for GitHubAPI call"""
		target_url = "https://api.github.com/search/repositories?q=language:"
		target_url += self.identifier
		target_url += "&sort=stars"
		return target_url


	def printSummary(self):
		"""Print total GitHub Repos for language and total number of 
		repos for which data is received"""
		"""Mostly a sanity check"""
		print("Total GitHub Repos for " + str(self.name), 
			self.response_dict['total_count'])
		print("Repos received in response:", len(self.response_dict['items']))

	def populateData(self):
		"""Populate names, repo count, description, and url for use with Pygal"""
		for repo in self.response_dict['items']:
			try:
				repo_name = repo['name']
				repo_stars = repo['stargazers_count']
				repo_desc = str(repo['description'])
			except UnicodeDecodeError:
				print("Error decoding data for "+ self.name)
			else:
				self.repo_names.append(repo_name)
				tempDict = {
					'value': repo_stars,
					'label': str(repo_desc),
					'xlink': repo['html_url']
				}
				self.repo_dicts.append(tempDict)


	def getData(self):
		"""Fetch and store data for language from GitHub by making an API Call"""
		url = self.createURL()
		print("\nFetching data for " + self.name)
		response = requests.get(url)
		if (response.status_code == 200):
			print("API request for " + self.name + " successful")
			self.response_dict = response.json()
			self.printSummary()
			self.populateData()
		else:
			print("Could not fetch data for " + self.name)

