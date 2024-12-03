number=int(input("Enter number"))
fact=1
sum=0
temp=number
while(number>0):
    digit=number%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    number=number//10
if(temp==sum):
    print(temp, "peterson number")
else:
    print(temp,"number is not peterson number")
