# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:50:38 2018
Streams mouse position and RGB data where the mouse is pointed.
Continuous - close by closing console.
https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=2017-03-01T00:00:00Z&endtime=2017-03-31T23:59:59Z&shape=state_dept_countries/shp_185&bbox=50.5371,24.3237,51.7676,26.2573&data=OMDOAO3e_003_ColumnAmountO3&variableFacets=dataFieldMeasurement%3AOzone%3B
@author: Brian
"""
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print positionStr,''
        print '\b' * len(positionStr),''
except KeyboardInterrupt:
    print'\n'