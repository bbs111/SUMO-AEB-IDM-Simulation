# SUMO ACC-AEB Simulation

基于 SUMO 与 TraCI 的智能驾驶纵向控制仿真平台。

实现车辆跟驰控制、碰撞风险评估以及自动紧急制动功能。


## Features

- SUMO交通仿真环境搭建
- TraCI实时车辆控制
- IDM车辆跟驰模型
- 安全距离控制
- TTC(Time To Collision)碰撞风险评估
- AEB自动紧急制动策略


## System Architecture


SUMO Simulation

↓

TraCI Controller

↓

Vehicle Longitudinal Control

↓

IDM Model

↓

TTC Risk Evaluation

↓

AEB Emergency Braking



## Algorithm


### IDM

实现智能驾驶车辆跟驰模型：

- 期望速度控制
- 安全距离保持
- 加速度调整


### TTC

碰撞时间：

TTC = Distance / Relative Velocity


当TTC低于阈值时：

触发风险预警。


### AEB

当：

TTC < 1.5s


系统自动降低车辆速度，实现紧急制动。


## Environment


Python 3.x

SUMO

TraCI



## Run


启动仿真：

```bash
python src/main.py