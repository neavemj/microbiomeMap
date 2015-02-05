__author__ = 'neavemj'


## use basemap in python to create a sampling map for Microbiome project ##
# Matthew J. Neave 5.2.2015

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print '*** creating map ***'

# the ll and ur mean lower-left corner, upper-right corner etc. for zooming on a region

map = Basemap(projection = 'merc', lat_0 = 0, lon_0 = 0, resolution = 'l', area_thresh = 1000, llcrnrlon=-136.25, llcrnrlat=56, urcrnrlon=-134.25, urcrnrlat=57.75)

map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='blue')
map.drawmapboundary()

map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

spist_known_file = open("/Users/neavemj/microbiome/subprojects/4.map/s.pistillataKnownDist.csv")
pVerr_known_file = open("/Users/neavemj/microbiome/subprojects/4.map/p.verrucosaKnownDist.csv")

spist_known = pd.DataFrame.from_csv(spist_known_file)

print spist_known

lon = -135.33
lat = 57.08
x,y = map(lon, lat)

map.plot(x, y, 'ro', markersize=12)



plt.show()

