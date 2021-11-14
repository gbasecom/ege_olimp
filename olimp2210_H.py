
    


N,S=map(int,input().split())
a=[]
for i in range(N):
    a.append(list(map(int,input().split())))
k_sv=set()
k_sv.add(S-1)

def kompon(el):
    for i in range(N):
        if (a[el][i]==1):
            if i not in k_sv:
                k_sv.add(i)
                kompon(i)

kompon(S-1)
print(len(k_sv))
