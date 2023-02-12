import math
x1,y1,z1 = map(int,input().split())
x2,y2,z2=map(int,input().split())
xt=(x2-x1)*(x2-x1)
yt=(y2-y1)*(y2-y1)
zt=(z2-z1)*(z2-z1)
ab=xt+yt+zt
raiz=math.sqrt(ab)

print(x1,y1,z1)
print(x2,y2,z2)
print("%2.2f"%raiz)
