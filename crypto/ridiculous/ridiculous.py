'''
Small value of n
'''


import math
import binascii
from Crypto.Util.number import inverse

#https://www.cryptool.org/en/cto-highlights/rsa-step-by-step



n,e = 627585038806247, 65537

#from factordb

p,q=13458281,46631887

message=""
with open("message.txt") as f:
    message=f.read()

message = message[1:-1]
message=list(map(int,message.strip().split(",")))
#print(message)


phi = ( q - 1 ) * ( p - 1 ) 

d = inverse( e, phi )

out=""

for i in message:
    pt=pow(i,d,n)
    out+=chr(pt)


print(out)
