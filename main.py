import os



def parse(url):
	try:
		parsed_url_components = url.split('//')
		sublevel_split = parsed_url_components[1].split('/', 1)
		domain = sublevel_split[0].replace("www.", "")
		return domain
	except IndexError:
		print "Error reading URL"


data_path = os.path.expanduser('~')+"\AppData\Local\Google\Chrome\User Data\Default" #path to user's history database (Chrome)
files = os.listdir(data_path)

history_db = os.path.join(data_path, 'history')