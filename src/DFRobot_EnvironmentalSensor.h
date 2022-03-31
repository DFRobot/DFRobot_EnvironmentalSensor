/*!
 * @file  DFRobot_EnvironmentalSensor.h
 * @brief Basic structure of DFRobot_URM09 class, the implementation of basic method
 * @copyright	Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license   The MIT License (MIT)
 * @author    [TangJie](jie.tang@dfrobot.com)
 * @version   V1.0
 * @date      2021-08-31
 * @url       https://github.com/DFRobot/DFRobot_EnvironmentalSensor
 */

#ifndef DFROBOT_MULTIFUNCTIONAL_ENVIRONMENTAL_SENSOR_H
#define DFROBOT_MULTIFUNCTIONAL_ENVIRONMENTAL_SENSOR_H

#include "Arduino.h"
#include "Wire.h"
#include "DFRobot_RTU.h"
#include "String.h"

#if (defined ARDUINO_AVR_UNO) && (defined ESP8266)
#include "SoftwareSerial.h"
#else
#include "HardwareSerial.h"
#endif

//#define ENABLE_DBG ///< 打开这个宏, 可以看到程序的详细运行过程
#ifdef ENABLE_DBG
#define DBG(...) {Serial.print("[");Serial.print(__FUNCTION__); Serial.print("(): "); Serial.print(__LINE__); Serial.print(" ] "); Serial.println(__VA_ARGS__);}
#else
#define DBG(...)
#endif

#ifndef RTU_BROADCAST_ADDRESS
#define RTU_BROADCAST_ADDRESS                      0x00 ///< Broadcast address of the modbus protocol is 0x00
#endif
#define SEN050X_DEFAULT_DEVICE_ADDRESS             0x22 ///< Default device address of SEN0500/SEN0501 sensor is 0x22

class DFRobot_EnvironmentalSensor: public DFRobot_RTU{

public:
#define DEVICE_PID_GRAVITY   0x01F5
#define DEVICE_PID_BREAKOUT  0x01F4
#define DEVICE_VID           0x3343

#define HPA                  0x01 ///< Atmospheric pressure Hectopascal
#define KPA                  0X02 ///< Atmospheric pressure Kilopascal

#define TEMP_C                    0X03  ///< ℃
#define TEMP_F                    0X04  ///< ℉

#define REG_PID                   0x0000 ///< Register for protocol transition adapter
#define REG_VID                   0x0001 ///< Register for protocol transition adapter
#define REG_DEVICE_ADDR           0x0002 ///< Register for protocol transition adapter
#define REG_UART_CTRL0            0x0003 ///< Register for protocol transition adapter
#define EG_UART_CTRL1             0x0004 ///< Register for protocol transition adapter
#define REG_VERSION               0x0005 ///< Register for protocol transition adapter

#define REG_ULTRAVIOLET_INTENSITY 0x0008 ///< Register for protocol transition adapter
#define REG_LUMINOUS_INTENSITY    0x0009 ///< Register for protocol transition adapter
#define REG_TEMP                  0x000A ///< Register for protocol transition adapter
#define REG_HUMIDITY              0x000B ///< Register for protocol transition adapter
#define REG_ATMOSPHERIC_PRESSURE  0x000C ///< Register for protocol transition adapter
#define REG_ELEVATION             0x000D ///< Register for protocol transition adapter



  /**
   * @fn DFRobot_EnvironmentalSensor
   * @brief DFRobot_EnvironmentalSensor constructor
   * @param pWire I2C pointer to the TowWire stream, which requires calling begin in the demo to init Arduino I2C config.
   * @param addr  I2C communication address of SEN0500/SEN0501 device
   */
  DFRobot_EnvironmentalSensor(uint8_t addr, TwoWire *pWire = &Wire);

  /**
   * @fn DFRobot_EnvironmentalSensor
   * @brief DFRobot_EnvironmentalSensor constructor
   * @param addr: The device address of the communication between the host computer and SEN0500/SEN0501 slave device
   * @n     SEN0501_DEFAULT_DEVICE_ADDRESS or 32（0x20）: Default address of SEN0500/SEN0501 device, if users do not change the device address, it's default to 32.
   * @param s   : The serial port pointer to the Stream, which requires calling begin in the demo to init communication serial port config of Arduino main controller, in line with that of SEN0500/SEN0501 device slave.
   * @n SEN0500/SEN0501 serial port config: 9600 baud rate, 8-bit data bit, no check bit, 1 stop bit, the parameters can't be changed.
   */
  DFRobot_EnvironmentalSensor(uint8_t addr, Stream *s);
  ~DFRobot_EnvironmentalSensor(){};

  /**
   * @fn begin
   * @brief Init SEN0500/SEN0501 sensor
   * @return Return value init status
   * @retval 0  Succeed
   * @retval -1 Failed
   */
  int8_t begin(void);

  /**
   * @fn getTemperature
   * @brief Get SEN0500/SEN0501 temperature data
   * @param units Temperature data unit select
   * @n     TEMP_C ℃
   * @n     TEMP_F ℉ 
   * @return Return the obtained temperature data
   */
  float getTemperature(uint8_t unist);

  /**
   * @fn getHumidity
   * @brief Get SEN0500/SEN0501 humidity data 
   * @return Return the obtained humidity data
   */
  float getHumidity(void);

  /**
   * @fn getUltravioletIntensity
   * @brief Get SEN0500/SEN0501 ultraviolet intensity index data 
   * @return Return the obtained ultraviolet intensity index data
   */
  float getUltravioletIntensity(void);

  /**
   * @fn getLuminousIntensity
   * @brief Get SEN0500/SEN0501 luminous intensity data 
   * @return Return the obtained luminous intensity data
   */
  float getLuminousIntensity(void);

  /**
   * @fn getAtmospherePressure
   * @brief Get SEN0500/SEN0501 atmosphere pressure data 
   * @param units Atmosphere pressure data unit select
   * @n            HPA Hectopascal
   * @n            KPA Kilopascal
   * @return Return the obtained atmosphere pressure data
   */
  uint16_t getAtmospherePressure(uint8_t units);

  /**
   * @fn getElevation
   * @brief Get SEN0500/SEN0501 elevation data 
   * @return Return the obtained elevation data
   */
  float getElevation(void);


protected:
  uint16_t getDevicePID();
  float mapfloat(float x, float in_min, float in_max, float out_min, float out_max);
  uint16_t getDeviceVID();
  uint8_t  readReg(uint16_t reg, void *pBuf, uint8_t size);
  bool detectDeviceAddress(uint8_t addr);
  
protected:
  TwoWire   *_pWire = NULL;
  Stream    *_s = NULL;
  uint8_t   _addr;

};

#endif
