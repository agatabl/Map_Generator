import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PatchCollection
import numpy as np
from descartes import PolygonPatch
import geopandas as gp
from matplotlib import pyplot as plt
import shapely

glaciers = gp.GeoDataFrame.from_file(
    'C:/Users/agata/Desktop/MAMA/mapki/natural_earth_vector/10m_physical/ne_10m_glaciated_areas.shp')
print(glaciers.head())
print(glaciers.crs)
studyarea = shapely.geometry.box(-136., 56., -130., 60.)
glaciers[glaciers.geometry.intersects(studyarea)].head(20)

water = 'lightskyblue'
earth = 'cornsilk'
font = {'family': 'Calibri',
        'weight': 'bold',
        'size': 20}
mpl.rc('font', **font)
fig, ax1 = plt.subplots(figsize=(12, 10))
juneau_lon, juneau_lat = -134.4167, 58.3

fig, ax1 = plt.subplots(figsize=(12, 10))
mm = Basemap(
    width=600000, height=400000,
    resolution='i',
    projection='aea',
    ellps='WGS84',
    lat_1=55., lat_2=65.,
    lat_0=58., lon_0=-134)
coast = mm.drawcoastlines()
rivers = mm.drawrivers(color=water, linewidth=1.5)
continents = mm.fillcontinents(
    color=earth,
    lake_color=water)
bound = mm.drawmapboundary(fill_color=water)
countries = mm.drawcountries()
merid = mm.drawmeridians(np.arange(-180, 180, 2), labels=[False, False, False, True])
parall = mm.drawparallels(np.arange(0, 80), labels=[True, True, False, False])
x, y = mm(juneau_lon, juneau_lat)
juneau = mm.scatter(x, y, 80, label="Juneau", color='red', zorder=10)
patches = []
for poly in glaciers[glaciers.geometry.intersects(studyarea)].geometry:
    if poly.geom_type == 'Polygon':
        mpoly = shapely.ops.transform(mm, subpoly)
        patches.append(PolygonPatch(mpoly))
    elif poly.geom_type == 'MultiPolygon':
        for subpoly in poly:
            mpoly = shapely.ops.transform(mm, subpoly)
            patches.append(PolygonPatch(mpoly))
    else:
        print(poly, " is neither a polygon nor a multi-polygon. Skipping it.")
glaciers = ax1.add_collection(PatchCollection(patches, match_original=True))
