import numpy as np

x=0
d=0
p=0

def deriv(d,x):
    f = ((x+d)*(x+d-1) - x*(x-1))/d
    return f

if __name__ == "__main__":
    temp = input('Hello user, please input a point at which to take the derivative:')
    x = float(temp)

    for i in range(0,7):
        p += 2
        d = 1.0 / (10**(p))
        print('dd',d)
        temp = deriv(d,x)
        print(temp)



