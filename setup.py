from setuptools import Extension, setup
from distutils.command.sdist import sdist as _sdist

from Cython.Build import cythonize
from Cython.Distutils import build_ext


cmdclass = {}


class sdist(_sdist):
    def run(self):
        cythonize(
            ext_modules, annotate=True, compiler_directives={"embedsignature": True}
        )
        _sdist.run(self)


cmdclass["sdist"] = sdist
cmdclass.update({"build_ext": build_ext})
ext_modules = cythonize([Extension("scripts.append_df", ["scripts/append_df.pyx"])])

setup(
    name="convertSPEI",
    description="A Python script to convert Standardised Precipitation-Evapotranspiration Index (SPEI) data from the netcdf format to csv and Excel formats.",
    version="0.3",
    author="Uthpala Herath",
    author_email="ukh0001@mix.wvu.edu",
    url="https://github.com/uthpalaherath/convertSPEI",
    download_url="https://github.com/uthpalaherath/convertSPEI/archive/0.3.tar.gz",
    license="LICENSE.txt",
    scripts=["scripts/convertSPEI.py"],
    install_requires=["pandas", "cython"],
    keywords=["netcdf", "spei", "atmosphereicsciences", "earthsciences"],
    ext_modules=ext_modules,
)
