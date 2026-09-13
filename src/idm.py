import traci
import math


# IDM参数

v0 = 15      # 期望速度 m/s

s0 = 5       # 最小距离 m

T = 1.5      # 反应时间 s

a = 1.5      # 最大加速度

b = 2        # 舒适减速度



def IDM(car_front, car_back):

    # 前车速度

    v_front = traci.vehicle.getSpeed(
        car_front
    )


    # 后车速度

    v = traci.vehicle.getSpeed(
        car_back
    )


    # 位置

    front_pos = traci.vehicle.getPosition(
        car_front
    )

    back_pos = traci.vehicle.getPosition(
        car_back
    )


    # 车辆间距

    s = front_pos[0] - back_pos[0]


    # 防止除0

    if s <= 0:
        return -10



    # 相对速度

    delta_v = v - v_front



    # 期望安全距离

    s_star = (
        s0
        + v*T
        + (v*delta_v)
        /
        (2*math.sqrt(a*b))
    )



    # IDM加速度公式

    acc = a * (
        1
        - (v/v0)**4
        - (s_star/s)**2
    )


    return acc