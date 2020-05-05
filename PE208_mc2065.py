# Robot Walks ProjectEuler Problem 208
import numpy as np
from copy import copy

total = 0
l = np.sqrt(2-2*np.cos(0.4*np.pi))
c_paths = []

def dr(theta, direction): # direction either 1 or -1
    return [l*np.sin(theta + 36 * direction), l*np.cos(theta + 36 * direction)]


def n_state(prev_r, prev_bearing, direction):
    # sorts out new coords and angle from previous
    #al = add_link(n - 1) # previous coordinates and angle
    prev_x = prev_r[0]
    prev_y = prev_r[1]
            
    r = [  (  prev_x + dr(prev_bearing, direction)[0]  )  ,  (  prev_y + dr(prev_bearing, direction)[1]  )  ]
    bearing = prev_bearing + 0.4 * np.pi * direction
            
    # and sends them up
    return r, bearing



r = [0,0]
bearing = 0

def f(r_i, bearing_i, n, temp_r_log = []):
    global total, c_paths
    
    for i in [-1, 1]:
        #print(n_state(r_i, bearing_i, i))
        
        r, bearing = n_state(r_i, bearing_i, i) # done
        temp_r_log.append(r)
        
        #print(temp_dir_log)
        
        if (n != 1):
            f(r, bearing, n-1, temp_r_log)
            
        else:
            #print(r,bearing)
            if (float("%.2f" % r[0]) == 0.00):
                if (float("%.2f" % r[1]) == 0.00):
                    if (float("%.2f" % (abs(bearing) % 6.283185)) == 0.00):
                        #print('yippee')
                        total += 1
                        c_paths.append(copy(temp_r_log))
        temp_r_log.pop()

f(r, bearing, 15)
#print(c_paths)
print("total: ", total)


# plot r's
import matplotlib.pyplot as plt
import numpy as np
for path in c_paths:
    x = []
    y = []
    for coord in path:
        x.append(coord[0])
        y.append(coord[1])
    x.append(path[0][0])
    y.append(path[0][1])
    
    axes = plt.gca()
    axes.set_xlim([-5,5])
    axes.set_ylim([-5,5])
    plt.plot(x, y, 'C3', zorder=1, lw=3)
    plt.show()
