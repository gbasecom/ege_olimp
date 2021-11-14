N=int(input())
a,b=map(int,input().split())
arr=list(map(int,input().split()))
err=0
arr_set=set(arr)
len_arr=len(arr)
len_set=len(arr_set)

if len_arr>len_set:
    err+=2
if any((x<a or x>b) for x in arr):
    err+=4
if all((arr[i]<=arr[i+1]) for i in range(len_arr-1)):
    err+=1
  
if all((arr[i]>=arr[i+1]) for i in range(len_arr-1)):
    err+=1
print(err)



