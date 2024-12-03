number=int(input("Enter number "))
sum=0
temp=number
while(number>0):
    digit=number%10
    sum=sum+digit
    number=number//10  
if(temp%sum==0):
    print(temp,"is a Harshad number")
else:
    print(temp, "is a not Harshad number")