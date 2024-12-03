#pop(),  popitem(),     ------------------------------return   it delete the value of key & value if we know the key
# clear()

data = {'1': 2390, '2':3456, '3' : 943}
print(data)

value = data.pop('2')

print(data)
print(value)

#pop item delete last key - value 
data1 = {'1': 2390, '2':3456, '3' : 943}
value1 = data1.popitem()
print(data1)
print(value1)

data = {'1': 2390, '2':3456, '3' : 943, '4' : {'11' : 3542, '12' : 5474, '13': 4574}}
value = data['4'].pop('13')
print(data)

data['4'].popitem()
print(data)


