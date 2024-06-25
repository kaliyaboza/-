from collections import deque
k=list(input())
p=len(k)
ans=['NO','YES']
while True:
    try:
        w=deque(list(input()))
        if len(w)!=p:
            print('NO')
            continue
        boza=True
        for i in k:
            if w[0]==i:
                w.popleft()
            elif w[-1]==i:
                w.pop()
            else:
                boza=False
                break
        print(ans[boza])
    except:
        break
        