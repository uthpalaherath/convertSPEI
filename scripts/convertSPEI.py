#!/usr/bin/env python

"""
SPEI data converter.

This script converts SPEI time series data in netcdf format
retrieved from https://spei.csic.es to Excel or csv formats.

Note: Although parallelized,  for large datasets the conversion
might take a while.

- Uthpala Herath
  July, 2020

Usage:

$ convertSPEI.py -inp spei01.nc -np 4 -type excel

convertSPEI.py -h brings up the help menu.

"""

import netCDF4
import pandas as pd
import sys
from multiprocessing import Pool
import argparse
from argparse import RawTextHelpFormatter


class Converter:
    """
    This class contains methods to perform the conversion.
    """

    def __init__(self, args):
        print("----------------------------------")
        print("\nSPEI data converter")
        print("\nAuthor: Uthpala Herath")
        print("https://github.com/uthpalaherath")
        print("----------------------------------")
        print("\nRunning on %d cores..." % args.np)

        self.inp = args.inp
        self.out = args.out
        self.np = args.np
        self.type = args.type

        spei_nc_file = self.inp
        nc = netCDF4.Dataset(spei_nc_file, mode="r")

        self.lat = nc.variables["lat"][:]
        self.lon = nc.variables["lon"][:]
        rawtime = nc.variables["time"]
        self.dtime = netCDF4.num2date(rawtime[:], rawtime.units)
        self.spei = nc.variables["spei"][:]

        nc.close()

        self.dtime_retlist = []
        self.lat_retlist = []
        self.lon_retlist = []
        self.spei_retlist = []

        # Calling main function
        self.main()

    def get_spei(self, datalist):
        """
        this method returns the SPEI value given
        time, latitude and longitude indexes i,j,k.
        """

        self.dtime_retlist.append(datalist[0])
        self.lat_retlist.append(datalist[1])
        self.lon_retlist.append(datalist[2])
        self.spei_retlist.append(self.spei.data[datalist[0], datalist[1], datalist[2]])

        return self.dtime_retlist, self.lat_retlist, self.lon_retlist, self.spei_retlist

    def main(self):

        # Creating array for calling get_spei() in parallel.
        print("\nCreating data list...")
        datalist = []
        for i in range(len(self.dtime)):
            for j in range(len(self.lat)):
                for k in range(len(self.lon)):
                    datalist.append([i, j, k])

        # Calling get_spei to get spei value and append
        # to dataframe
        print("Indexing SPEI data [This may take a while!]...")
        p = Pool(self.np)
        result = p.map(self.get_spei, datalist)
        p.close()

        # creating dataframe
        print("Updating dataframe...")
        df = pd.DataFrame(columns=["Time", "Latitude", "Longitude", "SPEI"],)

        for it in range(len(result)):
            df = df.append(
                {
                    "Time": str(self.dtime.data[result[it][0][0]]),
                    "Latitude": self.lat[result[it][1][0]],
                    "Longitude": self.lon[result[it][2][0]],
                    "SPEI": result[it][3][0],
                },
                ignore_index=True,
            )

        # Saving dataframe to output file
        df.sort_values(by=["Time"])
        print("Writing to file...")
        if self.type == "excel":
            df.to_excel(self.out, index=False)
        elif self.type == "csv":
            df.to_csv(self.out, index=False)
        print("Complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument("-inp", type=str, help="Input netcdf file name")
    parser.add_argument(
        "-out", type=str, help="Output file name", default="spei_converted.xlsx"
    )
    parser.add_argument(
        "-type",
        type=str,
        help="Output format",
        default="excel",
        choices=["excel", "csv"],
    )
    parser.add_argument("-np", type=int, help="Number of processors", default=1)
    args = parser.parse_args()
    Converter(args)
