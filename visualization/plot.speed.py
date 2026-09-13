import pandas as pd
import matplotlib.pyplot as plt


# 读取数据

data = pd.read_csv("data.csv")


time = data["time"]


# ===================
# 速度曲线
# ===================

plt.figure(figsize=(8,4))

plt.plot(
    time,
    data["car1_speed"],
    label="car1"
)

plt.plot(
    time,
    data["car2_speed"],
    label="car2"
)


plt.xlabel("Time(s)")
plt.ylabel("Speed(m/s)")

plt.title("Vehicle Speed")

plt.legend()

plt.grid()

plt.show()



# ===================
# 跟车距离
# ===================


plt.figure(figsize=(8,4))


plt.plot(
    time,
    data["distance"]
)


plt.xlabel("Time(s)")
plt.ylabel("Distance(m)")


plt.title(
    "Following Distance"
)


plt.grid()

plt.show()



# ===================
# TTC风险
# ===================


plt.figure(figsize=(8,4))


plt.plot(
    time,
    data["TTC"]
)


plt.xlabel("Time(s)")
plt.ylabel("TTC(s)")


plt.title(
    "Time To Collision"
)


plt.grid()


plt.show()