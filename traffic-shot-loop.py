# -*- coding: utf-8 -*-
"""
Created on Sun Jan 06 11:50:53 2019

@author: CALPUFF
Midpoint locator removed

"""

from selenium import webdriver
import time
import datetime
from datetime import date
import pandas as pd
import pyautogui
import sys

def twospace(x):
#### adds a 0 to month or day less than 10 (1 -> 01)
    if len(x) == 1:
        x = '0'+str(x)
    return x

##### uses selenium to take screenshot of map and save.
##### webdriver should be in the same folder
##### comment out when not being used
while 1:
    try:
        driver = webdriver.Chrome()
        
        road_lat = ['29.2452651']
        road_long = ['48.0915586']
        
        tile_list = [] ### make a list with file names of screenshot tiles
        
        zoom = '14.25z'  #### set zoom scale

        tile1 = 'https://www.google.com/maps/place/'
        tile2 = '\@' + road_lat[0] + ',' + road_long[0] + ',' + zoom + '/data=!4m5!3m4!1s0x0:0x0!8m2!3d'
        tile3 = road_lat[0] + '!4d' + road_long[0] + '!5m1!1e1'
        
        road_tile = tile1 + tile2 + tile3
        #road_tile = 'https://www.google.com/maps/@29.2859526,47.9549992,13.25z'
       
        driver.get(road_tile)
        driver.refresh()
        
        time.sleep(5)  ### wait for map to load
        pyautogui.click(976, 25, button='left')  #maximize window#1
        time.sleep(.5)   ### wait for tab to clear
        pyautogui.click(528, 134, button='left')  #move cursor to button location and click to hide tab try #2
        time.sleep(.5)   ### wait for tab to clear
        
        pyautogui.click(1176, 144, button='left')  #hide box
        time.sleep(1)   ### wait for screen to expand
        
        #### make timestamp
        time1 = str(time.clock())  #add timestamp for unique name
        time1 = time1[0:4] 
        today1 = date.today().timetuple()
        today_str = str(today1.tm_year) + twospace(str(today1.tm_mon))+twospace(str(today1.tm_mday))+time1
        
        tile_name = 'kw20-'+ zoom +'-'+ today_str   #make file name with lat/long coord
       
        #### remove extra '.' from filename
        tile_name = tile_name.replace(".", "",) + '.png'
        
        ### take screenshot        
        driver.save_screenshot(tile_name)
        
        time.sleep(5)  ### delay
        
        ## append list of tile names after you replace the comma separater with an underscore
        tile_list.append(tile_name.replace(",", "_")) 
            
        print "Image saved as " + tile_name, "on {:%Y-%b-%d %H:%M:%S}".format(datetime.datetime.now())
             
        driver.quit()
        
        #### add delay and countdown timer
        delay = 1800
        for i_sleep in range (delay):
            ### delay for 30 minutes (1800 sec) - check every 1 sec            
            mins, secs = divmod(delay-i_sleep, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            sys.stdout.write('\r'+timeformat+' till next screenshot')
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write('\r                                        ')
        sys.stdout.flush()
    
    except KeyboardInterrupt:
        break