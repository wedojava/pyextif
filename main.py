from controller import Controller
from osgeo import gdal


def main():
    src = input("Input tiff files dir(default is \".\"):")
    cfg = input("Input config file path(default is \"./config.txt\"):")
    # c = Controller()
    # c = Controller("./example", "./example/config.txt")
    # c = Controller(cfg="./example/config.txt")
    c = Controller(src, cfg)
    c.set_tifs_area()
    c.rename()

if __name__ == "__main__":
    while 1:
        try:
            main()
        except FileNotFoundError:
            print("[-] Please make sure config file at right spot as you input.")
        except Exception as err:
            print(err)
