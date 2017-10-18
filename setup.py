from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as req_file:
    install_requires = req_file.readlines()

# with open('test_requirements.txt') as req_file:
#     tests_require = req_file.readlines()

NAME = 'woodruffstats'
VERSION = '0.0.0'

setup(
    name = NAME,
    version = VERSION,
    license='All rights reserved.',
    packages = find_packages(),
    install_requires=install_requires,
    # tests_require=tests_require,
    zip_safe=False
)