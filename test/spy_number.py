number=int(input("Enter number "))
sum=0
product=1
temp=number
while(number>0):
    digit=number%10
    sum=sum+digit
    product=product*digit
    number=number//10  
if (sum==product):
    print(temp,"spy number")
else:
    print("temp, is not spy number")                                      