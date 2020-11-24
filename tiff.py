from osgeo import gdal
from os import path


class Tiff:
    """Tif file class"""

    def __init__(self, filepath):
        self.__filepath = filepath
        self.filename = path.basename(self.filepath).split('.')[0]
        self.areaname = ""
        self.__envelope = []

    @property
    def filepath(self):
        return self.__filepath

    @property
    def ds(self):
        return gdal.Open(self.filepath)

    @property
    def envelope(self):
        return self.__envelope

    @envelope.setter
    def envelope(self):
        ds = self.ds
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
        self.__envelope = metadata

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

    def match_area(self, areas):
        pass

    def rename(self):
        pass
