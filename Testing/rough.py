import random
import math

x = list(range(0, 60))
y_dlib = []
y_dl = []

for _ in range(60):
    y_dlib.append(random.randint(25,35))

for _ in range(60):
    y_dl.append(random.randint(12,19))


diff = []

for i in range(60):
    diff.append(y_dlib[i] - y_dl[i])

print(sum(diff)/len(diff))