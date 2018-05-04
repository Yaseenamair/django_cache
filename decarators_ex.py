def is_positive(f):
    print("Inside decorator")

    def my_helper(x, y):
        print("isndie Helper")
        if x > 0 and y > 0:
            return f(x, y)
        else:
            return "Please enter positive numbers only"

    return my_helper


@is_positive
def my_sum(n1, n2):
    print("Insude my_sum()")
    return n1 + n2


print("Calling my_sum()")
print(my_sum(10, 20))
print('#'*20)
print(my_sum(-1, -2))
