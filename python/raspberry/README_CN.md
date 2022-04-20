DFRobot_EnvironmentalSensor
===========================

* [English Version](./README.md)

SEN0500/SEN0501 是一个气象传感器，模块上集成了，紫外线传感器、光照传感器、大气压强传感器、温湿度传感器，模块有Gravity接口和Breakout两种接口方式，通过串口或I2C进行数据传输，通过模块上的切换开关进行通信方式选择。
DFRobot_Environmental_Sensor库是DFRobot专门为该传感器写的一个Arduino驱动库，用户可以用此驱动库来驱动Ardunio主控连接的传感器获取传感器数据。

![产品效果图片](../../resources/images/SEN0501.png)
![产品效果图片](../../resources/images/SEN0500.png)

## 产品链接（https://www.dfrobot.com）

    SKU：SEN0500/SEN0501
  
## 目录

  * [概述](#概述)
  * [库安装](#库安装)
  * [方法](#方法)
  * [兼容性](#兼容性)
  * [历史](#历史)
  * [创作者](#创作者)

## 概述

这是一个多气象传感器得库，使用该库能够很便捷得获取温度、湿度、压强、紫外线强度、自然光线强度和海拔等信息，
模块还提供了Gravity版本和breakout版本方便使用。


## 库安装

要使用这个库，首先将库下载到Raspberry Pi，然后打开例程文件夹。要执行一个例程demox.py，请在命令行中输入python demox.py。例如，要执行control_led.py例程，你需要输入:

```python
python control_led.py
```



## 方法

```python
'''!
    @brief 初始化SEN0500/SEN0501传感器
    @brief 初始化SEN0500/SEN0501传感器
    @return 返回值初始化状态
    @retval 0  成功
    @retval -1 失败
  '''
  def begin(self):

  '''!
    @brief 获取SEN0500/SEN0501温度数据
    @param units 温度数据单位选择
    @n     TEMP_C 摄氏度
    @n     TEMP_F 华氏度 
    @return 返回获取的温度数据
  '''
  def get_temperature(self,unist):

  '''!
    @brief 获取SEN0500/SEN0501湿度数据 
    @return 返回获取的湿度数据
  '''
  def get_humidity(self):

  '''!
    @brief 获取SEN0500/SEN0501紫外线强度指数数据 
    @return 返回获取的紫外线强度指数数据
  '''
  def get_ultraviolet_intensity(self):

  '''!
    @brief 获取SEN0500/SEN0501光线强度数据 
    @return 返回获取的光线强度数据
  '''
  def get_luminousintensity(self):

  '''!
    @brief 获取SEN0500/SEN0501大气压强数据 
    @param units 大气压强数据单位选择
    @n            HPA 百帕
    @n            KPA 千帕
    @return 返回获取的大气压强数据
  '''
  def get_atmosphere_pressure(self, units):

  '''!
    @brief 获取SEN0500/SEN0501海拔数据 
    @return 返回获取的海拔数据
  '''
  def get_elevation(self):
```

## Compatibility

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |     √     |            |          |         |
| RaspberryPi4 |           |            |     √    |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |

## History

- 2021-08-31 - 1.0.0 版本

## Credits

Written by TangJie(jie.tang@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))