def add(*args):
    i = 0
    for j in args:
        i += j

    return i

add(1,2,3,4)

def calculate(**kwargs):
    print(kwargs)
    type(kwargs)


calculate(add=3, multiply=5)