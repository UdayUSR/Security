p=15527
alpha=2
t=0
while t<100:
    i=1
    day=[]
    while(i<p):
        x=(alpha**i)%p
        day.append(x)
        # print(x)
        i=i+1
    day.sort()
    q=0
    i=1
    j=0
    while(i<p):
        # print(day[j])
        if(day[j]!=i):
            q=1
            # print("Not Primitive")
            break
        i=i+1
        j=j+1

    if(q==0):
        print(str(alpha)+" is Primitive")
    else:
        print(str(alpha)+" is not Primitive")
    t=t+1
    alpha=alpha+1
