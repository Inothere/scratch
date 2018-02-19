print 'Hello world'
def fib(n):
    i = 0
    a = 0
    b = 1
    if n == 0:
        return 0
    for i in range(n):
        c = b
        b = a+b
        a = c
    return b

def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n - 1) + fib2(n - 2)

if __name__ == '__main__':
    for i in range(5):
        print fib(i)