from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

m = Basemap(projection='ortho',
            lat_0=-90, lon_0=0,
            # llcrnrlat=49,
            # llcrnrlon=13,
            # urcrnrlat=55,
            # urcrnrlon=25,
            resolution='l')

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral', lake_color="aqua")

# m.drawrivers()
parallels = np.arange(0., 81, 10.)
m.drawparallels(parallels, labels=[False, True, True, False])
meridians = np.arange(10., 351., 20.)
m.drawmeridians(meridians, labels=[True, False, False, True])

plt.title("Moja mapa")
plt.show()
