from setuptools import setup, find_packages
import sys, os, io

# List all of your Python package dependencies in the
# requirements.txt file

def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()

readme = readfile("README.md")[3:]  # skip title
requires = readfile("requirements.txt")
license = readfile("LICENSE")
package_data = {
  'mapclientplugins.fieldworkgait2392musclehmfstep': [
    'data/fieldwork_geometry/*',
  ],
}

setup(name=u'mapclientplugins.fieldworkgait2392musclehmfstep',
    version='0.1.0',
    description='',
    long_description='\n'.join(readme) + license,
    classifiers=[
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    ],
    author=u'Ju Zhang',
    author_email='',
    url='https://github.com/mapclient-plugins/fieldworkgait2392musclehmfstep',
    license='APACHE',
    packages=find_packages(exclude=['ez_setup',]),
    namespace_packages=['mapclientplugins'],
    include_package_data=True,
    package_data=package_data,
    zip_safe=False,
    install_requires=requires,
    )
