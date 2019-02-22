import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

font = {'family':'YuGothic'}
matplotlib.rc('font',**font)

# define constant
Period_Earth = 1.00000 # 年
Period_Mars = 1.88089 # 年
Distance_Earth = 1.4960 # 億km
Distance_Mars = 2.2794 # 億km

# Angle
def angle_translator(theta):
    return 2 * np.pi * (theta - np.floor(theta))

def polar(r, theta):
    return np.array([r * np.cos(theta), r * np.sin(theta)])


def angle_on_earth(t):
    # Location of two planets
    thetaE = angle_translator(2 * np.pi * t/Period_Earth)
    thetaM = angle_translator(2 * np.pi * t/Period_Mars)
    Location_Earth = polar(Distance_Earth, thetaE)
    Location_Mars = polar(Distance_Mars, thetaM)
    Location_diff = Location_Mars - Location_Earth
    # Angle
    return np.arctan2(Location_diff[1],Location_diff[0])

time = [t/1000 for t in range(0,501)]
Xdat = []
Ydat = []
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
ims = []

for t in time:
  angle = angle_on_earth(t)
  Xdat.append(np.cos(angle))
  Ydat.append(np.sin(angle))
  Xdat = Xdat[-10:]
  Ydat = Ydat[-10:]
  im = ax.plot(Xdat,Ydat,"b")
  ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=100)
ani.save("test.gif", writer="imagemagick") 
