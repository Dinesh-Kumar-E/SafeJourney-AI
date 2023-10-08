import sys
sys.path.append("modules")

import Face_data
import matplotlib.pyplot as plt


fid = Face_data.EAR_MAR()

face_pos = fid[2]

for i in range(68):
    print(i, face_pos[i])

x,y = [],[]

for i in face_pos:
    x.append(-1*i[0])
    y.append(-1*i[1])

plt.scatter(x,y)
plt.plot((x[16],x[0]),(y[16],y[0]), color='red')
plt.plot(((x[22]+x[21])/2,x[8]),((y[22]+y[21])/2,y[8]), color='red')
plt.show()


plt.show()