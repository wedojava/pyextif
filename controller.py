import os
from osgeo import ogr
from tiff import Tiff


class Controller:
    """Deal with folder and files"""

    def __init__(self, src="./", cfg="./config.txt"):
        self.src = src
        self.cfg = cfg
        self.tifs = []
        self.areas = []
        self.read_cfg()
        self.scan_tif(self.src)

    def scan_tif(self, dir):
        """Scan dir for tif files recursively"""

        for entry in os.scandir(dir):
            if entry.is_dir():
                self.scan_tif(entry)
            elif not entry.name.startswith(".") and entry.name.endswith(".tif"):
                tif = Tiff(entry.path)
                tif.filename = entry.name
                self.tifs.append(tif)

    def read_cfg(self):
        with open(self.cfg) as f:
            for line in f:
                name, wkt = line.split(':')
                self.areas.append([name, wkt.strip()])

    def set_tifs_area(self):
        """if tif intersected with areas in config, set the areaname to the tif."""

        def intersection(wkt1, wkt2):
            poly1 = ogr.CreateGeometryFromWkt(wkt1)
            poly2 = ogr.CreateGeometryFromWkt(wkt2)
            intersection = poly1.Intersection(poly2)
            if "EMPTY" in intersection.ExportToWkt():
                return False
            else:
                return True

        for tif in self.tifs:
            tif.dataset()
            tif.make_wkt_geom()
            for area in self.areas:
                if intersection(tif.wkt, area[1]):
                    tif.areanames.append(area[0])
    
    def rename(self):
        pass