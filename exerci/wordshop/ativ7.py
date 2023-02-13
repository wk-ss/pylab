anoi,anof=map(int,input().split())
k=0
for c in range(anoi,anof):
    if c % 100 != 0 and c % 4 == 0 or c % 400 == 0:
     k=1
     print(c)
if k ==0 :
    print(-1)
