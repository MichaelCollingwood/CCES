""" Project Euler: 693 """

def finite_sequence_generator(x, y):
    a = []
    a.append(y)
    z = x
    
    while (a[-1]**2 % z != 0) and (a[-1]**2 % z != 1):
        a.append(a[-1]**2 % z)
        z += 1
    
    a.append(a[-1]**2 % z) # since while loop stops prematurely
    return a, len(a)

# print(finite_sequence_generator(5,3))

# modified function without output of sequence
def mfinite_sequence_generator(x, y):
    a = y
    z = x
    
    while (a**2 % z != 0) and (a**2 % z != 1):
        a = a**2 % z
        z += 1
    
    z += 1 # since while loop stops prematurely
    return z-(x-1) # x-1 added initially

# print(mfinite_sequence_generator(5,3))
    
def g(x):
    maxx = [0,0]
    for y in range(1,x):
        if mfinite_sequence_generator(x, y) > maxx[0]:
            maxx = [mfinite_sequence_generator(x, y), y]
    return maxx[0]

# print(g(5))
    
def f(n):
    maxx = [0,0]
    for x in range(1,n):
        if g(x) > maxx[0]:
            maxx = [g(x), x]
    return maxx[0]

print(f(100))
print(f(10000))
# in order to do these high power, must reduce order with using redundancy!