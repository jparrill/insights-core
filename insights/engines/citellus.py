import os.path
from citellusclient import shell as citellus

class CitellusTypes(object):
    """
    This class creates and object to define the structure of a report
    """
    def __init__(self, name, long_name, description, status, error, bugzilla,
            _id, priority, backend, plugin):
        
        self.name = name
        self.long_name = long_name
        self.description = description
        self.status = status
        self.error = error
        self.bugzilla = bugzilla
        self.id = _id
        self.priority = priority
        self.backend = backend
        self.plugin = plugin



class CitellusEngine(object):
    """
    This engine will serve a transformation component to work with
    Citellus project.
    """

    def __init__(self, sosreport):
        print "Sosreport: {}".format(os.path.basename(sosreport))
        self.rc_types = { 10: 'RC_OKAY', 20: 'RC_FAILED', 30: 'RC_SKIPPED' }
        self.engine = 'citellus'


    def get_plugins(self, options, filter=False):
        return citellus.findallplugins()

    def exec_engine(self, path=False, plugins=False, forcerun=False, include=None, exclude=None):
        plugins = self.get_plugins(include, filter=True)
        raw_results = citellus.docitellus(path=path, plugins=plugins, forcerun=forcerun, include=include, exclude=exclude, quiet=True)

        formatted_results, stats = self.formatter(raw_results, plugins)

        #return self.type_instantiation(new_dict)
        return formatted_results, stats


    def check_rc(self, rc):
        return self.rc_types[rc]

    def formatter(self, results, plugins):
        # Process plugin output from multiple plugins to be returned as a dictionary of ID's for each plugin
        new_dict = {}
        
        # Stats
        # TODO: Implement in citellus loader a counter to get all fails loading rules and parsers
        stats = {}

        # Rules loaded
        stats['loaded_rule'] = {}
        stats['loaded_rule']['count'] = 0
        stats['loaded_rule']['fail'] = 0

        # Parsers Executed
        stats['parser'] = {}
        stats['parser']['count'] = 0
        stats['parser']['fail'] = 0

        # Skipped plugins (?)
        stats['skip'] = {}
        stats['skip']['count'] = 0
        stats['skip']['fail'] = 0

        # Rules 
        stats['loaded_rule'] = {}
        stats['loaded_rule']['count'] = len(plugins)
        stats['loaded_rule']['fail'] = 0

        for item in results:
            name = results[item]['name']
            results[item]['plugin'] = os.path.relpath(results[item]['plugin'])
            results[item]['status'] = self.check_rc(results[item]['result']['rc'])
            results[item]['engine'] = str.capitalize(self.engine)
            if results[item]['result']['rc'] == 20:
                results[item]['error'] = results[item]['result']['err']
            elif results[item]['result']['rc'] == 30:
                stats['skip']['count'] += 1
            
            # Stats
            stats['parser']['count'] += 1

            # Omit some output
            del results[item]['result']
            del results[item]['name']

            # Result
            new_dict[name] = dict(results[item])
        del results

        stats['skip']['count'] = stats['loaded_rule']['count'] - stats['skip']['count']

        return new_dict, stats

    def type_instantiation(self, results):
        # Instantiate dict into classes types decalrated on init
        formatted_result = []

        for key, value in results.iteritems():
            if value['result']['rc'] == 20:
                error = value['result']['err']
            else:
                error = False

            formatted_result.append(CitellusReport(
                value['name'], value['long_name'], value['description'], self.check_rc(value['result']['rc']),
                error, value['bugzilla'], value['id'], value['priority'], value['backend'], value['plugin']
                ))

        return formatted_result
