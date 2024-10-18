'''Given the following code:
python
data = [[1, 2], (3.5, 4.5)]
data[1][0] = 7.5

What will be the result of this code?
 A: [1, 2], [7.5, 4.5]
 B: [[1, 2], (7.5, 4.5)]
 C: Error: 'tuple' object does not support item assignment
 D: (7.5, 4.5)
 '''
data = [[1, 2], (3.5, 4.5)]
data[1][0] = 7.5
print(data)

#Error: 'tuple' object does not support item assignment