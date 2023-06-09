def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
p=6421
a=3
e1=11
e2=pow(e1,a,p)
k=7
m=int(input())
y1=pow(e1,k,p)
y2=((m-a*y1)*modInverse(k,p-1))%(p-1)
first=pow(y1,y2,p)*pow(e2,y1,p)
first=first%p
second=pow(e1,m,p)
print("First = "+str(first)+" Second = "+str(second))
if first==second:
    print("Signature is valid")