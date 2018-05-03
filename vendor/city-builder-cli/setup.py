from codecs import open
from os import path

from setuptools import Command, find_packages, setup

from city_builder import __version__

this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        # errno = call(['py.test', '--cov=skele', '--cov-report=term-missing'])
        # raise SystemExit(errno)
        # TODO find out what it does
        pass


args = {
    'name': 'city-builder',
    'version': __version__,
    'description': 'A command line program for creating cities',
    'long_description': long_description,
    'url': 'https://github.com/augustoerico/city-builder-cli',
    'author': 'Jonathan Sauder',
    'author_email': 'jonathan.sauder@student.hpi.de',
    'license': 'MPL2.0',
    'classifiers': [],  # TODO add classifiers
    'packages': find_packages(exclude=['doc', 'outputs', 'temp']),
    'install_requires': ['docopt'],  # TODO add all required packages (scipy basically)
    'extra_require': {
        'test': ['coverage', 'pytest', 'pytest-cov']
    },
    'entry_points': {
        'console_scripts': ['city_builder=city_builder.cli:main']
    },
    'cmdclass': {
        'test': RunTests
    }
}
setup(**args)
