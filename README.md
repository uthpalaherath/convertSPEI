# convertSPEI

This program converts time series Standardised Precipitation-Evapotranspiration Index (SPEI) data from the netcdf format to a csv format which could be read by a program such as Excel. The SPEI data is available at <https://spei.csic.es/index.html>. </br>
Although parallelized, for large datasets the conversion might take a while. 
The column headers are Time, Latitude, Longitude and SPEI value in that order.


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
convertSPEI.py -np 20 -inp spei01.nc -out spei01_converted.csv
```

where, </br>

- np : the number of processors
- inp : input file name
- out : output file name

**Note:** </br>

If ``Memory Error`` occurs, reduce the number of processors to provide more memory per core for the conversion. 