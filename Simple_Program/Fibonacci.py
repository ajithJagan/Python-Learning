from tokenize import endpats


def fibonacci(input_num: int):
    first, second, add = 0, 1, 0
    for i in range(0, input_num, 1):
        print(first, end=" ")
        add = first + second
        first = second
        second = add


fibonacci(5)
print()


def new_fib(num: int):
    a, b = 0, 1
    for _ in range(num):
        print(a,end=" ")
        a, b = b, a + b   # Here I am just swapping the variable

new_fib(5)
