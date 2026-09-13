import traci
import csv
import time


print("SUMO测试开始")


traci.start([
    "sumo-gui",
    "-c",
    "simulation/test.sumocfg"
])


print("SUMO连接成功")


file = open("data.csv","w",newline="")

writer = csv.writer(file)


writer.writerow([
    "time",
    "car1_speed",
    "car2_speed",
    "distance",
    "TTC",
    "AEB"
])


from idm import IDM

from ttc import calculate_TTC

from aeb import AEB_control, AEB_TTC



for i in range(100):


    traci.simulationStep()

    time.sleep(0.2)



    # 控制前车

    if "car1" in traci.vehicle.getIDList():


        traci.vehicle.setSpeedMode("car1",0)


        if i < 30:

            traci.vehicle.setSpeed(
                "car1",
                10
            )

            print("前车正常行驶")


        else:

            traci.vehicle.setSpeed(
                "car1",
                5
            )

            print("前车开始减速")




    # 后车控制

    if "car1" in traci.vehicle.getIDList() and "car2" in traci.vehicle.getIDList():


        car1_pos = traci.vehicle.getPosition("car1")

        car2_pos = traci.vehicle.getPosition("car2")



        distance = abs(
            car1_pos[0]-car2_pos[0]
        )


        car1_speed = traci.vehicle.getSpeed("car1")

        car2_speed = traci.vehicle.getSpeed("car2")



        # 计算TTC

        ttc = calculate_TTC(
            distance,
            car1_speed,
            car2_speed
        )
        aeb_active = 0



        print(
            "距离:",
            round(distance,2),
            "TTC:",
            round(ttc,2)
            if ttc != float("inf")
            else "∞"
        )



        # 风险判断

        if ttc < AEB_TTC:

            aeb_active = 1

            print("危险碰撞风险")

            aeb_speed = AEB_control("car2")
        else:
            acc=IDM(
                "car1",
                "car2"
            )
            
            speed = traci.vehicle.getSpeed("car2")


            new_speed = speed + acc * 0.2


            if new_speed < 0:
                new_speed = 0


            traci.vehicle.setSpeed(
                "car2",
                new_speed
            )


            print(
                "IDM控制",
                "加速度:",
                round(acc,2),
                "速度:",
                round(new_speed,2)
            )





        # 写入CSV

        writer.writerow([

            round(i*0.2,2),

            round(car1_speed,2),

            round(car2_speed,2),

            round(distance,2),

            round(ttc,2),
            aeb_active
            if ttc != float("inf")
            else 999

        ])




    # 打印车辆状态

    for v in traci.vehicle.getIDList():

        print(
            "车辆:",
            v,
            "速度:",
            round(traci.vehicle.getSpeed(v),2),
            "位置:",
            traci.vehicle.getPosition(v)
        )



try:

    input("按回车关闭")


finally:

    file.close()

    traci.close()



print("测试结束")