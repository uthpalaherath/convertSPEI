import setuptools
from numpy.distutils.core import Extension, setup

setup(
    name="convertSPEI",
    description="A Python script to convert Standardised Precipitation-Evapotranspiration Index (SPEI) data from the netcdf format to csv and Excel formats.",
    version="0.1",
    author="Uthpala Herath",
    author_email="ukh0001@mix.wvu.edu",
    url="https://github.com/uthpalaherath/convertSPEI",
    download_url="https://github.com/uthpalaherath/convertSPEI/archive/0.1.tar.gz",
    license="LICENSE.txt",
    scripts=["scripts/convertSPEI.py"],
    install_requires=["pandas"],
    keywords=["netcdf", "spei", "atmosphereicsciences", "earthsciences"],
)
