f = lambda x: x*x

print(f(10))
print(f(20))

f2 = lambda n1, n2 : n1*n2

n1 = input("Enter number1: ")
n2 = input("Enter number2: ")
p1 = f2(n1, n2)
p2 = f2(100, 200)

print(p1, p2)


f3 = lambda n: n > 0

print(f3(100))
print(f3(-10))
