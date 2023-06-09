import math
import random

m1=int(input("Enter the message m1 to be encrypted: \n"))
m2=int(input("Enter the message m2 to be encrypted: \n"))
m=m1*m2

p=int(input("Enter the value of p: \n"))
q=int(input("Enter the value of q: \n"))
n=p*q
phi=(p-1)*(q-1)

e=random.randint(2,phi-1)
while math.gcd(e,phi)!=1:
    e=random.randint(2,phi-1)

d=pow(e,-1,phi)

print("Value of e is: \n",e)
print("Value of d is: \n",d)

c1=pow(m1,e,n)
d1=pow(c1,d,n)
c2=pow(m2,e,n)
d2=pow(c2,d,n)
print("Encrypted Message c1 is: \n",c1)
print("Decrypted Message d1 is: \n",d1)
print("Encrypted Message c2 is: \n",c2)
print("Decrypted Message d2 is: \n",d2)
print("Multiplied Encrypted Message c1*c2 is: \n",c1*c2)
print("Multiplied Decrypted Message of c1*c2 is: \n",pow(c1*c2,d,n))

c=pow(m,e,n)
x=pow(c,d,n)
print("Encrypted Message c is: \n",c)
print("Decrypted Message x is: \n",x)
