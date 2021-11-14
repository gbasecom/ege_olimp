

N,M=map(int,input().split())
arr=[]
M=M*1000
for i in range(N):
    spl=input().split()
    a=list(map(int,spl[2:]))
    arr.append(a[0]*a[1])
print(arr)
len_arr=len(arr)

def max_w(ost):
    if len(ost)==0: return 0
    if len(ost)==1: return ost[0]
    new_ost=[]
    ves_max=0
    ves=0
    for i in range(len(ost)):
        for el in ost[:i]+ost[i+1:]:
            if el<=M-ost[i]:
                new_ost.append(el+ost[i])
        ves=max_w(new_ost)
        ves_max=max(ves_max,ves)
    
print(max_w(arr))
    
    



