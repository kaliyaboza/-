q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m=map(int,input().split())
















n=int(input())
N=n+1
def boza(p,q=N):#p>q
    s=1
    for i in range(p-q+1,p+1):
        s=s*i
    for i in range(1,q+1):
        s=s/i
    return int(s)#算Cpq


t=int(input())
lst=[False,False]+[True]*(t-1)
prime=[]
for i in range(1,t+1):
    if lst[i]:
        prime.append(i)
    for j in prime:
        if i*j>t:
            break
        lst[i*j]=False
        if j%i==0:
            break#欧拉筛
        
        
my_dict={1:4,2:3,3:2,4:1}#lambda函数使用范例
sorted_dict_by_value = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}


L=0
R=a-1
while R-L>1:
    z=(L+R)//2
    if b[z]>e:
        R=z
    elif b[z]<e:
        L=z
    else:           
        index=z+1
        while index<a and b[index]==e:
            index+=1
        d.append(index)
        break
d.append(L+1)#二分查找