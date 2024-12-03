#set default function   setdefault()

#1) key available ------return existing value
#2) key not available --------------------key - value pair add, return added value
data = {'1': 2390, '2':3456, '3' : 943}

value = data.setdefault('11' , 9999)

print(data,value)