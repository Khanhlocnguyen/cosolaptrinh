n=int(input("So tien ban dau: "))
k=int(input("So thang gui: "))
T=float(input("Lai suat/ thang: "))
m=n*(1+k*T)
print("Voi so tien ban dau",n,end=",")
print(" sau",k,end=" ")
print("thang gui",sep="",end=",")
print(" lai suat",T,end="")
print("/ thang",sep="")
print("Thi so tien nhan duoc cuoi ky la:",m)