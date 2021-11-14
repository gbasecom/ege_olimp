a=ord('A')
s=''
for i in range(a,a+26):
   s=s+chr(i)

matr=[s]
for i in range(1,26):
    new_s=s[i:]+s[:i]
    matr.append(new_s)
    

s_1=input()
par=input()
s_key=''
while len(s_key)<len(s_1):
    for c in par:
        s_key+=c
s_key=s_key[:len(s_1)]


res=''
for i in range(len(s_key)):
    
    res+=matr[ord(s_key[i])-ord('A')][ord(s_1[i])-ord('A')]
print(res)
