# -*- coding: utf-8 -*
'''!
  @file        dfrobot_environmental_sensor.py
  @brief       DFRobot_EnvironmentalSensor library is developed for DFRobot environmental sensor.
  @copyright   Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      TangJie(jie.tang@dfrobot.com)
  @version     V1.0
  @date        2021-08-31
  @url         https://github.com/DFRobot/DFRobot_EnvironmentalSensor
'''

import serial
import time
import smbus
import os
import math
import RPi.GPIO as GPIO
import math

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

I2C_MODE                  = 0x01
UART_MODE                 = 0x02
DEV_ADDRESS               = 0x22

DEVICE_VID                = 0x3343
DEVICE_ADDRESS            = 0x22

HPA                       = 0x01
KPA                       = 0X02
TEMP_C                    = 0X03
TEMP_F                    = 0X04

class DFRobot_Environmental_Sensor():
  '''!
    @brief Define DFRobot_Environmental_Sensor basic class
    @details For driving the environmental sensor
  '''
  def __init__(self ,bus ,baud = 9600):
    if bus != 0:
      self.i2cbus = smbus.SMBus(bus)
      self._uart_i2c = I2C_MODE
      
    else:
      self.master = modbus_rtu.RtuMaster(serial.Serial(port="/dev/ttyAMA0",baudrate=baud, bytesize=8, parity='N', stopbits=1))
      self.master.set_timeout(1.0)
      self._uart_i2c = UART_MODE
  
  def _detect_device_address(self):
    '''!
      @brief Get sensor address
      @return  Return sensor address
    '''
    rbuf = self._read_reg(0x04,2)
    if self._uart_i2c == I2C_MODE:
      data = rbuf[0] << 8 | rbuf[1]
    elif self._uart_i2c == UART_MODE:
      data = rbuf[0]
    return data

  
  def begin(self):
    '''!
      @brief Init SEN0500/SEN0501 sensor
      @return Return init status
      @retval 0  Succeed
      @retval -1 Failed
    '''
    if self._detect_device_address() != DEV_ADDRESS:
      return False
    return True

  
  def get_temperature(self,unist):
    '''!
      @brief Get SEN0500/SEN0501 temperature data
      @param units Temperature data unit select
      @n     TEMP_C ℃
      @n     TEMP_F ℉ 
      @return Return the obtained temperature data
    '''
    rbuf = self._read_reg(0x14, 2)
    if self._uart_i2c == I2C_MODE:
      data = rbuf[0] << 8 | rbuf[1]
    elif self._uart_i2c == UART_MODE:
      data = rbuf[0]
    temp = (-45) +((data * 175.00) / 1024.00 / 64.00)
    if(unist == TEMP_F):
      temp = temp * 1.8 + 32 
    return round(temp,2)
    
  
  def get_humidity(self):
    '''!
      @brief Get SEN0500/SEN0501 humidity data 
      @return Return the obtained humidity data
    '''
    rbuf = self._read_reg(0x16, 2)
    if self._uart_i2c == I2C_MODE:
      humidity = rbuf[0] << 8 | rbuf[1]
    elif self._uart_i2c == UART_MODE:
      humidity = rbuf[0]
    humidity = (humidity / 1024) * 100 / 64
    return humidity
  
 
  def get_ultraviolet_intensity(self):
    '''!
      @brief Get SEN0500/SEN0501 UV intensity index data 
      @return Return the obtained UV intensity index data
    '''
    version = self.self._read_reg(0x05, 2)
    if (version[0] << 8 | version[1]) == 0x1001:
      rbuf = self._read_reg(0x10, 2)
      data = rbuf[0] << 8 | rbuf[1]
      ultraviolet = data / 1800
    else:
      rbuf = self._read_reg(0x10, 2)
      if self._uart_i2c == I2C_MODE:
        data = rbuf[0] << 8 | rbuf[1]
      elif self._uart_i2c == UART_MODE:
        data = rbuf[0]
      outputVoltage = 3.0 * data/1024
      ultraviolet = (outputVoltage - 0.99) * (15.0 - 0.0) / (2.9 - 0.99) + 0.0 
    return round(ultraviolet,2)
      
  
  def get_luminousintensity(self):
    '''!
      @brief Get SEN0500/SEN0501 luminous intensity data 
      @return Return the obtained luminous intensity data
    '''
    rbuf = self._read_reg(0x12 ,2)
    if self._uart_i2c == I2C_MODE:
      data = rbuf[0] << 8 | rbuf[1]
    elif self._uart_i2c == UART_MODE:
      data = rbuf[0]
    luminous = data * (1.0023 + data * (8.1488e-5 + data * (-9.3924e-9 + data * 6.0135e-13)))
    return round(luminous,2)

  
  def get_atmosphere_pressure(self, units):
    '''!
      @brief Get SEN0500/SEN0501 atmosphere pressure data 
      @param units Atmosphere pressure data unit select
      @n            HPA Hectopascal
      @n            KPA Kilopascal
      @return Return the obtained atmosphere pressure data
    '''
    rbuf = self._read_reg(0x18, 2)
    if self._uart_i2c == I2C_MODE:
      atmosphere = rbuf[0] << 8 | rbuf[1]
    elif self._uart_i2c == UART_MODE:
      atmosphere = rbuf[0]
    if units == KPA:
      atmosphere /= 10
    return atmosphere

  
  def get_elevation(self):
    '''!
      @brief Get SEN0500/SEN0501 elevation data 
      @return Return the obtained elevation data
    '''
    rbuf = self._read_reg(0x18, 2)
    if self._uart_i2c == I2C_MODE:
      elevation = rbuf[0] << 8 | rbuf[1]
    elif self._uart_i2c == UART_MODE:
      elevation = rbuf[0]
    elevation = 44330 * (1.0 - pow(elevation / 1015.0, 0.1903));
    return round(elevation,2)

  
        

class DFRobot_Environmental_Sensor_I2C(DFRobot_Environmental_Sensor):
  '''!
    @brief An example of an i2c interface module
  '''
  def __init__(self ,bus ,addr):
    self._addr = addr
    DFRobot_Environmental_Sensor.__init__(self,bus,0)   
    
  
  def _read_reg(self, reg_addr ,length):
    '''!
      @brief read the data from the register
      @param reg register address
      @param value read data
    '''
    try:
      rslt = self.i2cbus.read_i2c_block_data(self._addr ,reg_addr , length)
    except:
      rslt = -1
    return rslt    


class DFRobot_Environmental_Sensor_UART(DFRobot_Environmental_Sensor):
  '''!
    @brief An example of an UART interface module
  '''
  def __init__(self ,baud, addr):
    self._baud = baud
    self._addr = addr
    try:
      DFRobot_Environmental_Sensor.__init__(self,0,self._baud)
    except:
      print ("plese get root!")
   
  
  def _read_reg(self, reg_addr ,length):
    '''!
      @brief Read data from the sensor
    '''
    return list(self.master.execute(self._addr, cst.READ_INPUT_REGISTERS, reg_addr/2, length/2))
    
    
