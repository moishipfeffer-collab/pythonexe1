#section 1
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)
numbers2=[3, 1, 4, 1, 5, 9, 2, 6]
sortednum=sorted(numbers)
print(numbers2,sortednum)
#section 2
a = [1, 2, 3]
b = [4, 5, 6]
c=a+b
print(c)
a.extend(b)
print(a)
#section 3
items = ['x', 'y', 'z', 'x', 'y', 'x']
print(items.count("x"))
items.remove("x")
items.remove("x")
items.remove("x")
print(items)
#section 4
data = [1, 2, 3, 4, 5]
print(data[::2])
# section 5
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])



