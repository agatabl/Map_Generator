from matplotlib.collections import PatchCollection
from descartes import PolygonPatch
import shapely
import numpy as np
from mpl_toolkits.basemap import Basemap
import geopandas as gp
import matplotlib.pyplot as plt
from osgeo import ogr


path = "C:/Users/agata/Desktop/MAMA/mapki/gory/mnts.shp"

# jak na razie do niczego nie przydatne generowanie bounding boza. przy wyborze
# odwzorowania chce tego uzyc do wycntrowania odwzorowania 'orto' do danego kraju


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
        print(bbox)
        # output : ymin, xmin, ymax, xmax
        return bbox


# to są wszystkie łąncuchy gorskie z pliku
features = gp.GeoDataFrame.from_file(path)
# print(type(features))
# features.plot()
# wyswietla porządany element jako wykres matplotliba
for index, row in features.iterrows():
    Qkod = row[1]
    if Qkod == 'Q686362':
        bouning_box = get_bbox(path, "WIKIDATAID = 'Q686362'")

# wyswietla basemape przyzoomowna do danego miejsca
        mm = Basemap(width=800000, height=700000,
                     resolution='i', projection='aea',
                     lat_1=(bouning_box[0]-5), lat_2=(bouning_box[2]+5),
                     lon_0=(bouning_box[0] + abs((bouning_box[2]-bouning_box[0])/2)),
                     lat_0=(bouning_box[1] + abs((bouning_box[3]-bouning_box[1])/2)))

        # mm = Basemap(llcrnrlon=(bouning_box[0]-5), llcrnrlat=(bouning_box[1]-5),
        #              urcrnrlon=(bouning_box[2]+5), urcrnrlat=(bouning_box[3]+5),
        #              resolution='i', projection='tmerc', lat_0=bouning_box[1], lon_0=bouning_box[2])
        water = 'lightskyblue'
        earth = 'cornsilk'
        countries = mm.drawcountries()
        mm.fillcontinents(color=earth, lake_color=water)
        boundary = mm.drawmapboundary(fill_color=water)
        merid = mm.drawmeridians(np.arange(-180, 180, 20), labels=[False, False, False, True])
        parall = mm.drawparallels(np.arange(0, 80, 20), labels=[True, True, False, False])

        juneau_lon, juneau_lat = -3.716667, 40.383333
        x, y = mm(juneau_lon, juneau_lat)
        madrid = mm.scatter(x, y, 80, label="Madrid", color='red', zorder=10)
        plt.title('moja mapa')

    # ax to jest wyplotowany dany element chyba
        ax1 = features.loc[[index], 'geometry'].plot()
        ax1.set_aspect(1.5)
        ax1.set_title('W sumie tytul')
        fig = plt.gcf()
        #fig, ax = plt.subplots(1,1,figsize=(12, 10))

        patches = []
        poly = row.geometry
        if poly.geom_type == 'Polygon':
            mpoly = shapely.ops.transform(mm, poly)
            # print(row.geometry)
            patches.append(PolygonPatch(mpoly))
        elif poly.geom_type == 'MultiPolygon':
            for subpoly in poly:
                mpoly = shapely.ops.transform(mm, poly)
                patches.append(PolygonPatch(mpoly))
        else:
            print(row, "is neither a polygon nor a multi-polygon. Skipping it.")

        patches.append(ax1)
        print(patches)
        ax1.add_collection(PatchCollection(patches, match_original=True))
