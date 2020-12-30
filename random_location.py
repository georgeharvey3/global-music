#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:04:13 2020

@author: george
"""

# imports
import re
import random
import shapefile
from shapely.geometry import shape, Point
import sys

# function that takes a shapefile location and a country name as inputs
def random_point_in_country(shp_location, country_name):
    shapes = shapefile.Reader(shp_location) # reading shapefile with pyshp library
    try:
        country = [s for s in shapes.records() if country_name in s][0] # getting feature(s) that match the country name 
    except:
        print(country_name)
        return 'None'
    country_id = int(re.findall(r'\d+', str(country))[0]) # getting feature(s)'s id of that match

    shapeRecs = shapes.shapeRecords()
    feature = shapeRecs[country_id].shape.__geo_interface__

    shp_geom = shape(feature)

    minx, miny, maxx, maxy = shp_geom.bounds
    while True:
        p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
        if shp_geom.contains(p):
            return str(p.x) + ", " + str(p.y)


if __name__ == '__main__':
    print(random_point_in_country('World_Countries.shp', sys.argv[1]))