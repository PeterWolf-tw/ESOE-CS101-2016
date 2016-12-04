import sys  
from numpy import *  
import pylab as p  
from mpl_toolkits.mplot3d.axes3d import Axes3D  
def heart(x, y, z):  
    return (x*x + 9/4.*y*y + z*z -1)**3 - x*x*z*z*z - 9/80.*y*y*z*z*z;  
def polar_to_cartesian(u,v):  
    return (cos(u)*sin(v), sin(u)*sin(v), cos(v))  
def surf(equation, r, iter=50):  
    us = r_[0:2*pi:iter*2j]  
    vs = r_[0:pi:iter*1j]  
    xs = zeros((len(us),len(vs)))  
    ys = xs.copy()  
    zs = xs.copy()  
    for i in range(len(us)):  
        for j in range(len(vs)):  
            c = polar_to_cartesian(us[i],vs[j])  
            minrad = min(r_[0:r:iter*2j],   
                         key=lambda rad:abs(equation(rad*c[0], rad*c[1], rad*c[2])))  
            xs[i][j] = minrad*c[0]  
            ys[i][j] = minrad*c[1]  
            zs[i][j] = minrad*c[2]  
    return (xs,ys,zs)  
heartsurf = surf(heart, 2)  
fig=p.figure()  
ax = Axes3D(fig)  
ax.plot_wireframe(*heartsurf, color='r')  
#ax.plot3D(*map(ravel, heartsurf))  
p.s
