#zip function - it make a dictionary if we have a key & value list

key = ["ajay", "vikas", "arun", "sonam", "naman"]
value = [23,23,45,24,26]

result = dict(zip(key,value))
#result = tuple(zip(key,value))
#result = list(zip(key,value))


print(result)