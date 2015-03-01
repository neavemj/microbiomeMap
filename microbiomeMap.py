__author__ = 'neavemj'


## use basemap in python to create a sampling map for Microbiome project ##
# Matthew J. Neave 5.2.2015

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# function to change degrees to decimal degrees if needed
# My co-ordinates are given as degrees then decimal minutes. Seconds are not given so I've commented then out.

print '*** creating map ***'

# the ll and ur mean lower-left corner, upper-right corner etc. for zooming on a region

map = Basemap(projection = 'merc', lat_0 = 0, lon_0 = 106, resolution = 'l', area_thresh = 1000, llcrnrlon=20, llcrnrlat=-50, urcrnrlon=210, urcrnrlat=40)

map.drawcoastlines(linewidth=0.5)
map.drawcountries(linewidth=0.5)
map.fillcontinents(alpha=0.5)
map.drawmapboundary()


map.drawmeridians(np.arange(0, 360, 30), labels=[False, False, False, True], linewidth=0.1)
map.drawparallels(np.arange(-90, 90, 30), labels=[False, True, False, False], linewidth=0.1)

pVerr_known_file = open("/Users/neavemj/microbiome/subprojects/4.map/p.verrucosaKnownDist.csv")
pVerr_known = pd.DataFrame.from_csv(pVerr_known_file)
a,b = map(list(pVerr_known["longitude"]), list(pVerr_known["latitude"]))

#spist_known_file = open("/Users/neavemj/microbiome/subprojects/4.map/s.pistillataKnownDist.csv")
#spist_known = pd.DataFrame.from_csv(spist_known_file)
#a,b = map(list(spist_known["longitude"]), list(spist_known["latitude"]))

sites_file = open("/Users/neavemj/microbiome/siteCoordinates.txt")
sites = pd.DataFrame.from_csv(sites_file, sep='\t')
c,d = map(list(sites["Longitude"]), list(sites["Latitude"]))

sitesPverr_file = open("/Users/neavemj/microbiome/siteCoordinatesPverr.txt")
sitesPverr = pd.DataFrame.from_csv(sitesPverr_file, sep='\t')
e,f = map(list(sitesPverr["Longitude"]), list(sitesPverr["Latitude"]))

map.plot(a, b, 'bo', markersize=20, markeredgecolor='none')
map.plot(c, d, 'ro', markersize=5)
map.plot(e, f, 'ro', markersize=5)

plt.savefig("spistMap.pdf", format='pdf')

plt.show()

