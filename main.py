from controller import Controller
from osgeo import gdal
import sys


def main():
    src = input("Input tiff files dir(default is \".\"):")
    cfg = input("Input config file path(default is \"./config.txt\"):")
    # c = Controller()
    # c = Controller(src="./example", cfg="./example/config.txt")
    # c = Controller(cfg="./example/config.txt")
    c = Controller(src, cfg)
    c.set_tifs_area()
    c.rename()


if __name__ == "__main__":
    while 1:
        try:
            main()
            input("[+] Done. Press any key to exit.")
            sys.exit(0)
        except FileNotFoundError:
            print("[-] Please make sure config file at right spot as you input.")
        except Exception as err:
            print(err)
