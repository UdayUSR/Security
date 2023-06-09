# elgamal algorithm
p=2039

# d=random.randrange(10,50)
# e1=random.randrange(10,50)
d=11
e1=18
# e2=pow(e1,d,p)
e2=pow(e1,d,p)
print("Public Key: "+str(e1),str(e2),str(p))
print("Private Key: "+str(d))
r=8
# c1=pow(e1,r,p)
c1=pow(e1,r)%p
m=int(input("Enter the message: "))
c2=m*(pow(e2,r)%p)
print("Encrypted Message: "+str(c1),str(c2))
# x=521
# while(1):
#     x=x+1
#     n=pow(c1,d)*x
#     if(n%p==1):
#         break
    
# decrypted=(c2*x)%p
#decrypted=c2/pow(c1,d,p)
decrypted=c2/(pow(c1,d)%p)
print("Decrypted Message: "+str(decrypted))