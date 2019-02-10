
import shapefile
import shapely
import matplotlib.pyplot as plt
from descartes import PolygonPatch


sf = shapefile.Reader(
    "C:/Users/agata/AppData/Local/Programs/Python/Python36-32/games/mapgenerator/countries_new/simpleCountries")
records = sf.records()
shapes = sf.shapes()
print(shapes)
fields = sf.fields
# print(fields)
# print(records)


for record in records:
    i = records.index(record)
    if record[3] == 'Poland':
        poly = shapes[i].__geo_interface__
        fig = plt.figure()
        ax = fig.gca()
        ax.add_patch(PolygonPatch(poly))
        ax.axis('on')
        plt.show()
