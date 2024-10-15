#       0   1   2      3       4  5   6      7     8   9 10
list = [12, 3, 44, 'sourabh', 56, 7, 88, 'aditya', 33, 4, 5]
#      -11 -10 -9      -8     -7 -6  -5     -4 -    3 -2 -1

print (list)
a=list[3:]
print(a)
a=list[3::2]
print(a)
a=list[3:7]+list[8:]
print(a)
a=list[7:2:-1]
print(a)
a=list[-4:-9:-1]
print(a)
a=list[::-1]
print(a)


