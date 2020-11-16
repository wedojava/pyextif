from osgeo import gdal, ogr, osr
import os


def envelope(src):
    ds = gdal.Open(src)
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
    return metadata




if __name__ == "__main__":
    a = envelope("./test.tif")
    print(a)
