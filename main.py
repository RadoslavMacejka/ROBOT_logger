import matplotlib.pyplot as plt
import csv

import numpy
import numpy as np

ODO_l = []
ODO_r = []
sensor_1 = []
sensor_2 = []
sensor_3 = []
sensor_4 = []
sensor_5 = []
sensor_6 = []
voltage_raw = []

def normalize(raw_signal):
    return (raw_signal - np.min(raw_signal)) / (np.max(raw_signal) - np.min(raw_signal))

def ustep2m(raw_signal):
    return raw_signal


directory = '/home/radoslav/robot/cmake-build-debug/logs/'

last_log_txt = open(directory + "last_log.txt", "r")
last_log = last_log_txt.read()
last_log_txt.close()

file = directory + last_log

# file = "/home/radoslav/robot/cmake-build-debug/logs/ROBOT log Thu Mar 23 10:07:08 2023.csv"


with open(file, 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        voltage_raw.append(int(row[0]))
        sensor_1.append(int(row[1]))
        sensor_2.append(int(row[2]))
        sensor_3.append(int(row[3]))
        sensor_4.append(int(row[4]))
        ODO_l.append(float(row[5]))
        ODO_r.append(float(row[6]))

sensor_1 = sensor_1[1:]
sensor_2 = sensor_2[1:]
sensor_3 = sensor_3[1:]
sensor_4 = sensor_4[1:]
ODO_l = ODO_l[1:]
ODO_r = ODO_r[1:]

ODO_l = numpy.float64(ODO_l)

plt.figure()
plt.title("raw signals")
plt.plot(ODO_l,sensor_1,label = "sensor 1")
plt.plot(ODO_l,sensor_2,label = "sensor 2")
plt.plot(ODO_l,sensor_3,label = "sensor 3")
plt.plot(ODO_l,sensor_4,label = "sensor 4")
plt.legend()
plt.xlabel("m")
plt.ylabel("ADC value")


plt.figure()
plt.title("normalized signals")
zero = 0.2247
# plt.plot(ODO_l-zero,normalize(sensor_1)/100,label = "sensor 1")
# plt.plot(ODO_l-zero,normalize(sensor_2)/100,label = "sensor 2")
# plt.plot(ODO_l-zero,normalize(sensor_3)/100,label = "sensor 3")
# plt.plot(ODO_l-zero,normalize(sensor_4)/100,label = "sensor 4")
plt.plot(ODO_l-zero,(normalize(sensor_1) - normalize(sensor_3))/100,label = "sensor 1 - 3 ")
plt.plot(ODO_l-zero,((normalize(sensor_1) - normalize(sensor_3))/100)+(ODO_l-zero) ,label = "error")
plt.xlabel("m")
plt.ylabel("m")
plt.xlim(-0.03,0.03)
plt.ylim(-0.015,0.015)
plt.grid()
plt.legend()




plt.show()