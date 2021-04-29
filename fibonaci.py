def fib(n):
    a = 0
    b = 1

    for k in range(n):
        c = a+b
        a = b
        b = c

    return b

for x in range(5):
    print(fib(x))