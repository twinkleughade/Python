'''Number=int(input("Enter number \n"))
x=Number+1
check=0
for i in range(1,x):
    if(i*i==x):
        check=1
        break
if (check==1):
    print(Number,"= is sunny number") 
else:
    print(Number,"= is not sunny number")'''   


Number=int(input("Enter number \n"))
sum=0
product=0
temp=0
while(Number>0):
    digit=Number%10
    sum=digit+sum
    product=digit**2+product
    Number=Number//10
while(product>0):
    digit1=product%10
    temp=digit1+temp
    product=product//10
if(sum==temp):
    print("sunny number")
else:
    print("not sunny number")    



