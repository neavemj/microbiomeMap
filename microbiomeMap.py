__author__ = 'neavemj'


## use basemap in python to create a sampling map for Microbiome project ##
# Matthew J. Neave 5.2.2015

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


map = Basemap(projection = 'ortho', lat_0 = 50, lon_0 = -100, resolution = 'l', area_thresh = 1000.0)

map.drawcoastlines()

plt.show()

