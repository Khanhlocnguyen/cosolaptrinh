import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
s=(a+b+c)/2
DienTich=round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)
print("Dien tich=",DienTich,sep="")