a=[]
num=int(input())
for i in range(num):
    B=list(input())
    while '-'in B:
        B.remove("-")
    for j in B:
        a.append(j)#移除-，并且打散放一起

for i in range(len(B)):
    if a[i] in ['A','B','C']:
        a[i]='2'
    elif a[i] in ['D','E','F']:
        a[i]='3'
    elif a[i] in ['G','H','I']:
        a[i]='4'
    elif a[i] in ['J','K','L']:
        a[i]='5'
    elif a[i] in ['M','N','O']:
        a[i]='6'
    elif a[i] in ['P','R','S']:
        a[i]='7'
    elif a[i] in ['T','U','V']:
        a[i]='8'
    elif a[i] in ['W','X','Y']:
        a[i]='9'#转化
c=[]
for i in range(0,len(a),7):
    d=[]
    d.append(a[i])
    d.append(a[i+1])
    d.append(a[i+2])
    d.append('-')
    d.append(a[i+3])
    d.append(a[i+4])
    d.append(a[i+5])
    d.append(a[i+6])
    e=''.join(d)
    c.append(e)
c.sort()#包装，整理
d=c[:]
w=0
for i in range(len(d)):
    p=len(c)
    if d[i] in c:
        while d[i] in c:
            c.remove(d[i])
        if p-len(c)!=1:
            print(d[i]+" "+str(p-len(c)))
        else:
            w=w+1
if w==len(d):#一个重复的都没有
    print('No duplicates.')
    
        
    
    


    
