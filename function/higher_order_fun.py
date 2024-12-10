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
# from functools import reduce
# my_tuple=(10,20,30,40,50)
# def max_digitt(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=reduce(max_digitt,my_tuple)
# print(x)

#lambda
# x=lambda x:x**2                     #for single variable
# print(x(5))

# x=lambda x,y,z,p,q,r : x+y-z/p%q//r
# print(x(1,2,3,4,5,6))

#for odd number
# my_list=[10,15,20,25,30]
# x=list(filter(lambda x: x%2==0,my_list))
# print(x)


#for sum of odd

# from functools import reduce
# my_list=[10,15,20,25,30]
# x=filter(lambda x: x%2==0,my_list)
# y=reduce(lambda x,y:x+y,x)
# print(y)

#                   or

# import functools
# my_list=[10,15,20,25,30]
# x=filter(lambda x: x%2==0,my_list)
# y=functools.reduce(lambda x,y:x+y,x)
# print(y)

#                square than sum
# from functools import reduce
# my_list=[10,15,20,25,30]
# even_data=list(filter(lambda x: x%2==0,my_list))
# sqr_even=list(map(lambda x:x**2,even_data))
# sqr_sum=reduce(lambda x,y:x+y,sqr_even)
# print(even_data)
# print(sqr_even)
# print(sqr_sum)

#                sum than square
# from functools import reduce
# my_list=[10,15,20,25,30]
# even_data=filter(lambda x: x%2==0,my_list)
# sum_even=reduce(lambda x,y:x+y,even_data)
# sum_sqr=sum_even**2
# print(even_data)
# print(sum_even)
# print(sum_sqr)


#                                Decorator
#representation @
def outer_function(func):
    def inner_function(x,y):
        x=x+5
        y=y+5
        data=func(x,y)
        return data
    return inner_function
@outer_function
def main_function(x,y):
    z=x+y 
    return z
data=main_function(5,10)
print(data)




