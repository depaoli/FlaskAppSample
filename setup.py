#
# Distribution setup file
#
import os
from setuptools import setup, find_packages


# Parse 'etc' to look for config files (ie. data_files arg)
data_files = []
for directory, sub_directories, files in os.walk('etc'):
	filenames = []
	for filename in files:
		filenames.append(os.path.join(directory, filename))
	data_files.append((os.path.join('/FlaskAppServer', directory), filenames))

args = dict(
    # Application details
    name                = "FlaskAppSample",
    long_description    = open("README.md").read(),
    version             = "0.0.1",
    author              = "Matteo De Paoli",
    author_email        = "depaoli@",
    url                 = "https://github.com/depaoli/FlaskAppSample",

    # Find Packages automatically but don't include those in "test" (ie. unittest)
    packages = find_packages(exclude=("test",)),

    # Tells distribute to look for a MANIFEST.in file
    # and wrap-up all the entries that match inside the package itself
    # (rather than declaring "package_data" arg)
    include_package_data = True,

    # Data files to be wrapped-up but to be copied outside the package
    data_files = data_files
)

setup(**args)
