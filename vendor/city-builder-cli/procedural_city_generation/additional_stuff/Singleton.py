class Singleton:
    """
    Singleton Object which can only have one instance.
    Is instantiated with a modulename, e.g. "roadmap", and reads the
    corresponding "roadmap.conf" in procedural_city_generation/inputs.
    All attributes are mutable, however this class should mainly be used for
    immutable numeric values to avoid confusion/difficult-to-trace-bugs.
    """

    class __Singleton:

        def __init__(self, module_name=None):
            import procedural_city_generation
            import os
            import json
            if module_name:
                path = os.path.dirname(procedural_city_generation.__file__)
                with open(path + "/inputs/" + module_name + ".conf", 'r') as f:
                    d = json.loads(f.read())
                for k, v in d.items():
                    setattr(self, k, v["value"])
            else:
                print("Warning, Singleton instantiated without parsing a json file. "
                      "Please specify the module name parameter to avoid errors")

    instance = None

    def __init__(self, module_name=None):
        """
        Creates the instance.

        Parameters
        ----------
        module_name : String

        """
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton(module_name)

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        setattr(self.instance, name, value)

    def kill(self):
        """
        Deletes the Singleton's instance
        """
        Singleton.instance = None
