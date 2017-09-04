try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Woodruff Stats',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['woodruffstats'],
    'scripts': [],
    'name': 'woodruffstats'
}

setup(**config)