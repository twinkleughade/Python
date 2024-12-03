'''
n=int(input("enter any no:"))
i=1
while i<=n:
    print(i,end=',') #infite loop
    i=i+1   #it give comma in last but we dont want it
    '''
#-------------------     1         -----------------------
'''
WAP to print the number 1 to n
n=int(input("enter any no:"))
i=1
while i<=n:
    if i<n:
        print(i,end=',')
    else:
        print(i)
    i=i+1
    '''
#------------------       2       ------------------------------
#WAP tp print even number from 2 to 10
'''n=int(input("enter any no:"))
i = 1
while i<=n:
    if n%2==0:
        if i%2==0:
            if i<=(n-2):
                print(i,end=',')
            else:
                print(i)
    else:
        if i%2==0:
            if i<=(11-2):
                print(i,end=',')
            else:
                print(i)
    i=i+1
'''
 #                      or

'''n=int(input("enter any no:"))
i=1
while i<=n:
    if i%2==0:
        if i<=(n-2):
            print(i,end=',')
        else:
            print(i)
    i=i+1'''
          
#---------------------           3        -------------------------------
#write a program to print even 10 even numbers
'''n=int(input("enter any no:"))
i=1
while i<=n:
    if i<n:
        print (2*i,end=',')
    else:
        print(2*i)
    i=i+1'''

   
#---------------------           4        ------------------------------
#write a program to find odd numbers 1 to 10                                      
'''n=int(input("enter any no:"))
i = 1
while i<=n:
    if n%2!=0:
        if i%2!=0:
            if i<=(n-2):
                print(i,end=',')
            else:
                print(i)
    else:
        if i%2!=0:
            if i<=(n-2):
                print(i,end=',')
            else:
                print(i)
    i=i+1'''

#------------------------           5            ---------------------------

'''n=int(input("enter any no:"))
i=1
while i<=n:
    if i<n:
        print (2*i-1,end=',')
    else:
        print(2*n-1)
    i=i+1'''
  

#----------------------             6            ---------------------------
#write a program to print  numbers  1+2+3+4+5+6+7+8+9+10=
'''n=int(input("enter the number"))
i=1
s=0
while i<=n:
    s=s+i
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
    s=s+i
    i=i+1
print(s)'''
       

#---------------------7 --------------------------------------
#print tghe sum of even or odd
'''n=int(input("enter any no:"))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
        if i<=(n-2):
            print(i,end='+')
        else:
            print(i,end='=')
    i=i+1
print(sum)'''     

#------------------------   8   ----------------------------------
#print the sum of odd
'''n=int(input("enter any no:"))
i=1
sum=0
while i<=n:
    if i%2!=0:
        sum=sum+i
        if i<=(n-2):
            print(i,end='+')
        else:
            print(i,end='=')
    i=i+1
print(sum)'''     

#=================================    for -loop    ===================================
#print the number n natural number
'''n=int(input("Enter any number"))
for i in range(1,n+1):
    if i<=(n-1):
        print(i,end=',')
    else:
        print(i)'''

# print the sum of all natural numbers
'''n=int(input("Enter any number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    if i<=(n-1):
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)'''

#print the even numbers upto 10 
'''n=int(input("Enter any number"))
for i in range(2,11,2):
    if i<=(n-1):
        print(i,end=',')
    else:
        print(i)'''

# print sum of all even numbers                               ****
'''n=int(input("Enter any number"))
sum=0
for i in range(0,n,2):
    sum=sum+i
    if i<=(n-2):
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)'''

#print the 10 even numbers
'''n=int(input("Enter any number"))
for i in range(1,n+1):
    if i<n:
        print (2*i,end=',')
    else:
        print(2*n)'''
    
#print 10 odd numbers
'''n=int(input("Enter any number"))
for i in range(1,n+1):
    if i<n:
        print (2*i-1,end=',')
    else:
        print(2*n-1)'''


#==============       string      ==============
'''n=input("Enter any string")
v=0
c=0
for i in n:
    x=['a','e','i','o','u','A','E','I','O','U']
    if i in x:
        v=v+1
    else:
        c=c+1
print(v)
print(c)'''