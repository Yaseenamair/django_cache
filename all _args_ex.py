def my_func(a, b=20, *args, **kwargs):
    print(a, b, args, kwargs)

my_func(10)
my_func(100, 200, 300)
my_func(1, 2, 3, 4, 5, x=10, y=20)
