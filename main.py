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


def raster_metadata(src):
    """

    Args:
            src: file path

    Returns:
            metadata

    """
    ds = gdal.Open(src)
    metadata = dict()
    # 也可以是 LongName。GTiff 与 GeoTiff 的区别
    metadata['format'] = ds.GetDriver().ShortName
    # 波段数
    metadata['band_count'] = ds.RasterCount
    # band 1
    band = ds.GetRasterBand(1)
    metadata['nodata'] = band.GetNoDataValue()
    # 统计值
    band_stat = band.GetStatistics(True, True)
    metadata['min'] = band_stat[0]
    metadata['max'] = band_stat[1]
    metadata['mean'] = band_stat[2]
    metadata['stddev'] = band_stat[3]
    # 空间参考系统
    srs = osr.SpatialReference(ds.GetProjectionRef())
    metadata['proj4'] = srs.ExportToProj4()
    metadata['wkt'] = srs.ExportToWkt()
    # 地理坐标系
    metadata['geocs'] = srs.GetAttrValue('GEOGCS')
    metadata['uom'] = srs.GetAttrValue('UNIT')
    # 投影坐标系
    metadata['projcs'] = srs.GetAttrValue('PROJCS')  # if projected
    metadata['epsg'] = srs.GetAuthorityCode(None)
    # or
    # metadata['srid'] = srs.GetAttrValue('AUTHORITY', 1)
    # 是否有地图投影（平面坐标）
    metadata['is_projected'] = srs.IsProjected()
    # 仿射变换信息，6参数：
    # upper left x, x(w-e) resolution, x skew, upper left y, y skew, y(s-n) resolution
    ulx, xres, xskew, uly, yskew, yres = ds.GetGeoTransform()
    lrx = ulx + (ds.RasterXSize * xres)  # low right x
    lry = uly + (ds.RasterYSize * yres)  # low right y

    metadata['minx'] = ulx
    maxx = lrx  # ulx + xres * ds.RasterXSize
    metadata['maxx'] = maxx
    miny = lry  # uly + yres * ds.RasterYSize
    metadata['miny'] = miny
    metadata['maxy'] = uly
    # 中心点 centroid
    cx = ulx + xres * (ds.RasterXSize / 2)
    cy = uly + yres * (ds.RasterYSize / 2)
    metadata['center_x'] = cx
    metadata['center_y'] = cy
    metadata['resolution'] = xres
    # geographic width
    metadata['width'] = ds.RasterXSize * xres
    # geographic height，negative，负值
    metadata['height'] = ds.RasterYSize * yres
    # image width
    metadata['size_width'] = ds.RasterXSize
    metadata['size_height'] = ds.RasterYSize
    # minx,miny,maxx,maxy
    metadata['extent'] = [ulx, miny, maxx, uly]
    metadata['centroid'] = [cx, cy]
    ds = None
    return metadata


if __name__ == "__main__":
    a = envelope("./test.tif")
    print(a)
