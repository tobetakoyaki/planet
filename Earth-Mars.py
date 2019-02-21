import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# define constant
Period_Earth = 1.00000 # 年
Period_Mars = 1.88089 # 年
Distance_Earth = 1.4960 # 億km
Distance_Mars = 2.2794 # 億km

# Angle
def planet_angle(t,T):
    alpha = 2 * np.pi * t / T
    return alpha - 2 * np.pi * np.floor(alpha / (2*np.pi))

def polar(r, theta):
    return np.array([r * np.cos(theta), r * np.sin(theta)])


def angle_on_earth(t):
    # Location of two planets
    thetaE = planet_angle(t, Period_Earth)
    # thetaM = planet_angle(t, Period_Mars)
    Location_Earth = polar(Distance_Earth, thetaE)
    #Location_Mars = polar(Distance_Mars, thetaM)
    #Location_diff = Location_Mars - Location_Earth
    # Angle
    #phi = np.arctan2(Location_diff[0],Location_diff[1])
    #return 0.5 * np.pi - thetaE + phi
    return Location_Earth

fig = plt.figure()
X, Y = [], []

def update(i):
    if i!= 0:
        plt.cla()
    
    L = angle_on_earth(i)
    X.append(L[0])
    Y.append(L[1])
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.plot(X, Y, "r")

ani = animation.FuncAnimation(fig, update, interval=10, frames=132)
ani.save("Sample.gif", writer='imagemagick')
# time = np.array(range(0,int(1e+4)))
# angle = np.array([angle_on_earth(t) for t in time])
# plt.plot(time, angle)
# plt.show()
