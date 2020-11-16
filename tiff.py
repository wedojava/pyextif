import os

class Tiff:
    """Tif file class"""
    def __init__(self, filepath):
        self.filepath = filepath


    def get_tifs(self, path):
        """get tif filelist from src"""
        tifs = []
        for item in os.scandir(path):
            if item.is_file() and item.name.endswith(".tif"):
                tifs.append(item)

        return tifs
