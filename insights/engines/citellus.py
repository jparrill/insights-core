import os.path

class CitellusEngine(object):
    """
    This engine will serve a transformation component to work with
    Citellus project.
    """

    def __init__(self, sosreport):
        print "Loading Engine: {}".format(self.__class__.__name__)
        print os.path.abspath(sosreport)


