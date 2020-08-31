import numpy as np
import pandas as pd


def FirstDev(x=None,s=None,g=None):
    xx = x.shape[0]
    xy = x.shape[1]
    sd1= np.zeros([xx,xy])
    for i in range(int(s + g / 2 + 0.5), int(xy - s - g / 2 + 0.5)):
        sa=np.mean(x[:,int(i - s - g / 2 + 0.5):int(i - g / 2 - 0.5)], axis = 1)
        sc=np.mean(x[:,int(i + g / 2 + 0.5):int(i + g / 2 - 0.5 + s)], axis = 1)
        sd1[:,i]=sc - sa
    return sd1
# a = np.array([1,2,3,4]) #[N,1]
# b = np.array([[5],[6],[7],[8]]) #[1,N]
# print(a.shape) #ขนาดข้อมูล 4x1
# print(b.shape) #ขนาดข้อมูล 1x4
# print(a*b) #จะได้ขนาดข้อมูล 4x4
# print((a*b).T)
# print(a.dot(b)) #จะได้ขนาดข้อมูล = 1
# a = np.array([5,6,7,8]) #[N,1]
# b = np.array([[1],[2],[3],[4]]) #[1,N]
# print(a*b) 

f = open("gelato-graph-calculator/test.txt", "r")
line = 0
B = []
for x in f:
    if(line >= 8):
        if(x == "\n"):
            continue;
        tmp = x.split(";")
        # print(float(tmp[4]),"+++",line)
        B.append([float(tmp[4])])
    line+=1
f.close()

B = np.array(B)
X = pd.read_excel('gelato-graph-calculator/TEST_S5G5.xlsx', sheet_name='X', header = None)
x = np.array(X)
X = np.array(X)

print("Data from file calibrate :",X[0].shape)
print("Data from specific folder :",B.shape)
s = 5
g = 5
tmp = X[0].dot(B)
print("results X[0].dot(B) :", tmp)

raw = tmp*(X[0].T)
print("raw :",raw.shape)
first = tmp*FirstDev(x,s,g)

print("first :",first.shape)


