# convertSPEI

This program converts Standardised Precipitation-Evapotranspiration Index (SPEI) data from the netcdf format to csv and Excel formats. The SPEI data is available at <https://spei.csic.es/index.html>.

## Installation

```
pip install convertSPEI
```

\* Packages in PyPI are not case sensitive. 

Once installed, use the ``-h`` flag to see a list of options.

```
convertSPEI.py -h
```

## Usage

```
convertSPEI.py -np 20 -inp spei01.nc -out spei01_converted.xslx -type excel
```

where, </br>

- np : the number of processors
- type : the output format {excel,csv} 

**Note:** </br>

If ``Memory Error`` occurs, reduce the number of processors to provide more memory per core for the conversion. 