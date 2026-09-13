import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv("data.csv")


time = data["time"]
ttc = data["TTC"]


plt.figure(figsize=(10,5))


plt.plot(
    time,
    ttc,
    label="TTC"
)


# 风险阈值线

plt.axhline(
    y=3,
    linestyle="--",
    label="High Risk"
)


plt.axhline(
    y=1.5,
    linestyle="--",
    label="Danger"
)



plt.xlabel("Time(s)")

plt.ylabel("TTC(s)")


plt.title(
    "Time To Collision Analysis"
)


plt.legend()

plt.grid()


plt.show()