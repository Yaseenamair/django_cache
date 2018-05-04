def push(l, e):
    l.append(e)
    return l


def pop(l):
    l.pop()
    return l


l = ['a', 'b', 'c', 'd', 'e', 'f']
print(l)
print(push(l, 'g'))
print(pop(l))
print(pop(l))
print(push(l, 'x'))

