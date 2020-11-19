from osgeo import gdal

class Tiff:
    """Tif file class"""

    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = ""
        self.areaname = ""
        self.envelope = []

    def extract(self):
        ds = gdal.Open(self.filepath)
        metadata = dict()
        ulx, xres, _, uly, _, yres = ds.GetGeoTransform()
        lrx = ulx + (ds.RasterXSize * xres)  # low right x
        lry = uly + (ds.RasterYSize * yres)  # low right y
        metadata['minx'] = ulx
        maxx = lrx  # ulx + xres * ds.RasterXSize
        metadata['maxx'] = maxx
        miny = lry  # uly + yres * ds.RasterYSize
        metadata['miny'] = miny
        metadata['maxy'] = uly
    pass

    def match_area(self, areas):
        pass

    def rename(self):
        pass
