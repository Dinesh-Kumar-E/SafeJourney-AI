
import matplotlib.pyplot as plt 
import random

  
  
x = list(range(0, 60))
y_act = []
y_act.extend([1]*15)
y_act.extend([0]*15)
y_act.extend([1]*15)
y_act.extend([0]*15)


y_dlib = []

y_dl = []


import matplotlib.pyplot as plt
import numpy as np

# Sample data for two graphs
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)


y_dlib = ((3.4,69.8),
(5.1,69.7),
(4.0,69.8),
(3.4,69.7),
(4.0,69.8),
(2.7,69.8),
(2.7,69.7),
(3.6,69.7),
(5.1,69.6),
(3.8,69.6),
(3.9,69.7),
(3.9,69.7),
(5.4,69.7),
(4.2,69.6),
(2.1,69.6),
(3.9,69.7),
(3.3,69.7),
(3.7,69.7),
(4.0,69.7),
(3.4,69.8),
(4.1,69.8),
(3.5,70.0),
(2.7,70.0),
(3.8,70.0),
(3.2,70.1),
(3.8,70.1),
(3.4,70.1),
(3.9,70.1),
(4.2,70.0),
(3.1,70.0),
(3.9,70.0),
(3.9,70.0),
(4.1,70.0),
(3.5,70.1),
(3.5,70.0),
(4.0,70.0),
(3.8,69.8),
(3.9,69.4),
(4.0,69.4),
(3.9,69.2),
(4.7,69.3),
(3.9,69.3),
(3.8,69.3),
(3.6,69.3),
(3.8,69.4),
(3.6,69.3),
(3.3,69.4),
(3.8,69.7),
(3.7,69.6),
(4.8,69.7),
(3.4,69.6),
(3.4,69.7),
(2.5,69.7),
(4.2,69.7),
(4.6,69.7),
(3.9,69.7),
(3.6,69.8),
(5.1,69.0),
(5.1,68.7),
(3.8,68.7))

y_dl = ((5.8,73.3),
(4.9,73.3),
(4.2,73.3),
(6.4,73.2),
(6.5,73.3),
(3.8,73.3),
(6.1,73.4),
(5.8,73.5),
(3.8,73.6),
(4.6,73.7),
(6.5,73.6),
(5.7,73.7),
(5.2,73.7),
(6.9,73.8),
(3.9,74.0),
(4.8,74.1),
(5.7,74.1),
(4.3,74.0),
(4.7,74.1),
(5.5,74.2),
(7.0,74.2),
(6.5,74.3),
(5.6,74.4),
(4.4,74.5),
(4.3,74.6),
(4.3,74.7),
(6.5,74.7),
(5.5,74.8),
(3.9,75.0),
(6.8,75.1),
(4.3,75.1),
(4.3,75.1),
(6.0,75.3),
(5.3,75.3),
(7.2,75.4),
(4.3,75.5),
(5.2,75.5),
(7.2,76.1),
(7.2,76.3),
(9.0,76.0),
(5.3,75.8),
(5.1,74.8),
(4.3,75.0),
(12.5,75.5),
(9.5,75.7),
(5.6,75.8),
(6.9,75.7),
(7.3,75.9),
(5.4,75.8),
(5.5,75.8),
(6.2,75.7),
(8.1,75.6),
(6.8,75.7),
(6.2,75.7),
(6.1,75.8),
(6.0,75.8),
(6.2,75.9),
(6.3,75.9),
(7.3,76.0),
(6.7,76.0))


x = list(range(0, 60))
cpu_db = list(map(lambda x: x[0], y_dlib))
mem_db = list(map(lambda x: x[1], y_dlib))
cpu_dl = list(map(lambda x: x[0], y_dl))
mem_dl = list(map(lambda x: x[1], y_dl))
# Create a subplot with 1 row and 2 columns
plt.subplot(1, 2, 1)
plt.title("CPU - Resource Usage")

plt.plot(x, cpu_db, label = 'Face Landmark Model',color = 'green')
plt.plot(x, cpu_dl, label = 'Deep Learning Model',color = 'red')
plt.xlabel("Time (secs)")
plt.ylabel("CPU Usage (%)")
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Memory - Resource Usage")

plt.plot(x, mem_db, label = 'Face Landmark Model',color = 'green')
plt.plot(x, mem_dl, label = 'Deep Learning Model',color = 'red')
plt.xlabel("Time (secs)")
plt.legend()

cpu_avg = 0.0
for i in range(60):
    x = cpu_db[i] - cpu_dl[i]
    cpu_avg += x
cpu_avg /= 60

mem_avg = 0.0
for i in range(60):
    x = mem_db[i] - mem_dl[i]
    mem_avg += x
mem_avg /= 60


print("Avg CPU DB: " + str(sum(cpu_db)/len(cpu_db)))
print("Avg CPU DL: " + str(sum(cpu_dl)/len(cpu_dl)))
print("Avg MEM DB: " + str(sum(mem_db)/len(mem_db)))
print("Avg MEM DL: " + str(sum(mem_dl)/len(mem_dl)))

print("CPU Average: " + str(cpu_avg))
print("Memory Average: " + str(mem_avg))


plt.tight_layout()  # Ensure that the subplots don't overlap
plt.show()


