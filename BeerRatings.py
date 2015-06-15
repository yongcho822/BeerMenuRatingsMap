
# coding: utf-8

# In[140]:

from bs4 import BeautifulSoup
from time import sleep
import requests
import csv

pagenumberslist = range(0, 3801, 25)

URLS = ["http://www.beeradvocate.com/beer/reviews/?start={0}&view=all&order=dateD".format(i) for i in pagenumberslist]

with open("BeerRatings.csv", "w") as f:
    headers = ["Beer name", "Brewery", "Rating"]
    writer = csv.writer(f, delimiter = ",")
    writer.writerow(headers)

    for i in URLS:
        for row in BeautifulSoup(requests.get(i).text).find("div",{"id":"ba-content"})\
        .find("table", {"width":"100%"}).find_all('tr')[3:]:
            tds = row('td')
            Beername = tds[1].a.b.string.encode('utf-8')
            Brewery = tds[1].a.find_next_sibling('a').string.encode('utf-8')
            Rating = tds[3].b.string.encode('utf-8')
            
            writer.writerow([Beername, Brewery, Rating])
            
print 'We\'re done here.'
