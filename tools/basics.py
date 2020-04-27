import requests
from lxml import html

def url_to_tree(url):
	response = requests.get(url)
	tree = html.fromstring(response.content)
	return tree
