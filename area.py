from osgeo import ogr


class Area():
    """Contains name and points for the area.
    name is area name, points is sames like [[1154115.274565847, 686419.4442701361], [1154115.274565847, 686419.4442701361], [1154115.274565847, 686419.4442701361], [1154115.274565847, 686419.4442701361]]
    """

    def __init__(self, arg):
        self.name = arg
        self.wkt = None
        self.__geom_poly = None

    @property
    def geom_poly(self):
        return self.__geom_poly

    @geom_poly.setter
    def geom_poly(self, points):
        ring = ogr.Geometry(ogr.wkbLinearRing)
        for p in points:
            if len(p) == 2:
                ring.AddPoint(p[0], p[1])
        geom_poly = ogr.Geometry(ogr.wkbPolygon)
        geom_poly.AddGeometry(ring)
        self.__geom_poly = geom_poly
