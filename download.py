import requests

def download(url):
	path = url.split('/')[-1]
	with open(path, 'wb') as f:
		f.write(requests.get(url).content)
	return path 
