# Project Euler

# do on C++ once this has been worked out

def sp5d(n):
    digits = [x for x in str(n)]
    
    summ = 0
    
    for x in digits:
        summ += int(x)**5
    
    return summ

""" 
print(99999 > sp5d(99999)) # False
print(999999 > sp5d(999999)) # True
# Set n limit at 999999
"""

f = open("Digit_Fith_Powers_graph", "w")
f.write('[')
for n in range(2, 299999): # I found from the graph that limit more like 299999
    f.write('[%.0d, %.0d],'% (n, sp5d(n)))
    
f.write('[0,0]]')

X = []
Y = []
intersections = []
f = open("Digit_Fith_Powers_graph", "r") 
for point in eval(f.read()):
    X.append(point[0])
    Y.append(point[1])
    if point[0] == point[1]:
        intersections.append(point)
    
import matplotlib.pyplot as plt
plt.plot(X, Y)
for point in intersections:
    plt.plot(point[0], point[1], '-ro')
plt.show()

print(intersections)
