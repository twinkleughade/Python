#representation{}

#{1:"monday", 2:"tuesday", 3:"wednesday"}
d = {"one":"monday", "two":"tuesday", "three":"wednesday"}
print(d)
print(d["two"])
d["four"] = "tuesday"
d["five"] = "friday"
d["one"] = "friday"
print(d)

#another trick update
d.update({"six": "saturday"})
print(d)

#or
d1 = {"seven" : "sunday"}
d.update(d1)
print(d)