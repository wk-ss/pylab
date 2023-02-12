list=[]
n=0
while n!=99:
    n = int(input("numedo"))
    if (n!=99):
        list.append(n)
list.sort(reverse=True)
secmaior=list[1]
print(secmaior)
