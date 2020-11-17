import os
from tiff import Tiff


class Handle:
    """Deal with folder and files"""

    def __init__(self, src):
        self.src = src
        self.tifs = []
        self.areas = dict()

    def scan_tif(self, dir):
        """Scan dir for tif files recursively"""
        for entry in os.scandir(dir):
            if entry.is_dir():
                self.scan_tif(entry)
            elif not entry.name.startswith(".") and entry.name.endswith(".tif"):
                tif = Tiff(entry.path)
                tif.filename = entry.name
                self.tifs.append(tif)

    def read_cfg(self, cfg="./config.txt"):
        with open(cfg) as f:
            for line in f:
                name, envelope = line.split(':')
                envelope = envelope.split(',')
                self.areas[name.strip()] = envelope

    def do(self, src:str, cfg:str):
        self.read_cfg(cfg)
        self.scan_tif(src)
        for tif in self.tifs:
            tif.extract()
            tif.match_area(self.areas)
            tif.rename()

