from __future__ import division


class Variables:
    '''Singleton-Object'''

    class __Variables:
        def __init__(self, tuple_=None):
            for x in tuple_._fields:
                setattr(self, x, tuple_.__getattribute__(x))

    instance = None

    def __init__(self, tuple_=None):

        if not Variables.instance:
            Variables.instance = Variables.__Variables(tuple_)

    def __setattr__(self, name, val):
        setattr(self.instance, name, val)

    def __getattr__(self, name):
        return getattr(self.instance, name)


def config():
    '''Makes all necessary setups in order to run the polygon-generator'''
    import json
    from collections import namedtuple

    with open('inputs/polygons.conf', 'r') as f:
        variables_string = f.read()

    variables = json.loads(variables_string, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    variables = Variables(variables)
    return variables


if __name__ == "__main__":
    print(config())
