number=int(input("Enter number "))
squre=number*number
sum=0
while(squre>0):
    digit=squre%10
    sum=sum+digit
    squre=squre//10
if(sum==number):
    print("neon number")
else:
    print("not Neon number")       