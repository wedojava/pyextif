from osgeo import gdal
from osgeo import ogr
from os import path


class Tiff:
    """Tif file class"""

    def __init__(self, filepath):
        self.areanames = []
        self.geometry = None
        self.ds = None
        self.wkt = None
        self.filepath = filepath
        self.filename = path.basename(self.filepath).split('.')[0]

    def dataset(self):
        """Open tif file set `self.ds` and return dataset."""

        try:
            _ds = gdal.Open(self.filepath)
        except Exception as e:
            _ds = None
            raise e
        self.ds = _ds
        return _ds

    def make_wkt_geom(self):
        """This should be used after dataset get done."""

        def make_wkt(points):
            pp = ""
            for point in points:
                pp += f"{point[0]} {point[1]}, "
            pp = pp[:-2]
            return f"POLYGON (({pp}))"

        ds = self.dataset()
        ulx, xres, _, uly, _, yres = ds.GetGeoTransform()
        lrx = ulx + (ds.RasterXSize * xres)  # low right x
        lry = uly + (ds.RasterYSize * yres)  # low right y
        minx, miny, maxx, maxy = ulx, lry, lrx, uly
        points = [[minx, miny], [maxx, miny], [
            maxx, maxy], [minx, maxy], [minx, miny]]
        self.wkt = make_wkt(points)
        self.geometry = ogr.CreateGeometryFromWkt(self.wkt)
