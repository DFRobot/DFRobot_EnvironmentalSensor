# -*- coding: utf-8 -*
'''!
  @file  read_data.py
  @brief This demo shows how to get data of the SEN0500/SEN0501 sensor and outputs data through I2C or UART.
  @n Print the data returned by SEN0500/SEN0501 in the serial port monitor.
  @copyright   Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      TangJie(jie.tang@dfrobot.com)
  @version     V1.0
  @date        2021-08-31
  @url         https://github.com/DFRobot/DFRobot_EnvironmentalSensor
'''
import sys
import os
import time
import RPi.GPIO as GPIO

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from dfrobot_environmental_sensor import *

'''
  Select communication mode
  ctype=1：UART
  ctype=0：IIC
'''
ctype=1

ADDRESS = 0x22  
I2C_1   = 0x01               
if ctype==0:
  SEN0500/SEN0501 = DFRobot_Environmental_Sensor_I2C(I2C_1 ,ADDRESS)
else:
  SEN0500/SEN0501 = DFRobot_Environmental_Sensor_UART(9600, ADDRESS)

'''
  Atmospheric pressure unit select
'''
HPA                       = 0x01
KPA                       = 0X02

'''
  Temperature unit select
'''
TEMP_C                    = 0X03
TEMP_F                    = 0X04
 
def setup():
  while (SEN0500/SEN0501.begin() == False):
    print("Sensor initialize failed!!")
    time.sleep(1)
  print("Sensor  initialize success!!")
  
def loop():
  ##Obtain sensor data
  print("-----------------------\r\n")
  print("Temp: " + str(SEN0500/SEN0501.get_temperature(TEMP_C)) + " 'C\r\n")
  print("Temp: " + str(SEN0500/SEN0501.get_temperature(TEMP_F)) + " 'F\r\n")
  print("Humidity: " + str(SEN0500/SEN0501.get_humidity()) + " %\r\n")
  print("Ultraviolet intensity: " + str(SEN0500/SEN0501.get_ultraviolet_intensity()) + " mw/cm2\r\n")
  print("LuminousIntensity: " + str(SEN0500/SEN0501.get_luminousintensity()) + " lx\r\n")
  print("Atmospheric pressure: " + str(SEN0500/SEN0501.get_atmosphere_pressure(HPA)) + " hpa\r\n")
  print("Elevation: " + str(SEN0500/SEN0501.get_elevation()) + " m\r\n")
  print("-----------------------\r\n")
  time.sleep(1)

if __name__ == "__main__":
  setup()
  while True:
    loop()
    
