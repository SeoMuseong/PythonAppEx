a = [0,1,2,3,4]
print(a[:3], a[:-3])
print(a[::-1])

first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]

order = [first, second, third]
print(order)
john = [order[0][:-2],second[1::3], third[0]]
print(john)
del john[2]
print(john)
john.extend([order[2][0:1]])
print(john)

list_a = [3,2,1,4]
list_b = list_a.sort()
print(list_a, list_b)