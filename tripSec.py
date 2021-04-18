"""
Author: Henry Keena
License: MIT
Version: 1.0
Description: Script for Raspberry Pi Laser Trip Wire System
"""

#Imports gpiozero Library
from gpiozero import LightSensor

#Imports sleep Function from time Library
from time import sleep


"""
- Work & Logic Code for execution after the laser wire has been tripped should be written/defined here.
- Examples can include camera modules, buzzers, audio playing, etc.
"""


"""
Function: main()
Description: Main Function
"""
def main():
    ldr = LightSensor(4)
    while True:
        sleep(0.15)
        if ldr.value < 0.5:
            print("Laser Tipped")
            #Insert Work/Logic Code
        else:
            print("Laser Not Tripped")
            #Insert Debug Code

    
#Calls Main Function
if __name__ == "__main__":
    main()

