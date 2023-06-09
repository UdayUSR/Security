# elgamal algorithm
p=5573551
d=11
e1=18
# e2=pow(e1,d,p)
e2=pow(e1,d)%p
print("Public Key: "+str(e1),str(e2),str(p))
print("Private Key: "+str(d))
r=8
# c1=pow(e1,r,p)
c=pow(e1,r)%p
m1=int(input("Enter the message m1: "))
m2=int(input("Enter the message m2: "))
c21=(m1*pow(e2,r))%p
c22=(m2*pow(e2,r))%p
print("Encrypted Message: "+str(c),str(c21))
print("Encrypted Message: "+str(c),str(c22))
c1=c*c
c2=c21*c22
x=521
while(1):
    x=x+1
    n=pow(c1,d)*x
    if(n%p==1):
        break
    
decrypted=(c2*x)%p
print("Decrypted Message: "+str(decrypted))