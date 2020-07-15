#!/usr/bin/env python

cpdef cython_append(df, result, dtime, lat, lon):

    cdef int it

    for it in range(len(result)):
                df = df.append(
                    {
                        "Time": str(dtime.data[result[it][0][0]]),
                        "Latitude": lat[result[it][1][0]],
                        "Longitude": lon[result[it][2][0]],
                        "SPEI": result[it][3][0],
                    },
                    ignore_index=True,
                )

    return df
