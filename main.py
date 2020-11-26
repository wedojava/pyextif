from controller import Controller
from osgeo import gdal


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
    # a = envelope("./example/test/test.tif")
    # print(a)
    # c = Controller()
    # c = Controller("./example", "./example/config.txt")
    c = Controller(cfg="./example/config.txt")
    c.set_tifs_area()
    print(c.tifs[0].areanames)
    c.rename()
