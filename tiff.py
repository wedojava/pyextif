from osgeo import gdal
from osgeo import ogr
from os import path


class Tiff:
    """Tif file class"""

    def __init__(self, filepath):
        self.areanames = []
        self.geometry = None
        self.filepath = filepath
        self.filename = path.basename(self.filepath).split('.')[0]

        # get dataset
        try:
            _ds = gdal.Open(filepath)
        except Exception as e:
            raise e
        self.ds = _ds

        # make geom
        self.make_geom()

    def make_geom(self):
        """This should use after dataset get done.

        Return:
        """

        def make_wkt(points):
            pp = ""
            for point in points:
                i = 0
                pp += f"{point[0]} {point[1]}"
                if i < len(points):
                    pp += ", "
            return f"POLYGON (({pp}))"

        ds = self.ds
        ulx, xres, _, uly, _, yres = ds.GetGeoTransform()
        lrx = ulx + (ds.RasterXSize * xres)  # low right x
        lry = uly + (ds.RasterYSize * yres)  # low right y
        minx, miny, maxx, maxy = ulx, lry, lrx, uly
        points = [ [minx, miny], [maxx, miny], [minx, maxy], [maxx, maxy] ]
        wkt = make_wkt(points)
        self.geometry = ogr.CreateGeometryFromWkt(wkt)

    def match_area(self, areas):
        pass

    def rename(self):
        pass

