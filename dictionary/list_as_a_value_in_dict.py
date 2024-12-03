d = {1:["ajay", 23, "bhopal"], 2:["jay", 23, "ujjain"]}
print(d)
print(d[1])
print(d[1][2])
d[1][2] = "ujjain"
print(d)
d[2][2] = "indore"
print(d)


d1 = {101:{"name" : "ajay", "age":23, "city":"bhopal"}, 102:{"name":"jay", "age":23, "city":"ujjain"}}
print(d1)
print(d1[101])
print(d1[101]["city"])
print(d1["102"]["ujjain"]) = "indore"
d1.update[102]({"city":"indore"})
print(d1)


