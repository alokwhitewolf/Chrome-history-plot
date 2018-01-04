import sqlite3
import os
import operator
from collections import OrderedDict
import pylab as plt
#import matplotlib.pyplot as pl

def parse(url):
	try:
		parsed_url_components = url.split('//')
		sublevel_split = parsed_url_components[1].split('/', 1)
		domain = sublevel_split[0].replace("www.", "")
		return domain
	except IndexError:
		print "Error reading URL"


data_path = os.path.expanduser('~')+"/Library/Application Support/Google/Chrome/default" #path to user's history database (Chrome)
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'History')
print history_db

#db querying
c = sqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)

results = cursor.fetchall() #tuple

sites_count = {} #dict

for url, count in results:
	url = parse(url)
	if url in sites_count:
		sites_count[url] += 1
	else:
		sites_count[url] = 1

sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))

index = [1,2,3, 4, 5, 6, 7, 8, 9, 10]

count = list(sites_count_sorted.values())[:10]

LABELS = list(sites_count_sorted.items())[:10]
LABELS = [LABELS[i][0].encode('utf-8') for i in range(len(LABELS))]
plt.bar((index), count)
plt.xticks(index, LABELS,rotation=15)
#plt.xlim([0,len(LABELS)])
plt.axis('tight')
plt.show()