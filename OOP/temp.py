import dis 


def func(a, b):
    a=2
    b=2
    c=a+b
    return c

dis.dis(func)