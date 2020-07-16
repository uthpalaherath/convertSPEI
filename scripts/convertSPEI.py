#!/usr/bin/env python

"""
SPEI data converter.

This script converts SPEI time series data in netcdf format
retrieved from https://spei.csic.es to a csv format.

Note: Although parallelized, for large datasets the conversion
might take a while.

- Uthpala Herath
  July, 2020

Usage:

$ convertSPEI.py -np 4 -inp spei01.nc -out spei01_converted.csv

convertSPEI.py -h brings up the help menu.

"""

import netCDF4
import sys
from multiprocessing import Pool
import argparse
from argparse import RawTextHelpFormatter
import csv


def get_spei(datalist):
    """
    this method returns the SPEI value given
    time, latitude and longitude indexes i,j,k.
    """
    dtime_retlist = []
    lat_retlist = []
    lon_retlist = []
    spei_retlist = []

    dtime_retlist.append(datalist[0])
    lat_retlist.append(datalist[1])
    lon_retlist.append(datalist[2])
    spei_retlist.append(spei.data[datalist[0], datalist[1], datalist[2]])

    return dtime_retlist, lat_retlist, lon_retlist, spei_retlist


def main(args):

    print("----------------------------------")
    print("\nSPEI data converter")
    print("\nAuthor: Uthpala Herath")
    print("https://github.com/uthpalaherath")
    print("----------------------------------")
    print("\nRunning on %d cores..." % args.np)

    inp = args.inp
    out = args.out
    np = args.np

    spei_nc_file = inp
    nc = netCDF4.Dataset(spei_nc_file, mode="r")

    lat = nc.variables["lat"][:]
    lon = nc.variables["lon"][:]
    rawtime = nc.variables["time"]
    dtime = netCDF4.num2date(rawtime[:], rawtime.units)

    global spei
    spei = nc.variables["spei"][:]

    nc.close()

    # Creating array for calling get_spei() in parallel.
    print("\nCreating data list...")
    datalist = []
    for i in range(len(dtime)):
        for j in range(len(lat)):
            for k in range(len(lon)):
                datalist.append([i, j, k])


    # Calling get_spei to get spei value and append
    # to dataframe
    print("Indexing SPEI data [This may take a while!]...")
    p = Pool(np)
    result = p.map(get_spei, datalist)
    p.close()

    # Writing to file
    print("Writing %d lines to file..." % len(result))

    fieldnames = ["Time", "Latitude", "Longitude", "SPEI"]

    with open(out, "w") as fn:
        writer = csv.DictWriter(fn, fieldnames=fieldnames, dialect="excel")
        writer.writeheader()

        for it in range(len(result)):
            writer.writerow(
                {
                    "Time": str(dtime.data[result[it][0][0]]),
                    "Latitude": lat[result[it][1][0]],
                    "Longitude": lon[result[it][2][0]],
                    "SPEI": result[it][3][0],
                }
            )
    print("Complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument("-inp", type=str, help="Input netcdf file name")
    parser.add_argument(
        "-out", type=str, help="Output file name", default="spei_converted.csv"
    )
    parser.add_argument("-np", type=int, help="Number of processors", default=1)
    args = parser.parse_args()
    main(args)
