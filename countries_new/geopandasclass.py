import geopandas as gp
import shapely
import matplotlib.pyplot as plt
from osgeo import ogr

path = "C:/Users/agata/AppData/Local/Programs/Python/Python36-32/games/mapgenerator/countries_new/simpleCountries.shp"

class myClass:

def __init__(self, shapefile, driver, dataset, layer):
    shapefile = name
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataset = driver.Open(shapefile, 0)
    layer = dataset.GetLayer()


def get_bbox(self, name, condition):

    layer.SetAttributeFilter(condition)

    for feature in layer:
        env = feature.GetGeometryRef().GetEnvelope()
        # output: ymin, ymax, xmin, xmax
        bbox = [env[0], env[2], env[1], env[3]]
        # output : ymin, xmin, ymax, xmax
        return bbox

def show_feature():

bouning_box = get_bbox(path, "NAME_EN = 'New Zealand'")

countries = gp.GeoDataFrame.from_file(path)
studyarea = shapely.geometry.box(bouning_box[0], bouning_box[1], bouning_box[2], bouning_box[3])
ax1 = countries[countries.geometry.within(studyarea)].plot()

ax1.set_aspect(2)
fig = plt.gcf()
fig.set_size_inches(15, 10)
