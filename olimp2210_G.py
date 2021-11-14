def H(H_pr,p,Z,k,L,M):
    return (H_pr+k*p+L*p*p+M*p*p*p)%Z

n,p,Z=map(int,input().split())
H_pr=2999


for i in range(n):
    H_cur,k,L,M=map(int,input().split())
    
    if H_cur!=H(H_pr,p,Z,k,L,M):
        oz=2
        while (H_cur!=H(H_pr,p,Z,k,L,oz) and oz<=5):
            oz+=1
        res=i+1,k,L,oz
    H_pr=H_cur
print(res[0],res[1],res[2],res[3])

