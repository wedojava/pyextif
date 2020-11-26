import os
from osgeo import ogr
from tiff import Tiff


class Controller:
    """Deal with folder and files"""

    def __init__(self):
        self.src = ""
        self.cfg = "./config.txt"
        self.tifs = []
        self.areas = []

    def scan_tif(self, dir):
        """Scan dir for tif files recursively"""

        for entry in os.scandir(dir):
            if entry.is_dir():
                self.scan_tif(entry)
            elif not entry.name.startswith(".") and entry.name.endswith(".tif"):
                tif = Tiff(entry.path)
                tif.filename = entry.name
                self.tifs.append(tif)

    def read_cfg(self, cfg):
        if not cfg:
            cfg = self.cfg
        with open(cfg) as f:
            for line in f:
                name, wkt = line.split(':')
                self.areas.append([name, wkt.strip()])

    def do(self, src: str, cfg: str):
        def intersection(wkt1, wkt2):
            poly1 = ogr.CreateGeometryFromWkt(wkt1)
            poly2 = ogr.CreateGeometryFromWkt(wkt2)
            intersection = poly1.Intersection(poly2)
            if "EMPTY" in intersection.ExportToWkt():
                return False
            else:
                return True

        if not src:
            src = self.src
        if not cfg:
            cfg = self.cfg
        self.read_cfg(cfg)
        self.scan_tif(src)
        for tif in self.tifs:
            tif.dataset()
            tif.make_wkt_geom()
            for area in self.areas:
                if intersection(tif.wkt, area[1]):
                    tif.areanames.append(area[0])

        print(self.tifs[0].areanames)
        # rename
