a = []
for i in range(0,3):
    sub = []
    r = 3
    c = 3
    print("enter values for row",1)
    for j in range(0,3):
        print("enter values for column",1)
        ele = int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)
    print(a)  

    d = ()
    ans = []
    for i in range(0,r):
        for j in range(0,c):
            if a[i][j] not in d:
                d[a[i][j]] = 1
            else:
                d[a[i][j]] +=1
                if d[a[i][j]]==2:
                    ans.append(a[i][j])
print(d)
#missing
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
print(d)
print(ans)                                

