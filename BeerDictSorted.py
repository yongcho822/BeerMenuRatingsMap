
# coding: utf-8

# In[140]:

import csv
from collections import OrderedDict

od = OrderedDict()

with open("BeerRatings.csv", "rb") as f, open("BeerDictSorted.csv", "w") as out:
    r = csv.reader(f)
    wr = csv.DictWriter(out, fieldnames = ["Beer", "Brewery", "Rating"])
    throwawayfields = next(r)
    for row in r:
        Beer, Brewery, Rating = row
        od.setdefault(Beer, dict(Beer=Beer, Brewery=Brewery, Rating=[]))
        od[Beer]["Rating"].append(Rating)
    wr.writeheader()

    for k,v in od.items():
        floats = map(lambda x:float(x), od[k]["Rating"])
        numb_of_ratings = len(od[k]["Rating"])
        od[k]["Rating"] = "{0:.2f}".format(sum(floats)/numb_of_ratings)
        wr.writerow(v)