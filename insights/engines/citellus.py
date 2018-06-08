import os.path
from citellusclient import shell as citellus

class CitellusEngine(object):
    """
    This engine will serve a transformation component to work with
    Citellus project.
    """

    def __init__(self, sosreport):
        print "Loading Engine: {}".format(self.__class__.__name__)
        print os.path.abspath(sosreport)


    def get_plugins(self, options, filter=False):
        return citellus.findallplugins()

    def exec_engine(self, path=False, plugins=False, forcerun=False, include=None, exclude=None):
        plugins = self.get_plugins(include, filter=True)
        #ids = citellus.getids(plugins=plugins, include=include, exclude=exclude)
        results = citellus.docitellus(path=path, plugins=plugins, forcerun=forcerun, include=include, exclude=exclude, quiet=True)

        # Process plugin output from multiple plugins to be returned as a dictionary of ID's for each plugin
        new_dict = {}
        for item in results:
            name = results[item]['id']
            new_dict[name] = dict(results[item])
        del results

        return new_dict

