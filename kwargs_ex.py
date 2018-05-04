def my_func(**kwargs):
    print(kwargs.get('a'))
    print(kwargs)

my_func()
my_func(a=10)  # Named params
my_func(a=10, b=20)
my_func(a=1, b=2, c=3, d=4)
