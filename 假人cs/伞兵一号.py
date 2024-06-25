elements={}
equal=input()+'@'
copy=equal
begin=equal.split('+')
for substance in begin:#先找元素
    substance=list(substance)
    substance.append("@")
    for i in range(len(substance)-1):
        if substance[i] in list('QWERTYUIOPASDFGHJKLZXCVBNM'):
            if substance[i+1] in list('qwertyuiopasdfghjklzxcvbnm'):
                elements[substance[i]+substance[i+1]]=0
            else:
                elements[substance[i]]=0
print(elements)
for element in elements.keys():#再找每个元素有几个
    A=copy.split(element)
    b=0
    B=[]
    for i in range(1,len(A)):
        if A[i][0] in list('1234567890'):
            a=0
            B.append(A[a])
            a=a+1
            while A[i][a] in list('1234567890'):
                B.append(A[i][a])
                a=a+1
            print(B)
            #b=int("".join(B))
        else:
            b=1
    print(b)

            
                
            
    


