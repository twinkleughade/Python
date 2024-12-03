number=int(input("Enter number"))
num1=0
num2=1
temp=num2
for i in range(0,number+1):
    temp=num1+num2
    num1=num2
    num2=temp
    print(temp,end=",")
    
    