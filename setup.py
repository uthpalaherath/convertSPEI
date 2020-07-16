import setuptools
from numpy.distutils.core import Extension, setup

setup(
    name="convertSPEI",
    description="A Python script to convert Standardised Precipitation-Evapotranspiration Index (SPEI) data from the netcdf format to a csv format.",
    version="0.7",
    author="Uthpala Herath",
    author_email="ukh0001@mix.wvu.edu",
    url="https://github.com/uthpalaherath/convertSPEI",
    download_url="https://github.com/uthpalaherath/convertSPEI/archive/0.7.tar.gz",
    license="LICENSE.txt",
    scripts=["scripts/convertSPEI.py"],
    install_requires=["netcdf4", "csv"],
    keywords=["netcdf", "spei", "atmosphereicsciences", "earthsciences"],
)
