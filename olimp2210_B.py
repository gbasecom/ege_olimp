N=int(input())
dic=dict()
for i in range(N):
    n=int(input())
    if n in dic:
        dic[n]+=1
    else:
        dic[n]=1

flag=1
for a in dic:
    if dic[a]>N//2:
        print(a)
        flag=0
        break
if (flag):print(-1)
