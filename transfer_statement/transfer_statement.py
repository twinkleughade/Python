#                                                  1
# n=int(input("enter any number"))
# i=1
# while i<=n:
#     if i==5:
#         continue
#     else:
#         print(i)
#     i=i+1
# #output - 1 2 3 4 5 

#                                                   2 

# n=int(input("enter any number"))
# i=1
# while i<=n:
#     if i==5:
#         pass
#     else:
#         print(i)
#     i=i+1
#output - 1 2 3 4 6 7 

#                                                            3
# n=int(input("enter any number"))
# i=1
# while i<=n:
#     if i==5:
#         i=i+1
#         continue
#     else:
#         print(i)
#     i=i+1
#output 1 2 3 4 6 7 

#                                                          4
# n=int(input("enter any number"))
# i=1
# while i<=n:
#     if i==5:    
#         break
#     else:
#         print(i)
#     i=i+1

#                                                       5

while True:
    print("1.for add,2.for subtract,3.mul,4.div")
    n=int(input("enter your choice"))
    x=[1,2,3,4]
    if n in x:
        x=int(input("enter first value"))
        y=int(input("enter second value"))
        if n==1:
            print("addition =", x+y)
        elif n==2:
            print("subtraction =", x-y)
        elif n==3:
            print("multiply =", x*y)
        elif n==4:
            print("division =", x/y)
    elif n==5:
        break
    else:
        print("please enter right number")
