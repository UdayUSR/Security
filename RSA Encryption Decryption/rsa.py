import math
import random
# from sympy import mod_inverse


p=int(input("Enter the first prime number:\n"))
q=int(input("Enter the second prime number:\n"))
n=p*q
phi=(p-1)*(q-1)
e=random.randint(2,phi-1)
while math.gcd(e,phi)!=1:
    e=random.randint(2,phi-1)

# k=0
# while True:
#     d=(1+phi*k)/e
#     if d.is_integer():
#         d=int(d)
#         break
#     k+=1
d=pow(e,-1,phi)

print("Public key: n=",n,"e=",e)
print("Private key: d=",d)

print("Enter the message to be encrypted: ")
m=int(input())
# c=(m**e)%n
c=pow(m,e,n)
print("Encrypted message: ",c)
# x=(c**d)%n
x=pow(c,d,n)
print("Decrypted message: ",x)