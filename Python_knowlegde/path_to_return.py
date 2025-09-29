"""

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.


"""



def fun():
    try:
        return 2
    except:
        return 4
    else:
        return 5
    finally:
        return 8


print(fun())

