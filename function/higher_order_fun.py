#map
# my_list=[10,20,30,40,50]
# def dec(x):
#     return x-5
# x=map(dec,my_list)
# print(tuple(x))

# my_list=[1,2,3,4,5]
# def square(x):
#     return x*x
# x=map(square,my_list)
# print(tuple(x))                

#filter
# my_tuple=(70,75,67,89,23,45)
# def greater(x):
#     if x>60:
#         return x
# # x=list(filter(greater,my_tuple))  #we can add type in x and with orint
# # print(x)
# x=(filter(greater,my_tuple))  
# print(list(x))

#reduce - functool name module
# import functool name module
from functools import reduce
my_tuple=(10,20,30,40,50)
def max_digitt(x,y):
    if x>y:
        return x
    else:
        return y
x=reduce(max_digitt,my_tuple)
print(x)
