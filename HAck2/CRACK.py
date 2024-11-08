import math

def Y(x):
    return ((29**x)%251)

def X(y):
    return (math.log(y,29)%251)

x = 97+5-8
y=Y(x)
print(y)
print(X(y))

