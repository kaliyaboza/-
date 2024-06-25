n=int(input())
a=list(input())
b=""
ans=[]
for aaa in range(n):
    ct=0
    for i in range(0,len(a),n):
        ct+=1
        if ct%2!=0:
            b+=a[i:i+n][aaa]
        else:
            k=a[i:i+n]
            k.reverse()
            b+=k[aaa]
print(b)
        
        