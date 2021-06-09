"""Process data from the Nigeria Schools datsets 
Row information
===============
row[0]  = state_code
row[1]  = Source
row[2]  = name
row[3]  = ward_code
row[4]  = category
row[5]  = subtype
row[6]  = management
row[7]  = education
row[8]  = poi_type
row[9]  = global_id
row[10] = id
row[11] = no_of_teachers
row[12] = no_of_students
row[13] = Geometry
row[14] = Latitude
row[15] = Longitude
"""

import pandas as pd
import geopandas as gdp
import json
import csv
import argparse
import sys
import os




df = gdp.read_file("private-schools.geojson")
split_geo = df.Geometry.str.strip('POINT (').str.strip(')').str.split(' ')
df['Latitude'] = split_geo.apply(lambda x: x[0])
df['Longitude'] = split_geo.apply(lambda x: x[1])
df.head(2)
