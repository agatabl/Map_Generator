from osgeo import ogr, osr
import os


def get_bbox(name, condition):
    shapefile = name
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataset = driver.Open(shapefile, 0)
    layer = dataset.GetLayer()
    layer.SetAttributeFilter(condition)

    for feature in layer:
        env = feature.GetGeometryRef().GetEnvelope()
        # output: ymin, ymax, xmin, xmax
        bbox = [env[0], env[2], env[1], env[3]]
        # output : ymin, xmin, ymax, xmax
        return bbox

print(get_bbox("C:/Users/agata/AppData/Local/Programs/Python/Python36-32/games/mapgenerator/countries_new/simpleCountries.shp", "NAME_EN = 'Poland'"))
