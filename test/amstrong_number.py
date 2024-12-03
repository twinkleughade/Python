number=int(input("Enter number "))
product=0
temp=number
while(number>0):
    digit=number%10
    product=product+digit**3
    number=number//10
if(temp==product):
    print(temp,"amstrong number")
else:
    print(temp,"not a astrong number")