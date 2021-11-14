s=input()
if s.count('.')!=3:
    print('NO')
else:
    a=s.split('.')
    if any(((len(x)>1) and (x[0]=='0')) for x in a):
        print('NO')
    elif any(int(x)>255 for x in a):
        print('NO')
    else:
        print('YES')
        
    
