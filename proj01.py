#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:53:07 2018

@author: nicksimerson
"""

input_str = input("Input rods: ")
rodfloat = float(input_str)

print("You input:", rodfloat, "rods.")

print("Conversions")

meters = (rodfloat*5.0292)
metersrd = round(meters,3)
print("Meters:",metersrd)

feet = (meters/.3048)
feetrd = round(feet,3)
print("Feet:", feetrd)

miles = (meters/1609.34)
milesrd = round(miles,3)
print("Miles:", milesrd)

furlongs = (rodfloat/40)
furlongsrd = round(furlongs,3)
print("Furlongs:", furlongsrd)

mintowalk = (miles/3.1*60)
mintowalkrd = round(mintowalk,3)
print("Minutes to walk",rodfloat , "rods:", mintowalkrd)