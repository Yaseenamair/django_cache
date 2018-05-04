l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
l3 = [10, 20, 30]
d = {k: v for k, v, v2 in zip(l1, l2, l3)}

print(d)

print(zip(l1, l2, l3))
print(dict(zip(l1, l2)))
